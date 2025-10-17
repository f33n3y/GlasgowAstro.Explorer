from smolagents import Tool
from models.explorer import Explorer

class MoveExplorerTool(Tool):
    def __init__(self, explorer: Explorer):
        super().__init__()
        self.explorer = explorer

    name = "move_explorer_tool"
    description = (
        "Use this tool to move the explorer to a new position on the planet. "
        "Provide this tool with horizontal (dx) and vertical (dy) offsets to indicate the movement direction and distance — for example, dx=1, dy=0 moves one step to the right. "
        "This tool updates the explorer's coordinates and returns a message indicating whether the move was successful or if it failed due to reaching the planet's boundary. "
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
        return (
            f"Move failed: Explorer cannot move outside the planet bounds. "
            f"Explorer remains at ({self.explorer.x_pos}, {self.explorer.y_pos}). "
            f"Try a different direction."
        )
