from entities.entity import Entity
from entities.item import Item
from components.baseComponents import DescriptionComponent
from components.roomsComponents import RoomConnectionComponent
from dataclasses import dataclass,field
from data.enemies import Goblin
from typing import List

@dataclass
class Room(Entity):
    items: List[Item] = field(default_factory=list)
    enemy: Entity = None
    connectedRooms: List[RoomConnectionComponent] = field(default_factory=list)
    roomIntro: str = " "
    roomSearchStrings: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.playerInRoom = False

testRoom = Room(
    name="Test Room",
    enemy=Goblin,
    descriptionComp=DescriptionComponent("This is a cool looking test room."),
    roomIntro="This is still a cool looking test room"
)