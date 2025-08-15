def Shutdown(args: list[str], user: str) -> tuple[str, bool]:
    if user == "majojobears" or user == "theactualevie" or user == "danmanplayz":
        return (f"Goodbye {user} & chat!",True)
    else:
        return ("",False)