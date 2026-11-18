import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error

USE_GEMINI = True


CACHE_FILE = os.path.expanduser(
    "~/configs/NF0MakKkeR/genre_cache.json"
)

DISCOGS_HEADERS = {
    "User-Agent": "GenreLookup/1.1"
}

token = os.environ.get("DISCOGS_TOKEN")
if token:
    DISCOGS_HEADERS["Authorization"] = f"Discogs token={token}"

MUSICBRAINZ_HEADERS = {
    "User-Agent": "GenreLookup/1.1 (music metadata script)"
}


def normalize(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def normalize_artist(text):
    # Ignore case and extra spaces, but preserve punctuation.
    return " ".join(text.split()).casefold()


def get_json(url, headers):
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request, timeout=8) as response:
        return json.loads(response.read().decode("utf-8"))


def join_genres(genres):
    result = []
    seen = set()

    for genre in genres:
        if isinstance(genre, dict):
            genre = genre.get("name", "")

        genre = genre.strip()

        if genre and genre.casefold() not in seen:
            result.append(genre)
            seen.add(genre.casefold())

    return " | ".join(result) or None



def has_exact_artist(release, artist):
    target = normalize_artist(artist)

    return any(
        normalize_artist(member.get("name", "")) == target
        for member in release.get("artists", [])
        if isinstance(member, dict)
    )


def has_musicbrainz_artist(artist_credit, artist):
    target = normalize_artist(artist)

    for part in artist_credit:
        if isinstance(part, dict):
            member = part.get("artist", {})
            name = member.get("name", "") if isinstance(member, dict) else ""
            name = name or part.get("name", "")
        elif isinstance(part, str):
            name = part
        else:
            continue

        if normalize_artist(name) == target:
            return True

    return False



def load_cache():
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return {}




def save_cache(artist, album, genre, source):
    if not genre:
        return

    try:
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)

        cache = load_cache()
        key = normalize_artist(artist)
        entry = cache.get(key, {})

        # Migrate an older single-entry cache into the new structure.
        if "metadata" not in entry and "gemini" not in entry:
            old_source = entry.get("source", "legacy")

            if entry.get("genre"):
                old_entry = entry
                old_slot = "gemini" if old_source == "gemini" else "metadata"

                entry = {
                    "artist": old_entry.get("artist", artist),
                    "metadata": None,
                    "gemini": None
                }

                entry[old_slot] = {
                    "album": old_entry.get("album", ""),
                    "genre": old_entry["genre"],
                    "source": old_source
                }
            else:
                entry = {
                    "artist": artist,
                    "metadata": None,
                    "gemini": None
                }

        entry.setdefault("metadata", None)
        entry.setdefault("gemini", None)
        entry["artist"] = artist

        # Keep metadata and Gemini results separately.
        slot = "gemini" if source == "gemini" else "metadata"

        entry[slot] = {
            "album": album,
            "genre": genre,
            "source": source
        }

        cache[key] = entry

        temp_file = CACHE_FILE + ".tmp"

        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(cache, file, indent=4, ensure_ascii=False)

        os.replace(temp_file, CACHE_FILE)

    except (OSError, TypeError, AttributeError):
        pass


def cached_genre(artist, cache_type):
    cache = load_cache()
    entry = cache.get(normalize_artist(artist))

    if not isinstance(entry, dict):
        return None

    if normalize_artist(entry.get("artist", "")) != normalize_artist(artist):
        return None

    # Support both the old and new cache formats.
    if "metadata" in entry or "gemini" in entry:
        result = entry.get(cache_type)
    else:
        source = entry.get("source", "legacy")

        if cache_type == "gemini" and source == "gemini":
            result = entry
        elif cache_type == "metadata" and source != "gemini":
            result = entry
        else:
            return None

    if not isinstance(result, dict) or not result.get("genre"):
        return None

    return result["genre"], result.get("source", "legacy")


def discogs_genre(artist, album):
    try:
        params = urllib.parse.urlencode({
            "artist": artist,
            "release_title": album,
            "type": "release",
            "per_page": 10
        })

        url = "https://api.discogs.com/database/search?" + params
        results = get_json(url, DISCOGS_HEADERS)

        for result in results.get("results", []):
            release_id = result.get("id")

            if not release_id:
                continue

            release = get_json(
                f"https://api.discogs.com/releases/{release_id}",
                DISCOGS_HEADERS
            )

            if (
                has_exact_artist(release, artist)
                and normalize(release.get("title", "")) == normalize(album)
            ):
                genre = join_genres(release.get("genres", []))

                if genre:
                    return genre

        return None

    except Exception:
        return None


