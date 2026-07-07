"""Application config — SECURED version."""

import os

# FIXED: Read sensitive credentials from environment
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "dev_pass")
API_SECRET_KEY = os.environ.get("API_SECRET_KEY", "dev_key")

# FIXED: Restrict CORS origins & disable Debug mode in production environment
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1")
ALLOWED_HOSTS = ["api.example.com"]
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "https://dashboard.example.com"
}
