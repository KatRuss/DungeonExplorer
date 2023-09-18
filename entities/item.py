from dataclasses import dataclass, field
from typing import List
from entities.entity import Entity
from components.itemComp import AttackComponent, DefenseComponent, UseComponent

@dataclass
class Item(Entity):
    attackComponents: List[AttackComponent] = field(default_factory=list)
    defenseComponents: List[DefenseComponent] = field(default_factory=list)
    useComponent: UseComponent = None

    def __str__(self) -> str:
        return self.name

    def printStats(self):
        print(f"=== {self.name} ===")
        num = 1
        if self.attackComponents != []:
            print(f"=== Attacks ===")
            for attack in self.attackComponents:
                print(f" - {attack.diceNum}d{attack.dice.sides}{f'+{attack.flatDamage} ' if attack.flatDamage > 0 else ' '}{attack.atype.name} Damage")
                num+=1
        num = 1
        if self.defenseComponents != []:
            print("=== Defences ===")
            for defense in self.defenseComponents:
                print(f" - {defense.amount} {defense.defType.name} defense")
                num += 1
        # Insert Use Components here
        print("== Description ==")
        print(self.descriptionComp)