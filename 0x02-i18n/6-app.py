#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """Basic flask app"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Get locale based on the following priority:
    - Locale from URL parameters
    - Locale from user settings
    - Locale from request header
    - Default locale
    """

    # locale from url parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # locale from user pereferences
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users:
        if users[int(user_id)]['locale'] in app.config['LANGUAGES']:
            return users[int(user_id)]['locale']

    # locale from request header
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Return a user dictionary or None"""
    if user_id is None or int(user_id) not in users:
        return None
    return users[int(user_id)]['name']


@app.before_request
def before_request():
    """Get user before request"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)
    print(g.user)


if __name__ == '__main__':
    app.run(debug=True)
