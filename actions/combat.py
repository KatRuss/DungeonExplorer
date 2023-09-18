from actions.base import Action
from inputs.playerInput import listChoiceInput
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.entity import Entity
    from actions.base import Action

class AttackAction(Action):
    def do(self, target):
        if isinstance(target,Entity):
            for equipment in self.activator.equipmentSlots:
                for attack in equipment.attackComponents:
                    damage = attack.calculateDamage()
                    print(f"{target.name} Takes {damage} {attack.atype} Damage!")
                    target.health.takeDamage(damage)

# Handle playe input in combat
class PlayerCombatChoice(Action):
    _actionsList = ['Attack']
    def do(self, target):
        choice = listChoiceInput("What would you like to do?",self._actionsList)
        if choice == 'Attack':
            action = AttackAction(target=target)
