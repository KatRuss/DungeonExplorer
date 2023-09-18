# For running the combat
from random import randint
from typing import List,TYPE_CHECKING
from entities.entity import Entity

def getTurnOrder(entities: List[Entity]):
    for entity in entities:
        entity.combat.initiative = randint(1,20)+entity.stats.dex
    return sorted(entities,key=lambda entity: entity.combat.initiative)
    

def initCombat(player: Entity, enemy: Entity):
    combatEnded = False
    turnOrder = getTurnOrder([player,enemy])
    
    for entity in turnOrder:
        print(f"{entity.name}: {entity.combat.initiative}")
    
    # while combatEnded == False:
    #     for entity in turnOrder:
    #         entity.combat.doCombatAction()
