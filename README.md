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

- `app.py`: Flask application, homepage, about page and contact form, with
  inline HTML, shared styling and explanatory comments.
- `requirements.txt`: Pins Flask to version 3.0.3; pip installs its dependencies.
- `.gitignore`: Excludes the virtual environment, Python cache files, local
  environment settings and macOS metadata from version control.
- `README.md`: Describes the project and explains how to set it up and run it.

## Contact form

With the server running, visit **http://127.0.0.1:5000/contact**. Navigation links
connect the homepage, the existing `/about` project vision and the contact form.

The contact route supports GET (show the form) and POST (validate submission).
Name, email and message are required. Python rejects empty or whitespace-only
names and messages. Email addresses must have a reasonable format, including
an `@` and a domain such as `example.com`; this does not verify mailbox existence.
Surrounding whitespace is ignored when validating.

Invalid submissions return HTTP **422**, display errors next to the relevant
fields and preserve the original entries. The form uses `novalidate` so you can
see the server-side validation directly in your browser. User input is rendered
with Jinja's automatic HTML escaping.

A valid submission returns a confirmation thanking the user by name, with links
to the homepage and contact form. This is a demonstration: no email is sent and
no submitted information is saved to a database, file or session. Reloading a
confirmation may prompt the browser to resubmit the form.

### Manual test checklist

Start the application using the setup and run instructions above, then check:

- [ ] `/` still shows the original welcome heading and message.
- [ ] `/about` still shows the Delivery Driver Management App project vision.
- [ ] Navigation links work between all three pages.
- [ ] GET `/contact` shows an empty form with Name, Email, Message and Submit.
- [ ] Submit `Suzanne`, `suzanne@example.com` and `Hello!`: the confirmation
  thanks Suzanne and provides working return links.
- [ ] Submit `invalid`, `name@` or `name@example` as the email: an email error
  appears and the other entries remain in the form.
- [ ] Submit all fields blank: all three fields show errors.
- [ ] Submit only spaces in each field: all three fields show errors.
- [ ] Leave just the name or message blank: the correct field shows an error.
- [ ] Submit `<script>alert(1)</script>` as the name with otherwise valid input:
  the confirmation displays it as text, without executing it.
- [ ] In browser developer tools, check Network: invalid POST requests return
  422, while valid POST requests return 200.

Flask remains pinned to `3.0.3`; the form requires no additional packages.

## Project Idea - What Would I Build If It Took an Evening Instead of a Quarter?


If I could build an application in one evening instead of three months, I would develop a Delivery Driver Management App designed to simplify scheduling and daily deliveries.

The application would have two connected components: a Driver Scheduler and a Delivery Driver Helper.

The Scheduler would allow drivers to submit their availability and preferred locations. If a driver couldn't work an assigned shift, they could release it to a queue of available drivers, with the manager approving the replacement.

The Delivery Helper would use AI-powered document scanning to extract customer addresses, Eircodes and phone numbers from delivery dockets. Drivers could open destinations in Google Maps, Apple Maps or Waze, track completed deliveries and automatically calculate paid and outstanding delivery fees.

Using low-code tools and AI-assisted development, I could rapidly create a functional prototype, reduce administrative work and improve efficiency for both drivers and management.
