from smolagents import Tool
from models.explorer import Explorer

class MoveExplorerTool(Tool):
    def __init__(self, explorer: Explorer):
        super().__init__()
        self.explorer = explorer

    name = "move_explorer_tool"
    description = (
        "This tool allows you to move an explorer's position on a planet grid by providing an offset for the explorer's x and y coordinates. "
        "For example, dx=1, dy=0 moves you one step to the right. "
        "The tool will return a boolean indicating whether the move was successful."
    )

    inputs = {
        "dx": {
            "type": "integer",
            "description": "The number of spaces to move in the x axis."
        },
        "dy": {
            "type": "integer",
            "description": "The number of spaces to move in the y axis."
        }
    }
    output_type = "string"

    def forward(self, dx: int, dy: int) -> str:
        print("Agent called move_explorer_tool")
        success = self.explorer.move(dx, dy)
        if success:
            return f"Moved to ({self.explorer.x_pos}, {self.explorer.y_pos})."
        return "Move failed: out of bounds."
