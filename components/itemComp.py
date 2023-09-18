#FOR ATTACK, DEFENSE, USE
from dataclasses import dataclass, field
from components.compEnum import attackType, dieType

@dataclass
class AttackComponent:
    dice: dieType = dieType(4)
    diceNum: int = 1
    atype : attackType = attackType.PHYSICAL
    flatDamage: int = 0
    
    def calculateDamage(self):
        result = 0
        for x in range(0,self.diceNum):
            result + self.dice.RollDie()
        return result + self.flatDamage
    
@dataclass
class UseComponent:
    pass

@dataclass
class DefenseComponent:
    defType: attackType = attackType.PHYSICAL
    amount: float = 0