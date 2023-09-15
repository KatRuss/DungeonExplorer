from dataclasses import dataclass, field
from components import *

# ==============
# == Entities ==
# ==============

@dataclass
class Entity:
    name: str = "Unamed Entity"
    health: HealthComponent = None
    weight: WeightComponent = None
    inventory: InventoryComponent = None
    stats: StatsComponent = None
    tag: object = None
    description: DescriptionComponent = None

@dataclass
class Item(Entity):
    attackComponent: AttackComponent = None
    useComponent: UseComponent = None

class Room:
    name: str = "Unamed Room"
    conncectedRooms: list = field(default_factory=list)
    npcs: list = field(default_factory=list)
    items: list = field(default_factory=list)
    description: DescriptionComponent = None

