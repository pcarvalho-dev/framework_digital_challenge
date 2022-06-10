import datetime
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


class Config:
    # Base64 secret key to auth
    SECRET_KEY = os.environ.get('API_SECRET_KEY')

    # Keep order of dictionary passed to jsonify
    JSON_SORT_KEYS = False

    # JWT token config
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRES = 3600
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=3600)

    # SQLAlchemy connect config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 0
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4".format(
        os.environ.get("DB_USER"),
        os.environ.get("DB_PASS"),
        os.environ.get("DB_HOST"),
        os.environ.get("DB_NAME")
    )
    SQLALCHEMY_BINDS = {
        'slave': SQLALCHEMY_DATABASE_URI
    }
