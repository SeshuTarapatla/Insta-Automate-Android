from os import environ
from pathlib import Path
from typing import cast

from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.custom.dialog import Dialog
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.types import InputPeerChannel

from utils.logger import log

__all__ = ["telegram"]


class Telegram(TelegramClient):
    def __init__(self) -> None:
        load_dotenv()
        api_id = int(environ.get("TELEGRAM_API_ID", 0))
        api_hash = environ.get("TELEGRAM_API_HASH", "")
        super().__init__("insta-automate", api_id, api_hash)
        self.channel_name = "Insta Automate"
        self.channel_id = int(environ.get("CHANNEL_ID", 0))
        self.channel_hash = int(environ.get("CHANNEL_ACCESS_HASH", 0))
        self.channel = InputPeerChannel(self.channel_id, self.channel_hash)

    def start(self) -> None:
        phone = environ.get("TELEGRAM_NUMBER", "")
        super().start(phone)

    def fetch_channel(self) -> Dialog:
        for dialog in self.iter_dialogs():
            if dialog.name == self.channel_name:
                return dialog
        return cast(Dialog, None)

    def create_channel(self) -> None:
        result = self(
            CreateChannelRequest(
                title="Insta Automate",
                about="Channel created by Insta Automate application.",
                megagroup=False,
            )
        )
        self.channel = result.chats[0]  # type: ignore
        log.info(
            f"Channel create. Please update dotenv with [bold green]CHANNEL_ID={self.channel.id}[/]"
        )
        exit()

    def send_user_img(self, img: Path) -> None:
        self.send_file(
            self.channel,
            file=img.as_posix(),
            caption=f"[@{img.stem}](https://instagram.com/{img.stem})",
            parse_mode="md",
        )  # type: ignore
    
    def backup(self, file: Path) -> None:
        self.send_file(
            "me",
            file=file.as_posix(),
        ) # type: ignore


telegram = Telegram()
