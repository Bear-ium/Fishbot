from TwitchBotPlus import Bot
from typing import Callable
from pathlib import Path

# Commands
from commands import Hello, Shutdown, forg, wlw

# Config
command_handle = "!"
env_path = Path(__file__).resolve().parent.parent / ".env"

CommandFn = Callable[
    #args, user
    [list[str], str],
    #chat-text, shutdown request
    tuple[str, bool]
]

COMMANDS: dict[str, CommandFn] = {
    # Shutdown Command
    "shutdown": Shutdown,
    
    # Fish Commands
    
    
    # Misc Commands
    "hello": Hello,
    "forg": forg,
    "wlw": wlw
}

# <>------ BOT ------<>
bot = Bot(
    COMMANDS=COMMANDS,
    ENV_Path=env_path,
    HANDLE=command_handle
)
bot.start()