from slowapi import Limiter
from slowapi.util import get_remote_address
from app.config.settings import settings

"""
Rate limiter for FastAPI.
Limits how many requests a client can send.
Example: 10 requests per minute.
"""

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[f"{settings.RATE_LIMIT_PER_MINUTE}/minute"]
)
