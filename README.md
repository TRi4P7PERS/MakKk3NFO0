# MakKk3NFO0
MakKke NFO: A cli version of Music NFO Builder, for Linux :) .

## Features

- Generate NFO files for individual albums or complete artist discographies.
- Support multi-volume albums with one combined NFO.
- Automatically number tracks, including leading zeros.
- Calculate total playing time and file size.
- Can also produce an nfo for singles in a discography NFO.
- Retrieve genres using Discogs, MusicBrainz, cached metadata and an optional Gemini fallback.
- Customize the release group signature and final message.

## Installation 😊:

### Requirements:

- Linux
- Python 3.10 or newer
- MediaInfo
- Beautiful Soup 4


On Debian/Ubuntu, install MediaInfo and the Python virtual environment support:

```bash
sudo apt install mediainfo python3-venv
```

Clone the repository:

```
git clone https://github.com/TRi4P7PERS/MakKk3NFO0.git
cd MakKk3NFO0
```

(Recommended) Create and activate a virtual environment: `You can also skip this step, then you'll be able to run MaKeNfO w/o the virtual environment, but will also have Beautiful Soup 4 installed outside a virtual environment.`

```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
```

Install the required Python package:

```
pip install beautifulsoup4
```

## Configuration

Create the `~/.configs` folder if it doesn't exist:

```bash
mkdir -p ~/.configs
```

Then copy configuration files from the cloned repo into it :) :

```bash
cp SiG.nfo Me.nfo TemPla7Ǝ.nfo ~/.configs/
```

### The script uses the following files:

SiG.nfo — Your release group signature.

Me.nfo — Your final message for the NFO. 😊

TemPla7Ǝ.nfo — The NFO template used to generate the output.

Place these files inside `~/.configs` , and edit them to your needs (besides `TemPla7Ǝ.nfo`).

### Automatic Genre Lookup

Genres are retrieved from Discogs, MusicBrainz and (optional) from Gemini as a last resort.

To configure Gemini, add your API key to `~/.bashrc`:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

Then reload your shell configuration:

```bash
source ~/.bashrc
```

If you wish to turn off genre lookup with Gemini just change the line `USE_GEMINI = True` to `USE_GEMINI = False` in the `GetGenre.py` file.

Support for cached genres is added, while also having the support for using the genre of another album from the same artist for fallback 😁.

## Usage

Run the script with an album or discography directory:

```
python3 MaKeNfO.py "/path/to/Artist - Album"
```

Or launch it without arguments and enter the path when prompted:

```
python3 MaKeNfO.py
```

Sidenote: Albums should use the "Artist - Album" naming convention :) .

## Scripts End Result

<img width="508" height="845" alt="image" src="https://github.com/user-attachments/assets/60c2c310-19c6-4a2b-a668-99c891e5e6f3" />



Enjoy 😊.
