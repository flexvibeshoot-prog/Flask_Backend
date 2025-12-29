import os
from time import time

class Config:
    SECRET_KEY='abc123'

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://47vaDr39q2MWZRN.root:"
        "xypzX71xUJG00aro"
        "@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/"
        "test"
        "?ssl_verify_cert=true"
        "&ssl_verify_identity=true"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    JWT_SECRET_KEY='jwt-secret-string'
    JWT_TOKEN_LOCATION=["headers"]
    JWT_ACCESS_TOKEN_EXPIRES=86400
    JWT_REFRESH_TOKEN_EXPIRES=604800

    # ---------- CLOUDINARY ----------
    CLOUDINARY_CLOUD_NAME = "dr5r2rvkg"
    CLOUDINARY_API_KEY = "177237536613665"
    CLOUDINARY_API_SECRET = "IgdDmXCBP2tf3aexFEMO-Pbrt64"

    # ---------- FLASK MAIL ----------
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "flexvibeshoot@gmail.com"
    MAIL_PASSWORD = "keebynhevuqphfev"
    MAIL_DEFAULT_SENDER = "flexvibeshoot@gmail.com"

    # ---------- GOOGLE OAUTH ----------
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

    GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
    GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

    # MUST match Google Console redirect URI
    OAUTH_REDIRECT_URI = "http://127.0.0.1:5000/auth/google/callback"

    # OAuth scope used in your route
    SCOPE = [
        "openid",
        "email",
        "profile"
    ]

    # CELERY_BROKER_URL="redis://localhost:6379/0"
    # CELERY_RESULT_BACKEND="redis://localhost:6379/0"

    RAZORPAY_KEY_ID='rzp_test_Rr88bizTXEodBQ'
    RAZORPAY_KEY_SECRET='m75HxseUL5BEG3Fa2oJPR98i'

    #celery configuration
    broker_url = "redis://localhost:6379/0"
    result_backend = "redis://localhost:6379/1"
    RATELIMIT_STORAGE_URI = broker_url

    task_default_queue = "default"

    task_queues = {
        "default": {
            "exchange": "default",
            "routing_key": "default",
        },
        "email_queue": {
            "exchange": "email",
            "routing_key": "email.send",
        },
        "heavy_queue": {
            "exchange": "heavy",
            "routing_key": "heavy.process",
        },
    }

    task_routes = {
        "app.tasks.send_mail.send_mail_task": {"queue": "email_queue"},
        "app.tasks.heavy.*": {"queue": "heavy_queue"},
    }

    LOCK_KEY = "search:rebuild:lock"
    LOCK_KEY_INDEXING="search:rebuild:lockindexing"

    GEOLOCATION_URL="https://geocode.maps.co/search"
    GEOLOCATION_API_KEY="695139161fd0e132369546qxg61549e"

    ADMIN_LAT=22.8282019
    ADMIN_LONG=88.3414937
