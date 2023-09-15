from entity import Entity
from inputs import genericTextInput, binaryChoiceInput, genericKeyInputs
from components import *
from random import randint

# Process
#   - Let player choose name
#   - Choose Archetype
#   - Construct Player Object out of that information.

def ChooseItems():
    pass

def ChooseWeapon():
    newWeapon = None



    return newWeapon

def createPlayerInventory():
    newInventory = InventoryComponent(
        equipmentSlots=(
          EquipmentSlotComponent(itemSlotType.HEAD),
          EquipmentSlotComponent(itemSlotType.CHEST),
          EquipmentSlotComponent(itemSlotType.ARM),
          EquipmentSlotComponent(itemSlotType.ARM),
          EquipmentSlotComponent(itemSlotType.LEG),
          EquipmentSlotComponent(itemSlotType.LEG),
          EquipmentSlotComponent(itemSlotType.HAND),
          EquipmentSlotComponent(itemSlotType.HAND),
          EquipmentSlotComponent(itemSlotType.FOOT),
          EquipmentSlotComponent(itemSlotType.FOOT),
        ),
        items=ChooseItems(),
        weightCap=100
    )
    return newInventory

def createPlayerStats():
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
    print("What is your name?")
    newName = genericTextInput()
    
    if binaryChoiceInput(question= f"Is {newName} your name?"):
        print("Very Well")
        return newName
    else:
        print("My mistake...")
        return createPlayerName()

def playerCreator():
    newPlayer = Entity()
    newPlayer.tag = UserComponent()
    print("=== CHARACTER CREATION ===")
    newPlayer.name = createPlayerName()
    print("--------- Stats ----------")
    newPlayer.stats = createPlayerStats()
    print("------- Inventory --------")
    newPlayer.inventory = createPlayerInventory()

    return newPlayer


print(playerCreator())

