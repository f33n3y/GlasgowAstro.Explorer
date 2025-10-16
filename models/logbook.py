from typing import Set

from models.discovery import Discovery


class Logbook:
    def __init__(self):
        self.discoveries: Set[Discovery] = set()

    def add_discovery(self, discovery: Discovery) -> str:
        if discovery in self.discoveries:
            return f"Discovery already logged: {discovery.name} ({discovery.type_of_life}) at ({discovery.x}, {discovery.y})"
        self.discoveries.add(discovery)
        return f"Logged discovery: {discovery.name} ({discovery.type_of_life}) at ({discovery.x}, {discovery.y})"

    def summarize(self) -> str:
        if not self.discoveries:
            return "No discoveries have been logged."
        summary = "Summary of all discoveries:\n"
        for d in sorted(self.discoveries, key=lambda x: (x.type_of_life, x.name)):
            summary += f"- {d.type_of_life} named {d.name} at ({d.x}, {d.y}), rarity {d.rarity}\n"
        return summary
