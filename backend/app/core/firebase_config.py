import os
import toml
import pyrebase
import firebase_admin

from firebase_admin import credentials, firestore
from pathlib import Path

# Load secrets from .streamlit/secrets.toml (works without Streamlit runtime)
_secrets = None

def _load_secrets():
    global _secrets
    if _secrets is not None:
        return _secrets

    # Look for secrets.toml in multiple locations
    candidates = [
        Path(__file__).resolve().parents[3] / ".streamlit" / "secrets.toml",  # chatbot-page/.streamlit/
        Path(__file__).resolve().parents[4] / ".streamlit" / "secrets.toml",
        Path.cwd() / ".streamlit" / "secrets.toml",
    ]

    for path in candidates:
        if path.exists():
            _secrets = toml.load(path)
            return _secrets

    raise FileNotFoundError(
        f"Could not find .streamlit/secrets.toml. Searched: {[str(p) for p in candidates]}"
    )

def get_pyrebase_auth():
    secrets = _load_secrets()
    firebase_cfg = dict(secrets["firebase_client"])
    firebase_app = pyrebase.initialize_app(firebase_cfg)
    return firebase_app.auth()

def init_firebase_admin():
    if not firebase_admin._apps:
        secrets = _load_secrets()
        cred_dict = dict(secrets["firebase_admin"])
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)

def get_firestore():
    init_firebase_admin()
    return firestore.client()

def get_google_oauth_config():
    """Return Google OAuth configuration from secrets."""
    secrets = _load_secrets()
    return dict(secrets["google_oauth"])