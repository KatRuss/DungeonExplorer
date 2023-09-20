from dataclasses import dataclass, field
from components.baseComponents import StatsComponent, HealthComponent, WeightComponent, DescriptionComponent, CombatComponent
from components.inventoryComponents import EquipmentSlotComponent, InventoryComponent
from typing import List
from formatting.textFormat import printTitle,printSubTitle,printListEntry
from components.tagsComponents import UserComponent

@dataclass
class Entity:
    name: str = "Unamed Entity"
    location: object = None
    health: HealthComponent = None
    weight: WeightComponent = None
    equipmentSlots: List[EquipmentSlotComponent] = field(default_factory=list)
    inventory: InventoryComponent = None
    stats: StatsComponent = None
    tag: object = None
    descriptionComp: DescriptionComponent = None
    combat : CombatComponent = None
    
    def EnterRoom(self, room):
        self.location = room
    
    def calculateDefense(self):
        result = 0
        for item in self.equipmentSlots:
            if item.equipment != None and item.equipment.defenseComponents != []:
                for defense in item.equipment.defenseComponents:
                    result += defense.amount
        return result
    
    def PrintStats(self):
        #TODO: Make a generic PrintStats entity function
        printTitle(self.name)
        
        if self.health != None:
            printSubTitle("Health")
            printListEntry(f"HP: {self.health.value}/{self.health.maxHP}")
            printListEntry(f"{self.name} is {'Dead' if self.health.isDead else 'not Dead'}")
        
        if self.weight != None:
            printSubTitle("Weight")
            printListEntry(f"Weight: {self.weight.weight}")
            
        if self.equipmentSlots != []:
            printSubTitle("Equipent")
            print(f"{self.name} appears to be equiped with: ")
            for equipentSlot in self.equipmentSlots:
                if equipentSlot.equipment != None:
                    printListEntry(equipentSlot.equipment)
        
        if self.descriptionComp != None:
            printSubTitle("Description")
            print(self.descriptionComp.value)
    
