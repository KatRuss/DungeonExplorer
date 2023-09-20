from systems.combatSystem import initCombat
from components.tagsComponents import UserComponent
from formatting.textFormat import printTitle, printSubTitle, printLine
from inputs.playerInput import pausePlayer

def enterRoom(target, room):
    target.location = room
    # -- PASTE DESCRIPTION
    printRoomEntry(room)
    pausePlayer()
    # -- COMBAT CHECK --
    if isinstance(target.tag,UserComponent):
        target.location.playerInRoom = True
        enemy = checkRoomForEnemies(room)
        if enemy != None:
            initCombat(target,enemy)

def assignNPCsToRoom(room):
    for npc in room.npcs:
        npc.location = room

def checkRoomForEnemies(room):
    if room.playerInRoom and room.enemy != None:
        return room.enemy
    else:
        return False
    
def printRoomEntry(room):
    printTitle(room.name)
    if room.descriptionComp != None:
        printSubTitle("Description")
        print(room.descriptionComp.value)
    printLine()