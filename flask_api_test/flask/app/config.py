
class Config:
    POSTGRES_config = {
        "user":"test",
        "password":"test",
        "host":"postgresql-container",
        "port":5432,
        "db":"demo"
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s'% POSTGRES_config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    CORS_HEADERS = 'Content-Type'