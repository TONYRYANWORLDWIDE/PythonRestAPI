class Config:

    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tonyryan:prolong-vivacity-asbestos@localhost/smilecook'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tonyryan:!Lsv%wbb962QT@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
    # JWT_ACCESS_TOKEN_EXPIRES = False #For Dev