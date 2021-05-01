# Auto-Leaver

This a Senior Sem Project, as such there has been aspects implement as requested by my professor.

## Installation

A requirements.txt file is provided and lists all requirements needed for the project, to install `python -m pip install -r requirements.txt`

## Usage

The project can run by running the module `python /path/to/src` or by running the main file `python /path/to/src/__main__.py`

this will generate an icon that looks like <br>![a photo of mic](icon.svg)

clicking on it will give you a sub-menu which will allow you to start the app to listen to the converstion. Using pydictionary we can generate a list of common key phrases that give an intent to say good-bye. This list is actually tagerted via the term `bye-bye`
```
goodbye
good-by
sayonara
farewell
bye-bye
bye
cheerio
good-bye
good day
word of farewell
adios
so long
au revoir
auf wiedersehen
goodby
arrivederci
adieu
```

saying any of these will force the application to close
