from systems.playerCreatorSystem import playerCreator
from entities.room import testRoom

player = playerCreator()
room = testRoom
player.EnterRoom(room)
