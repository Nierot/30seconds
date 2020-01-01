import string
import random

def randomNameTeam1():
    #TODO
    """
    Returns a random name picked from the Ubuntu releases for team 1, Debian for team 2
    """
    return "Bionic Beaver"

def randomNameTeam2():
    #TODO
    """
    Returns a random name picked from the Ubuntu releases for team 1, Debian for team 2
    """
    return "Buster"

def randomGameName():
    """
    Returns a random name for the game
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(4))