#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import pytz
from typing import Union
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Basic flask app"""
    return render_template('index.html')


def is_valid_tz(time_zone) -> bool:
    """Check if timezone is valid"""
    try:
        pytz.timezone(time_zone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


@babel.timezoneselector
def get_timezone() -> Union[str, None]:
    """Get timezone based on the following priority:
    - Timezone from URL parameters
    - Timezone from user settings
    - Default timezone (UTC)
    """
    # Timezone from URL parameters
    time_zone = request.args.get('timezone')
    if time_zone and is_valid_tz(time_zone):
        # print(time_zone)
        return time_zone

    # Timezone from user settings
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        time_zone = users[int(user_id)]['timezone']
        if time_zone and is_valid_tz(time_zone):
            # print(time_zone)
            return time_zone

    # Default to BABEL_DEFAULT_TIMEZONE if none found or invalid
    return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale() -> str:
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


def get_user(user_id: Union[str, None]) -> Union[str, None]:
    """Return a user dictionary or None"""
    if user_id is None or int(user_id) not in users:
        return None
    return users[int(user_id)]['name']


def get_current_time():
    """Get current time in the inferred timezone"""
    current_timezone = pytz.timezone(get_timezone())
    current_time = datetime.now(current_timezone)
    return current_time.strftime('%b %d, %Y, %I:%M:%S %p')


@app.before_request
def before_request() -> None:
    """Get user before request"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)
    g.timezone = get_current_time()
    # print(g.user)


if __name__ == '__main__':
    app.run(debug=True)
