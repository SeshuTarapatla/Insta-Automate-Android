from app.telegram.methods.follow import Follow
from utils.logger import log


def follow() -> None:
    """Action: FOLLOW -> Pick random N account to follow."""
    log.info("Action: [bold yellow]FOLLOW[/]\n")
    entity = Follow()
    entity.start()