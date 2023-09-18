from systems.playerCreatorSystem import playerCreator
from systems.combatSystem import initCombat
from data.enemies import Goblin


player = playerCreator()
enemy = Goblin

initCombat(player,enemy)