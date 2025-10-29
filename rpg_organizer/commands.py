from .models import Character, Item, Quest, to_serializable
from .storage import JSONStorage
from typing import Optional

class RPGManager:
    def __init__(self, storage: JSONStorage = None):
        self.storage = storage or JSONStorage()
        self.data = self.storage.load()

    # Characters
    def list_characters(self):
        return self.data.get("characters", [])

    def get_character(self, char_id: str) -> Optional[dict]:
        for c in self.data["characters"]:
            if c["id"] == char_id:
                return c
        return None

    def add_character(self, name: str):
        c = Character.create(name)
        self.data["characters"].append(to_serializable(c))
        self.storage.save(self.data)
        return c

    def remove_character(self, char_id: str) -> bool:
        before = len(self.data["characters"])
        self.data["characters"] = [c for c in self.data["characters"] if c["id"] != char_id]
        self.storage.save(self.data)
        return before != len(self.data["characters"])

    # Items
    def add_item(self, name: str, type_: str = "misc", weight: float = 0.0, notes: str = ""):
        it = Item.create(name, type_, weight, notes)
        self.data["items"].append(to_serializable(it))
        self.storage.save(self.data)
        return it

    def list_items(self):
        return self.data.get("items", [])

    # Quests
    def add_quest(self, title: str, notes: str = ""):
        q = Quest.create(title, notes)
        self.data["quests"].append(to_serializable(q))
        self.storage.save(self.data)
        return q

    def list_quests(self):
        return self.data.get("quests", [])

    # Inventory ops: add item id to character inventory
    def give_item_to_character(self, char_id: str, item_id: str):
        c = self.get_character(char_id)
        if not c:
            raise ValueError("Character not found")
        # check item exists
        if not any(it["id"] == item_id for it in self.data["items"]):
            raise ValueError("Item not found")
        c.setdefault("inventory", []).append(item_id)
        self.storage.save(self.data)
        return True
