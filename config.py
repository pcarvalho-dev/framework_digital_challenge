import datetime
import os


class Config:
    # Api secret key generating with base64
    SECRET_KEY = os.environ.get('API_SECRET_KEY',
                                'ZnJhbWV3b3JrOmRpZ2l0YWw6Y2hhbGxlbmdl')
