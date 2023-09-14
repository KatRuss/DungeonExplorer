from dataclasses import dataclass
from components import *

@dataclass
class Entity:
    name: str = "Unamed Entity"
    health: HealthComponent = None
    weight: WeightComponent = None
    inventory: InventoryComponent = None
    stats: StatsComponent = None
    tagComponent: object = None

@dataclass
class Item(Entity):
    attackComponent: AttackComponent = None
    useComponent: UseComponent = None
