# Hello from Suzanne

A small, single-file Python and Flask application for Session 1 of the CCT
College Dublin Certificate in Low-Code, No-Code & AI-Assisted Application
Development. It demonstrates how AI can help create a first web application.
The home page displays a welcome message and the heading “Hello from Suzanne”.

## Requirements

Install Python 3.8 or newer. Flask is pinned to version 3.0.3.
Run the commands below from the existing `sbam26642-lowcode-project` folder.

## Create and activate a virtual environment

A virtual environment keeps this project's Python packages separate from other
projects. Create it once, then activate it whenever you open a new terminal.

### Windows (Git Bash)

```bash
py -m venv .venv
source .venv/Scripts/activate
```

If the `py` launcher is unavailable, use `python -m venv .venv` instead.

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies and run

With the virtual environment active, install the required packages:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open **http://127.0.0.1:5000/** in your browser to see the welcome page.
The server runs locally for development. Stop it with **Ctrl+C**.
Run `deactivate` when you have finished using the virtual environment.

## Project files

- `app.py`: Flask application, GET `/` route, HTML and page styling, with comments.
- `requirements.txt`: Pins Flask to version 3.0.3; pip installs its dependencies.
- `.gitignore`: Excludes the virtual environment, Python cache files, local
  environment settings and macOS metadata from version control.
- `README.md`: Describes the project and explains how to set it up and run it.
