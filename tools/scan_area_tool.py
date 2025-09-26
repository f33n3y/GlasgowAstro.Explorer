from typing import Optional, Dict, Any

from smolagents import Tool

from models.explorer import Explorer
from models.planet import Planet


class ScanAreaTool(Tool):
    def __init__(self, explorer: Explorer, planet: Planet):
        super().__init__()
        self.explorer = explorer
        self.planet = planet

    name = "scan_area_tool"
    description = (
        "This tool allows you to scan an area on the planet for alien flora and fauna"
        "This tool will return an object containing the type, name and rarity of what has been discovered."
    )

    inputs = {}
    output_type = "object"

    def forward(self) -> Optional[Dict[str, Any]]:
        print("Agent called scan_area_tool")
        x, y = self.explorer.get_position()
        alien_discovery = self.planet.check_grid(x, y)

        if alien_discovery is None:
            return None

        return {
            "type" : "AlienFlora",
            "name" : alien_discovery.name,
            "rarity" : alien_discovery.rarity,
        }
