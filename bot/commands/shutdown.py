import os

from .modules import Webhook
from dotenv import load_dotenv
from typing import cast

load_dotenv()

webhook_url = cast(str, os.getenv("WEBHOOK_URL"))

wbhook = Webhook(
    url=webhook_url,
    default_username="Fish Bot V2"
)

def Shutdown(args: list[str], user: str) -> tuple[str, bool]:
    if user == "majojobears" or user == "theactualevie" or user == "danmanplayz":
        wbhook.send_message(content=f"{user} has shutdown the bot!")
        return (f"Goodbye {user} & chat!",True)
    else:
        return ("",False)