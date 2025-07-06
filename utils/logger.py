import logging

from rich.console import Console
from rich.highlighter import NullHighlighter
from rich.logging import RichHandler

__all__ = ["console", "log"]


class RichLogger:
    def __init__(self, console: Console, level=logging.DEBUG):
        self.console = console
        self.logger = logging.getLogger("insta-automate")
        self.logger.setLevel(level)

        handler = RichHandler(
            console=self.console,
            show_time=False,
            show_level=True,
            show_path=False,
            rich_tracebacks=True,
            markup=True,
            highlighter=NullHighlighter(),
        )
        handler.setFormatter(logging.Formatter("%(message)s"))

        # Avoid adding multiple handlers if reused
        if not self.logger.hasHandlers():
            self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def print(self, *args, **kwargs):
        self.console.print(*args, **kwargs)


console = Console()
log = RichLogger(console)
