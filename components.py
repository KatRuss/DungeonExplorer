from dataclasses import dataclass, field
from enum import Enum
from random import randint

class attackType(Enum):
    PHYSICAL = 0
    ASTRIL = 1
    FIRE = 2
    LIGHTNING = 3

class itemSlotType(Enum):
    HEAD = 0
    ARM = 1
    CHEST = 2
    LEG = 3
    HAND = 4
    FOOT = 5

# Represents a kind of die. e.g. sides = 6 means a standard six-sided die.
@dataclass
class dieType():
    sides: int
    
    def RollDie(self):
        return randint(1,self.sides)

# ================
# == COMPONENTS ==
# ================

@dataclass
class StatsComponent:
    might: int = 0
    mind: int = 0
    dex: int = 0
    cha: int = 0

    def RollStats(self):
        self.might = randint(1,6) + randint(1,6)
        self.mind = randint(1,6) + randint(1,6)
        self.dex = randint(1,6) + randint(1,6)
        self.cha = randint(1,6) + randint(1,6)
    
    def PrintStats(self):
        print(f"Might: {self.might}")
        print(f"Mind: {self.mind}")
        print(f"Dexterity: {self.dex}")
        print(f"Charisma: {self.cha}")
    
@dataclass
class WeightComponent:
    weight: float = 0

@dataclass
class DefenseComponent:
    defType: attackType = attackType.PHYSICAL
    amount: float = 0

@dataclass
class EquipmentSlotComponent:
    validSlotType: itemSlotType = None
    equipment: object = None

@dataclass
class InventoryComponent:
    equipmentSlots: list = field(default_factory=list)
    items: list = field(default_factory=list)
    weightCap: float = 100
    
    def __post_init__(self):
        self.weight = 0

    def calculateWeight(self):
        result = 0
        for slot in self.equipmentSlots:
            if not slot.equipment == None:
                result += slot.equipment.weight.weight
        for item in self.items:
            if not item.weight == None:
                result += item.weight.weight
        return result

class LockComponent:
    pass

class ContainerComponent:
    pass

@dataclass
class HealthComponent:
    maxHP: int = 1
    
    def __post_init__(self):
        self.isDead = False

@dataclass
class UserComponent:
    pass

@dataclass
class EnemyComponent:
    pass

@dataclass
class DescriptionComponent:
    string: str

@dataclass
class AttackComponent:
    pass

@dataclass
class CombatComponent:
    pass

@dataclass
class UseComponent:
    pass

@dataclass
class RoomConnectionComponent:
    pass