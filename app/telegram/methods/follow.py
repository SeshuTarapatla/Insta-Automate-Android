from random import randint
from app.misc import timestamp
from app.telegram import telegram
from app.vars import args
from utils.logger import log


class Follow:
    def __init__(self) -> None:
        self.client = telegram
        self.channel = telegram.channel
    
    def fetch_total(self) -> None:
        self.total = self.client.get_messages(self.channel, limit=0).total - 1  # type: ignore
        log.info(f"Total profiles: [bold magenta]{self.total}[/]")
        log.info(f"Random profiles to pick: [bold cyan]{args.fnum}[/]\n")
    
    def start(self) -> None:
        # Fetch total
        self.client.start()
        self.fetch_total()
        # Send random n profiles
        self.count = 0
        log.info("--- Random Profiles Started ---")
        banner = f"Batch Follow ({args.fnum}): [gray85 italic]{timestamp()}[/]"
        self.client.send_message(self.channel, banner)  # type: ignore
        log.info(banner)
        while self.count < args.fnum:
            self.resend()
            self.count += 1
        log.print()
        log.info("--- Random Profiles Completed ---" + "\n")

    def resend(self) -> None:
        index = randint(0, self.total)
        rel_index = self.total - index
        message = self.client.get_messages(self.channel, limit=1, add_offset=index)[0]  # type: ignore
        account = str(message.message).removeprefix("@")
        timestamp = message.date.strftime("%Y:%m:%d")
        log.info(f"{str(self.count + 1).rjust(2)}. [cyan]{account}[/] : Message([bold red]{rel_index}[/], [blue]{timestamp}[/])")
        self.client.send_file(
            self.channel, file=message.photo, caption=message.text, parse_mode="md"
        )  # type: ignore
        self.client.delete_messages(self.channel, [message.id])  # type: ignore
