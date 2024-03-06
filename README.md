# Udacity Project: Motivational Meme Generator

## Overview

The final project for Udacity's Intermediate Python Nanodegree involves creating a Meme Generator. This multimedia application dynamically generates memes by overlaying quotes on images of dogs. The project consists of two main components: a Command-Line Interface (meme.py) and a Flask application (app.py).

## Working Folder Structure
The project's working folder structure is organized as follows:
```bash
|-- _data
    |-- Fonts
    |-- Photoes
    |-- DogQuotes
    |-- SimpleLines
|-- MemeEngine
    |-- meme_engine.py
|-- QuoteEngine
    |-- csv_ingestors.py
    |-- docs_ingestors.py
    |-- pdf_ingestors.py
    |-- text_ingestors.py
    |-- ingestor.py
    |-- ingestor_interface.py
    |-- quote_model.py
|-- static
|-- templates
|-- env
|-- tmp
```

## Working Modules

### QuoteEngine

The `QuoteEngine` module handles the ingestion of various file types (such as .txt, .docx, .pdf, or .csv) containing quotes. It also parses and distinguishes between the quote body and the quote author.

### MemeEngine

The `MemeEngine` module is responsible for loading and manipulating images. It overlays the quote onto the image and can save the resulting meme to the local disk.

# Installation

## Installing Xpdf

Xpdf may not be installed on your local machine. If this is the case, you can install it using the open source XpdfReader utility. Here are some tips for installing xpdf on different operating systems:

For Mac, we suggest that you use Homebrew:
 - If you don't already have it, install use the command provided here to install Homebrew. After installing, read the last few lines that it outputs in your CLI it may provide additional commands that you can run to add Homebrew to PATH.
 - Once Homebrew is installed, simply run `brew install xpdf` in the terminal.

 For Windows, you'll need to:
 - Download the Windows command-line tools from the xpdf website.
 - Unzip the files in a location of your choice.
 - Get the full file path to the folder named `bin32` (if you have a 32-bit machine) or `bin64` (if you have a 64-bit machine).
 - Add this path to the `Path` environment variable. This will allow you to use the xpdf command from the command line. If you've never done this before, check out this Stack Overflow post on how to add a folder to the **`Path`** environment variable.

For Linux, you can use Homebrew (as shown above for Mac) or `apt-get` to install (simply enter `sudo apt-get install -y xpdf` in your command line interface).

## Installing Python Dependencies

```bash
pip install -r requirements.txt
```
## Check compatibility with PEP 257 Docstring Conventions 

```bash
pydocstyle --match='.*\\.py' --match-dir='^(?!env).*' .
```
## Check compatibility with PEP 8 code style Conventions 

```bash
pycodestyle --exclude=env --statistics .
```

### or run the lint.bat for `windows` make lint for `linux` 

```bash
lint.bat
make lint
```
# Running the project

## Command-Line Interface

```bash
python meme.py -h       
usage: MemeGenerator [-h] [-p PATH] [-b BODY] [-a AUTHOR]

Dog meme generator with fun quotes.

usage: MemeGenerator [-h] [-a AUTHOR] [-p PATH] [-b BODY]

let's get some Dog memes with fun quotes.

options:
  -h, --help  show this help message and exit
  -a AUTHOR, --author AUTHOR Quote author to add to the image
  -p PATH, --path PATH  Path to image file
  -b BODY, --body BODY  Quote body to add to the image
```
## Flask Application

```bash
python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open `http://127.0.0.1:5000` in a browser to interface with web app.
