from entities.entity import Entity
from entities.item import Item
from components.baseComponents import DescriptionComponent
from components.roomsComponents import RoomConnectionComponent
from components.tagsComponents import EnemyComponent
from dataclasses import dataclass,field
from data.enemies import Goblin
from typing import List
@dataclass
class Room(Entity):
    items: List[Item] = field(default_factory=list)
    npcs: List[Entity] = field(default_factory=list)
    connectedRooms: List[RoomConnectionComponent] = field(default_factory=list)

    def __post_init__(self):
        self.playerInRoom = False

    def assignNPCsToRoom(self):
        for npc in self.npcs:
            npc.location = self

    def checkRoomForEnemies(self):
        enemyList = []
        if self.playerInRoom:
            for npc in self.npcs:
                if npc.tag == EnemyComponent():
                    enemyList.append(npc)
            return enemyList
        else:
            return False

testRoom = Room(
    name="Test Room",
    npcs=[Goblin],
    descriptionComp=DescriptionComponent("This is a cool looking test room.")
)