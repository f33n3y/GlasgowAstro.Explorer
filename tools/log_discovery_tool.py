from smolagents import Tool

from models.discovery import Discovery
from models.logbook import Logbook


class LogDiscoveryTool(Tool):
    def __init__(self, logbook: Logbook):
        super().__init__()
        self.logbook = logbook

    name = "log_discovery_tool"
    description = (
        "Use this tool to keep track of all unique alien life discovered by the explorer. "
        "You can log a discovery with log_discovery(name, type_of_life, x, y), "
        "or get a summary of all discoveries with summarize_discoveries()."
    )
    inputs = {
        "name": {"type": "string", "description": "Name of the alien life."},
        "type_of_life": {"type": "string", "description": "The type of the alien life (Flora or Fauna)."},
        "x": {"type": "integer", "description": "X-coordinate of the discovery."},
        "y": {"type": "integer", "description": "Y-coordinate of the discovery."},
        "rarity": {"type": "integer", "description": "Rarity of the alien life."}
    }
    output_type = "string"

    def forward(self, name: str, type_of_life: str, x: int, y: int, rarity: int) -> str:
        discovery = Discovery(name, type_of_life, x, y, rarity)
        return self.logbook.add_discovery(discovery)