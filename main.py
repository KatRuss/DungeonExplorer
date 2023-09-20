from systems.playerCreatorSystem import playerCreator
from entities.room import testRoom
from systems.roomSystem import enterRoom

player = playerCreator()
room = testRoom
enterRoom(player,room)
