from entity import Item
from components import *

Longsword = Item(
    name="Longsword",
    weight=WeightComponent(3.5),
    attackComponent= AttackComponent(),
    description=DescriptionComponent("A common sword, used by savours and villains alike./n With skilled hands, a fine blade is all you will ever need.")
)

Mace = Item(
    name="Mace",
    weight=WeightComponent(3.5),
    attackComponent= AttackComponent(),
    description=DescriptionComponent("[Mace Description]")
)

testWeaponList = [Longsword,Mace]