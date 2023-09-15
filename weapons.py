from entity import Item
from components import *

Longsword = Item(
    name="Longsword",
    weight=WeightComponent(3.5),
    attackComponent= AttackComponent(),
)