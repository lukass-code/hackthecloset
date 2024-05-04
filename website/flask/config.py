class Config:
    """Set Flask config variables."""

    FLASK_APP = 'wsgi.py'  
    FLASK_ENV = 'development'
    TESTING = False
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = "NWjSSiPz9R39mX8YOZEz"

    STATIC_FOLDER = 'static'
