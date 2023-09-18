from typing import List, TYPE_CHECKING
from actions.combat import PlayerCombatChoice

def ChooseItems():
    items = ()
    return items

def ChooseWeapon(weaponList):
    from inputs.playerInput import binaryChoiceInput, listChoiceInput

    newWeapon = listChoiceInput("What weapon would you like?", weaponList)
    newWeapon.printStats()

    if binaryChoiceInput("Would you like this weapon?"):
        return newWeapon
    else:
        print("My mistake...")
        return ChooseWeapon(weaponList)

def createEquipmentSlots():
    from components.inventory import EquipmentSlotComponent
    from data.weapons import testWeaponList
    from components.compEnum import itemSlotType
    
    equipmentSlots:List[EquipmentSlotComponent] = list()
    
    equipmentSlots.append(EquipmentSlotComponent(itemSlotType.WEAPON,ChooseWeapon(testWeaponList)))
    equipmentSlots.append(EquipmentSlotComponent(itemSlotType.ARMOUR))
    
    return equipmentSlots

def createPlayerInventory():
    from components.inventory import InventoryComponent

    newInventory = InventoryComponent(
        items=ChooseItems(),
        weightCap=100
    )
    newInventory.weight = newInventory.calculateWeight()
    return newInventory

def createPlayerStats():
    from components.base import StatsComponent
    from inputs.playerInput import binaryChoiceInput
    
    stats = StatsComponent()
    stats.RollStats()
    print("Current your Stats are:")
    stats.PrintStats()

    if binaryChoiceInput(question= "Would you like to keep these stats?"):
        return stats
    else:
        print("My mistake...")
        return createPlayerStats()

def createPlayerName():
    from inputs.playerInput import genericTextInput, binaryChoiceInput
    
    print("What is your name?")
    newName = genericTextInput()
    
    if binaryChoiceInput(question= f"Is {newName} your name?"):
        print("Very Well")
        return newName
    else:
        print("My mistake...")
        return createPlayerName()

def playerCreator():
    from entities.item import Entity
    from components.tags import UserComponent
    from components.base import CombatComponent,HealthComponent
    
    newPlayer = Entity()
    newPlayer.tag = UserComponent()
    newPlayer.combat = CombatComponent(
        combatActions=[
            PlayerCombatChoice()
        ]
    )
    print("=== CHARACTER CREATION ===")
    newPlayer.name = createPlayerName()
    print("--------- Stats ----------")
    newPlayer.stats = createPlayerStats()
    print("------- Inventory --------")
    newPlayer.inventory = createPlayerInventory()
    newPlayer.equipmentSlots = createEquipmentSlots()
    newPlayer.health = HealthComponent(10+newPlayer.stats.might)

    return newPlayer