def musicbrainz_genre(artist, album):
    try:
        query = f'releasegroup:"{album}" AND artist:"{artist}"'

        params = urllib.parse.urlencode({
            "query": query,
            "fmt": "json",
            "limit": 10
        })

        url = "https://musicbrainz.org/ws/2/release-group/?" + params
        results = get_json(url, MUSICBRAINZ_HEADERS)

        for result in results.get("release-groups", []):

            if (
                not has_musicbrainz_artist(
                    result.get("artist-credit", []), artist
                )
                or normalize(result.get("title", "")) != normalize(album)
            ):
                continue

            time.sleep(1)

            release_id = result["id"]

            genre_url = (
                f"https://musicbrainz.org/ws/2/release-group/"
                f"{release_id}?inc=genres&fmt=json"
            )

            release = get_json(genre_url, MUSICBRAINZ_HEADERS)
            genre = join_genres(release.get("genres", []))

            if genre:
                return genre

        return None

    except Exception:
        return None


def discogs_other_album_genre(artist, current_album):
    try:
        params = urllib.parse.urlencode({
            "artist": artist,
            "type": "release",
            "per_page": 10
        })

        url = "https://api.discogs.com/database/search?" + params
        results = get_json(url, DISCOGS_HEADERS)

        for result in results.get("results", []):
            release_id = result.get("id")

            if not release_id:
                continue

            release = get_json(
                f"https://api.discogs.com/releases/{release_id}",
                DISCOGS_HEADERS
            )

            release_title = release.get("title", "")

            # Exact individual artist match, including collaborations.
            if not has_exact_artist(release, artist):
                continue

            # Do not borrow the genre from another edition of this album.
            if normalize(release_title) == normalize(current_album):
                continue

            genre = join_genres(release.get("genres", []))

            if genre:
                return genre, release_title

        return None

    except Exception:
        return None


def gemini_genre(artist, album):
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("[Gemini] API key not configured.", file=sys.stderr)
        return None

    model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

    prompt = f"""
Identify the most accurate music genres for this album:

Artist: {artist}
Album: {album}

Return only the genres, separated by " | ".

Rules:
- Prefer specific genres over broad ones.
- Use established music genre names.
- Do not invent genres.
- If you cannot confidently identify the album, return exactly: UNKNOWN
- Do not include explanations or the artist/album names.
"""

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/"
        f"models/{model}:generateContent"
    )

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 40
        }
    }

    try:
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": api_key
            },
            method="POST"
        )

        
        for attempt in range(2):
            try:
                with urllib.request.urlopen(request, timeout=10) as response:
                    data = json.loads(response.read().decode("utf-8"))
                break

            except urllib.error.HTTPError as error:
                if error.code == 503 and attempt == 0:
                    print(
                        "[Gemini] Server busy. Retrying in 2 seconds...",
                        file=sys.stderr
                    )
                    time.sleep(2)
                    continue
                raise


        result = data["candidates"][0]["content"]["parts"][0]["text"]
        result = result.strip().strip('"').strip("'")

        if not result or result.upper() == "UNKNOWN":
            print("[Gemini] No confident genre found.", file=sys.stderr)
            return None

        # Reject excessively long or malformed responses.
        if len(result) > 150 or "\n" in result:
            print("[Gemini] Unexpected response format.", file=sys.stderr)
            return None

        print(f"[Gemini] Genre found: {result}", file=sys.stderr)
        return result

    except Exception as error:
        print(f"[Gemini] Request failed: {error}", file=sys.stderr)
        return None



def get_genre(artist, album):

    # 1. Exact album on Discogs
    genre = discogs_genre(artist, album)

    if genre:
        save_cache(artist, album, genre, "discogs")

    # 2. Exact album on MusicBrainz
    if not genre:
        genre = musicbrainz_genre(artist, album)

        if genre:
            save_cache(artist, album, genre, "musicbrainz")

    # 3. Cached Discogs/MusicBrainz result
    if not genre:
        cached_metadata = cached_genre(artist, "metadata")

        if cached_metadata:
            genre, source = cached_metadata
            print(
                f"[Cache] Reusing {source} result: {genre}",
                file=sys.stderr
            )

    # 4. Another album by this exact artist on Discogs
    if not genre:
        other_album = discogs_other_album_genre(artist, album)

        if other_album:
            genre, source_album = other_album
            save_cache(artist, source_album, genre, "discogs_other")

    # 5. Fresh Gemini lookup (optional)
    if not genre and USE_GEMINI:
        genre = gemini_genre(artist, album)

        if genre:
            save_cache(artist, album, genre, "gemini")

    # 6. Cached Gemini fallback
    if not genre:
        cached_gemini = cached_genre(artist, "gemini")

        if cached_gemini:
            genre, source = cached_gemini
            print(
                f"[Cache] Gemini lookup failed or returned no result. "
                f"Reusing previous Gemini genre: {genre}",
                file=sys.stderr
            )

    # 7. Nothing found
    return genre or "/"


if __name__ == "__main__":
    artist = sys.argv[1]
    album = sys.argv[2]

    print(get_genre(artist, album))
