import json
from pathlib import Path
from typing import Dict, Any

DEFAULT_PATH = Path(__file__).parent / "data.json"

class JSONStorage:
    def __init__(self, path: Path = None):
        self.path = Path(path) if path else DEFAULT_PATH
        if not self.path.exists():
            # create default structure
            self.save({"characters": [], "items": [], "quests": []})

    def load(self) -> Dict[str, Any]:
        # use utf-8-sig to correctly handle files that start with BOM
        with open(self.path, "r", encoding="utf-8-sig") as f:
            return json.load(f)

    def save(self, data: Dict[str, Any]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
