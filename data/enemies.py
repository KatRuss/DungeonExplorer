from entities.entity import Entity
from components.base import HealthComponent,StatsComponent,CombatComponent
from components.inventory import EquipmentSlotComponent, itemSlotType
from components.tags import EnemyComponent
from data.weapons import Longsword

Goblin = Entity(
    name= "Goblin",
    health=HealthComponent(12),
    stats=StatsComponent(dex=2),
    combat=CombatComponent(),
    equipmentSlots=EquipmentSlotComponent(itemSlotType.WEAPON,Longsword),
    tag=EnemyComponent()
)