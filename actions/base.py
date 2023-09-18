from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entities.entity import Entity

@dataclass 
class Action(ABC):
    @abstractmethod
    def do(self, target):
        pass