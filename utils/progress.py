def progress_bar(p):
    filled = int(p*10)
    return "▰"*filled + "▱"*(10-filled)