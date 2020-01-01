import string
import random

def randomNameTeam1():
    #TODO
    """
    Returns a random name picked from the Ubuntu releases for team 1
    """
    releases = [
        "Warty Warthogs",
        "Bionic Beavers",
        "Breezy Badgers",
        "Dapper Drakes",
        "Edgy Efts",
        "Feisty Fawns",
        "Gutsy Gibbons",
        "Hardy Herons",
        "Lucid Lynxes",
        "Utopic Unicorns",
        "Disco Dingos",
    ]
    return random.choice(releases)

def randomNameTeam2():
    #TODO
    """
    Returns a random meme as name for team 2
    """
    memes = [
        "Dat Boi",
        "Epstein didn't kill himself",
        "Logan Paul",
        "Petscop 2",
        "Emoji",
        "Rood",
        "Brony",
        "Stonks",
    ]
    return random.choice(memes)

def randomGameName():
    """
    Returns a random name for the game
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(4))