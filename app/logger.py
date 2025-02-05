import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Define log format
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s"

# Create logger
logger = logging.getLogger("ai_news_agent")
logger.setLevel(logging.INFO)  # Default log level

# Create rotating file handler (limits file size to 5MB, keeps 5 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Create console handler for real-time logs
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("✅ Logger initialized successfully.")
