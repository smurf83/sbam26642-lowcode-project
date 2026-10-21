"""A first AI-assisted Flask application for CCT College Dublin Session 1."""

import re

from flask import Flask, render_template_string, request

# Create the Flask application. __name__ identifies this Python module.
app = Flask(__name__)

# Shared CSS keeps the welcome and contact pages visually consistent.
PAGE_STYLE = """
    <style>
        body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            background: #eef2ff;
            color: #243047;
            font-family: system-ui, sans-serif;
            line-height: 1.6;
        }
        main {
            width: min(36rem, 85%);
            box-sizing: border-box;
            margin: 2rem 0;
            padding: clamp(1.5rem, 5vw, 3rem);
            background: white;
            border-top: 6px solid #6356c9;
            border-radius: 1rem;
            box-shadow: 0 12px 36px #24304712;
        }
        h1 { margin-top: 0; line-height: 1.2; color: #493a9e; }
        p { margin-bottom: 0; }
        .label { font-size: 0.85rem; color: #58647a; margin-bottom: 1rem; }
    </style>
"""

# Keep the HTML here so this beginner project needs only one Python file.
HOME_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello from Suzanne</title>
""" + PAGE_STYLE + """
</head>
<body>
    <main>
        <div class="label">CCT College Dublin · Session 1</div>
        <nav aria-label="Main navigation">
            <a href="/">Home</a> · <a href="/about">About</a> ·
            <a href="/contact">Contact</a>
        </nav>
        <h1>Hello from Suzanne</h1>
        <p>Welcome to my first AI-assisted Flask project! I am learning to
        build web applications with Python, Flask and a little help from AI.</p>
    </main>
</body>
</html>
"""


# A route connects a URL to a function. This function handles GET requests to /.
@app.get("/")
def home() -> str:
    """Render the welcome page."""
    return render_template_string(HOME_PAGE)


@app.route("/about")
def about():
    """Display the Delivery Driver App project vision."""
    return """
    <html>
        <head>
            <title>About My Project</title>
        </head>
        <body>
            <h1>What Would I Build If It Took an Evening
            Instead of a Quarter?</h1>

            <h2>Delivery Driver Management App</h2>

            <p>
            If I could build an application in one evening
            instead of three months, I would develop a
            Delivery Driver Management App designed to
            simplify scheduling and daily deliveries.
            </p>

            <p>
            The application would have two connected
            components: a Driver Scheduler and a
            Delivery Driver Helper.
            </p>

            <p>
            The Scheduler would allow drivers to submit
            their availability and preferred locations.
            If a driver couldn't work an assigned shift,
            they could release it to a queue of available
            drivers, with the manager approving the
            replacement.
            </p>

            <p>
            The Delivery Helper would use AI-powered
            document scanning to extract customer addresses,
            Eircodes and phone numbers from delivery dockets.
            Drivers could open destinations in Google Maps,
            Apple Maps or Waze, track completed deliveries
            and automatically calculate paid and outstanding
            delivery fees.
            </p>

            <p>
            Using low-code tools and AI-assisted development,
            I could rapidly create a functional prototype,
            reduce administrative work and improve efficiency
            for both drivers and management.
            </p>

            <nav aria-label="Main navigation">
                <a href="/">Back to Home</a> · <a href="/about">About</a> ·
                <a href="/contact">Contact</a>
            </nav>
        </body>
    </html>
    """

# Reuse the homepage styling while keeping all templates in this Python file.
CONTACT_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Contact Suzanne</title>
""" + PAGE_STYLE + """
    <style>
        nav { margin-bottom: 1.5rem; }
        a { color: #493a9e; }
        label { display: block; font-weight: 600; margin-top: 1rem; }
        input, textarea {
            box-sizing: border-box; width: 100%; padding: 0.7rem;
            border: 1px solid #58647a; border-radius: 0.4rem; font: inherit;
        }
        textarea { resize: vertical; }
        [aria-invalid="true"] { border: 2px solid #a51d32; }
        .error { color: #a51d32; margin: 0.25rem 0; }
        button {
            margin-top: 1.5rem; padding: 0.7rem 1.4rem; background: #493a9e;
            color: white; border: 0; border-radius: 0.4rem; font: inherit;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <main>
        <nav aria-label="Main navigation">
            <a href="{{ url_for('home') }}">Home</a> ·
            <a href="{{ url_for('about') }}">About</a> ·
            <a href="{{ url_for('contact') }}">Contact</a>
        </nav>
        {% if confirmed %}
            <h1>Thank you, {{ name }}!</h1>
            <p>Your form passed validation. This demonstration does not save
            your information or send an email.</p>
            <p><a href="{{ url_for('home') }}">Back to homepage</a> ·
            <a href="{{ url_for('contact') }}">Back to contact form</a></p>
        {% else %}
            <h1>Contact Suzanne</h1>
            <p>All fields are required. This is a practice form; information
            is not saved and no email is sent.</p>
            {% if errors %}
                <p class="error" role="alert">Please correct the fields below.</p>
            {% endif %}
            <form method="post" action="{{ url_for('contact') }}" novalidate>
                {% for field, label in [('name', 'Name'), ('email', 'Email'),
                                         ('message', 'Message')] %}
                    <label for="{{ field }}">{{ label }}</label>
                    {% if field == 'message' %}
                        <textarea id="{{ field }}" name="{{ field }}" rows="5"
                    {% else %}
                        <input id="{{ field }}" name="{{ field }}"
                            type="{{ 'email' if field == 'email' else 'text' }}"
                            value="{{ values[field] }}"
                    {% endif %}
                        required aria-invalid="{{ 'true' if field in errors else 'false' }}"
                        {% if field in errors %}aria-describedby="{{ field }}-error"{% endif %}
                    >{% if field == 'message' %}{{ values[field] }}</textarea>{% endif %}
                    {% if field in errors %}
                        <p class="error" id="{{ field }}-error">{{ errors[field] }}</p>
                    {% endif %}
                {% endfor %}
                <button type="submit">Submit</button>
            </form>
        {% endif %}
    </main>
</body>
</html>
"""

# A practical format check, rather than a check that the mailbox exists.
EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}"
)


@app.route("/contact", methods=["GET", "POST"])
def contact() -> tuple[str, int]:
    """Validate a contact form without retaining or sending its contents."""
    values = {field: "" for field in ("name", "email", "message")}
    errors = {}
    if request.method == "POST":
        # Keep original values for redisplay; strip only for validation/use.
        values = {field: request.form.get(field, "") for field in values}
        if not values["name"].strip():
            errors["name"] = "Please enter your name."
        email = values["email"].strip()
        if not EMAIL_PATTERN.fullmatch(email) or len(email) > 254:
            errors["email"] = "Please enter a valid email address, such as name@example.com."
        if not values["message"].strip():
            errors["message"] = "Please enter a message."
        if not errors:
            # Jinja automatically escapes user values in render_template_string.
            return render_template_string(
                CONTACT_PAGE, confirmed=True, name=values["name"].strip()
            ), 200

    # 422 indicates that a submitted form contains invalid field values.
    return render_template_string(
        CONTACT_PAGE, confirmed=False, values=values, errors=errors
    ), 422 if errors else 200


# Start the local development server only when this file is run directly.
if __name__ == "__main__":
    app.run()
