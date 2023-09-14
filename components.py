from dataclasses import dataclass, field
from enum import Enum
from random import randint

class attackType(Enum):
    PHYSICAL: 0
    ASTRIL: 0
    FIRE: 0
    LIGHTNING: 0

class itemSlotType(Enum):
    HEAD: 0
    ARM: 1
    CHEST: 2
    LEG: 3
    HAND: 4
    FOOT: 5

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
    pass

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