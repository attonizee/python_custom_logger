import os

# =========================
# Logging
# =========================
LOG_DIR = os.getenv("LOG_DIR", "./logs")
LOG_FILE = os.path.join(LOG_DIR, "script.log")