from systems.combatSystem import initCombat
from components.tagsComponents import UserComponent
from formatting.textFormat import printTitle, printSubTitle, printLine
from inputs.playerInput import pausePlayer
from actions.roomActions import PlayerRoomChoiceAction

def enterRoom(target, room):
    target.location = room

    if isinstance(target.tag,UserComponent):
        # -- PASTE DESCRIPTION --
        printRoomEntry(room)
        pausePlayer()

        # -- COMBAT CHECK --
        target.location.playerInRoom = True
        enemy = checkRoomForEnemies(room)
        if enemy != None:
            initCombat(target,enemy)

        # -- ROOM ACTIONS UPDATE --
        roomLoop(target,room)



def roomLoop(player, room):
    
    # Process
    #   
    #   - while the player hasn't left the room: 
    #       - allow player to perform actions in the room
    #       - Including:
    #           - Checking themselves
    #           - Looking around for items
    #           - Moving between different rooms
    #           - Saving the game perhaps
    
    #- Give player the initial description of the room (post combat perhaps)
    printRoomIntroduction(room)
    pausePlayer()
    roomAction = PlayerRoomChoiceAction()
    movedRoom = False
    while movedRoom == False:
        movedRoom = PlayerRoomChoiceAction().do(activator=player,target=room)

def assignNPCsToRoom(room):
    for npc in room.npcs:
        npc.location = room

def checkRoomForEnemies(room):
    if room.playerInRoom and room.enemy != None:
        return room.enemy
    else:
        return False
    
# For entering the room for the first time (before combat)
def printRoomEntry(room):
    printTitle(room.name)
    if room.descriptionComp != None:
        printSubTitle("Description")
        print(room.descriptionComp.value)
    printLine()

# For entering the room after the first time (or after combat)
def printRoomIntroduction(room):
    printTitle(room.name)
    if room.roomIntro != " ":
        print(room.roomIntro)