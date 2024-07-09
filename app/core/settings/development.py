"""Local settings module."""
import os
from .base import Base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Base):
    """Local settings"""
    DEBUG = True
    # Set up testing settings
    INSTALLED_APPS = Base.INSTALLED_APPS

    CORS_ORIGIN_WHITELIST = [
        "http://localhost:3000"
    ]
