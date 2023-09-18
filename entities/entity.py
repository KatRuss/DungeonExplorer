from dataclasses import dataclass, field
from components.base import StatsComponent, HealthComponent, WeightComponent, DescriptionComponent, CombatComponent
from components.inventory import EquipmentSlotComponent, InventoryComponent
from typing import List

@dataclass
class Entity:
    name: str = "Unamed Entity"
    health: HealthComponent = None
    weight: WeightComponent = None
    equipmentSlots: List[EquipmentSlotComponent] = field(default_factory=list)
    inventory: InventoryComponent = None
    stats: StatsComponent = None
    tag: object = None
    descriptionComp: DescriptionComponent = None
    combat : CombatComponent = None
    
    def PrintStats(self):
        pass
    
    # def __str__(self) -> str:
    #     return self.name