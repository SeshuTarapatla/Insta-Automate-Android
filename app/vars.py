from argparse import ArgumentParser, Namespace
from utils.logger import console, log

__all__ = ["args"]


class InstaAutomateNamespace(Namespace):
    """Argparse Namespace for `InstaAutomate`"""

    fnum: int


TITLE = r"""
 _____           _                      _                        _       
|_   _|         | |          /\        | |                      | |      
  | |  _ __  ___| |_ __ _   /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___ 
  | | | '_ \/ __| __/ _` | / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \
 _| |_| | | \__ \ || (_| |/ ____ \ |_| | || (_) | | | | | | (_| | ||  __/
|_____|_| |_|___/\__\__,_/_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|
"""


parser = ArgumentParser(
    prog="Insta-Automate", description="Instagram automation tool set."
)
parser.add_argument(
    "fnum",
    help="Number of accounts to pick in telegram",
    default=10,
    type=int,
    nargs="?",
)


console.clear()
log.print(f"[bold bright_white]{TITLE}[/]")
args, _ = parser.parse_known_args(namespace=InstaAutomateNamespace)
