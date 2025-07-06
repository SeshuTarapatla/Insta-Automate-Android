from datetime import datetime


def timestamp() -> datetime:
    """Timestamp wrapper with microseconds removed."""
    return datetime.now().replace(microsecond=0)