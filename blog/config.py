import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/mojabaza'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# TODO: mislim da i ovaj secret key treba izmjeniti i ne smije biti vidljiv na gitu
# TODO: izmjeniti pass u uri i dodati ime
# TODO: https://youtu.be/Wfx4YBzg16s?t=1650 dodati u envronment varijable za bazu.