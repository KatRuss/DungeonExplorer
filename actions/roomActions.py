from actions.baseActions import Action
from inputs.playerInput import listChoiceInput, pausePlayer
from actions.combatActions import CheckSelfAction

# In this case Activator = player and target = the room itself

class LookAroundAction(Action):
    #TODO: Functionality for looking around and reading all of the descriptive strings in a room object.
    def do(self, activator, target) -> bool:
        return super().do(activator, target)
    
    

class MoveRoomAction(Action):
    def do(self, activator, target) -> bool:
        print("The player has left the room")
        target.playerInRoom = False
        
        #TODO: Add functionality for the player to actually move between rooms

        return True

class PlayerRoomChoiceAction(Action):
    _actionsList = ['Look Around','Check Self','Move Room']
    def do(self, activator, target) -> bool:
        choice = listChoiceInput("What would you like to do?",self._actionsList)
        if choice == 'Look Around':
            action = LookAroundAction()
        elif choice == 'Check Self':
            action = CheckSelfAction()
        elif choice == 'Move Room':
            action = MoveRoomAction()
        return action.do(activator,target)
    
