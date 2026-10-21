"""A first AI-assisted Flask application for CCT College Dublin Session 1."""

from flask import Flask, render_template_string

# Create the Flask application. __name__ identifies this Python module.
app = Flask(__name__)

# Keep the HTML here so this beginner project needs only one Python file.
HOME_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello from Suzanne</title>
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
</head>
<body>
    <main>
        <div class="label">CCT College Dublin · Session 1</div>
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


# Start the local development server only when this file is run directly.
if __name__ == "__main__":
    app.run()
