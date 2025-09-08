# Configuration settings for the Flask application

import os
from dotenv import load_dotenv
from utils.env_loader import load_env
load_env()
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
    TESTING = os.environ.get('TESTING', 'False').lower() in ['true', '1']
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'mssql+pymssql://sa:Aa%40123456@127.0.0.1:1433/FlaskApiDB'
    CORS_HEADERS = 'Content-Type'
    GEMINI_URL = os.environ.get('GEMINI_URL')
    GEMINI_KEY = os.environ.get('GEMINI_KEY')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'mssql+pymssql://sa:Aa%40123456@127.0.0.1:1433/FlaskApiDB'


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'mssql+pymssql://sa:Aa%40123456@127.0.0.1:1433/FlaskApiDB'


class ProductionConfig(Config):
    """Production configuration."""
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'mssql+pymssql://sa:Aa%40123456@127.0.0.1:1433/FlaskApiDB'

    
template = {
    "swagger": "2.0",
    "info": {
        "title": "Todo API",
        "description": "API for managing todos",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}
class SwaggerConfig:
    """Swagger configuration."""
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Todo API",
            "description": "API for managing todos",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ],
        "consumes": [
            "application/json"
        ],
        "produces": [
            "application/json"
        ]
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs"
    }