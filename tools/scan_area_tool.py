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
        "Use this tool to scan the current location on the planet grid. "
        "This tool will detect whether any alien flora or fauna are present at the explorer's current position. "
        "This tool returns a string describing what was found, including the lifeform's type, name, and rarity. "
        "If nothing is discovered, it will clearly state that no alien life was detected."
    )

    inputs = {}
    output_type = "string"

    def forward(self) -> str:
        print("Agent called scan_area_tool")
        x, y = self.explorer.get_position()
        alien_discovery = self.planet.check_grid(x, y)

        if alien_discovery is None:
            return f"No alien life was detected at position ({x}, {y})."

        return (
            f"Alien discovery at ({x}, {y}): "
            f"Type={alien_discovery.__class__.__name__}, "
            f"Name={alien_discovery.name}, "
            f"Rarity={alien_discovery.rarity}"
        )
