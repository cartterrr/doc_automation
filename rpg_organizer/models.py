import uuid
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any

def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

@dataclass
class Item:
    id: str
    name: str
    type: str = "misc"
    weight: float = 0.0
    notes: str = ""

    @classmethod
    def create(cls, name: str, type_: str = "misc", weight: float = 0.0, notes: str = ""):
        return cls(id=new_id("item"), name=name, type=type_, weight=weight, notes=notes)

@dataclass
class Character:
    id: str
    name: str
    level: int = 1
    hp: int = 10
    mp: int = 0
    attributes: Dict[str, int] = field(default_factory=lambda: {"str": 10, "dex": 10, "int": 10})
    inventory: List[str] = field(default_factory=list)

    @classmethod
    def create(cls, name: str):
        return cls(id=new_id("char"), name=name)

@dataclass
class Quest:
    id: str
    title: str
    status: str = "open"  # open, in_progress, done
    notes: str = ""

    @classmethod
    def create(cls, title: str, notes: str = ""):
        return cls(id=new_id("quest"), title=title, notes=notes)

# convert dataclass to dict for json storage
def to_serializable(obj: Any):
    if hasattr(obj, "__dataclass_fields__"):
        return asdict(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
