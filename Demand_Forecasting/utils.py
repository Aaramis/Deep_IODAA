import logging
import sys

from rich import print as rprint

def write_logs(msg, status, echo=False):
    """Print and log messages for reproducibility"""
    levels = {
        "info": ["", ""],
        "debug": ["[blue]", "[/blue]"],
        "warning": ["[dark_orange]", "[/dark_orange]"],
        "critical": ["[red]", "[/red]"]
    }
    if echo:
        rprint(f"o {levels[status][0]}{msg}{levels[status][1]}")

    if status == "info":
        logging.info(msg)

    if status == "debug":
        logging.debug(msg)

    if status == "critical":
        logging.critical(msg)
        if not echo:
            rprint(f"o {levels[status][0]}{msg}{levels[status][1]}")
        sys.exit()

    return