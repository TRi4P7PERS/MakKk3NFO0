# MakKk3NFO0
MakKke NFO: A cli version for Linux only, of Music NFO Builder :) .

#Installation 😊:

Create a virtual enviorment with python, choose a folder before where you want it then after you create it install the needed repos from pip, copy the files from the github repository in and it should work.

Creating a virtual enviorment:

    - Run `python -m venv /path/to/new/virtual/environment` where path is your path


    You'll have to run `source bin/activate` in that folder then install the requirements :) .

Things to install with pip: (Run the following commands to install needed software to run this wrapper 😊)

    - `pip install bs4`


The SiG.nfo is where you put your release group signature.
Me.nfo is where you put your last message 4 the torrent 😊. Both have to be placed in the home folder in .configs folder :) .

Gemini genre lookup added on last update, you'll have to add your Gemini API key (you can add it at the end of the file) to your `~/.bashrc` like so (to open it in a file editor use the `nano ~/.bashrc` command):

`export GEMINI_API_KEY="YOUR.API.KEY"`

Then update it with `source ~/.bashrc`
