import os

from .base import *  # noqa

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "[::1]",
    "srv29.mikr.us",
    "geodoc.toadres.pl",
]

DATABASES = {
    "default": {
        "ENGINE": os.environ["DB_ENGINE"],
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}

TEST_HOST = f"http://localhost:{os.environ['IP4_PORT']}"
CSRF_TRUSTED_ORIGINS = [
    os.environ["HOST_NAME"],
    TEST_HOST,
    "http://127.0.0.1:8000",
    "http://srv29.mikr.us",
    "http://geodoc.toadres.pl",
    "http://srv29.mikr.us:20158",
]

MEDIA_URL = os.environ["HOST_NAME"] + "/media/"

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
ADMIN_PASS = os.environ.get("ADMIN_PASS")
