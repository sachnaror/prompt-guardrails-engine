import logging
from app.config.settings import settings

"""
Central logging configuration for the application.
"""

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("prompt_guardrails_engine")
