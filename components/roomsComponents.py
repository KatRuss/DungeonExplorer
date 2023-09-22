from dataclasses import dataclass

class LockComponent:
    pass

@dataclass
class RoomConnectionComponent:
    otherRoom: object = None
    lock: LockComponent = None
    
