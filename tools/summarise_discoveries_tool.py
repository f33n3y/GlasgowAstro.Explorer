from smolagents import Tool

from models.logbook import Logbook


class SummariseDiscoveriesTool(Tool):
    def __init__(self, logbook: Logbook):
        super().__init__()
        self.logbook = logbook

    name = "summarise_discoveries_tool"
    description = ("Use this tool to obtain a summary of all alien life discovered during planet exploration. "
                   "This tool should only be called when you have finished exploring the planet")
    inputs = {}
    output_type = "string"

    def forward(self) -> str:
        return self.logbook.summarize()
