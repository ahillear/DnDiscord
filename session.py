from dataclasses import dataclass
import random


# Dataclass to store the session state
@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0
    player = None