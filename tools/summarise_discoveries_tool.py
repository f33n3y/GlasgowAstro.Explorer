from smolagents import Tool

from models.logbook import Logbook

class SummariseDiscoveriesTool(Tool):
    def __init__(self, logbook: Logbook):
        super().__init__()
        self.logbook = logbook

    name = "summarise_discoveries"
    description = "Use this tool to return a summary of all discoveries in the logbook."
    inputs = {}
    output_type = "string"

    def forward(self) -> str:
        return self.logbook.summarize()
