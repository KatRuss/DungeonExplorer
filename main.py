from systems.playerCreatorSystem import playerCreator
from entities.room import testRoom, combatRoom
from systems.roomSystem import enterRoom,addRoomConnection

player = playerCreator()
addRoomConnection(testRoom,combatRoom)

enterRoom(player,testRoom)
