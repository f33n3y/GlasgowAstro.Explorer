import random
from typing import Optional

from models.alien_flora import AlienFlora

class Planet:
    def __init__(self, planet_name):
        self.planet_name = planet_name
        self.grid = self._create_grid()

    @staticmethod
    def _create_grid() -> list[list[Optional['AlienFlora']]]:
        """Initialize an empty grid of None values"""
        return [[None for _ in range(10)] for _ in range(10)]

    def place_flora(self, flora: AlienFlora):
        """Place an AlienFlora on the grid"""
        rand_x = random.randint(0, 9)
        rand_y = random.randint(0, 9)
        self.grid[rand_x][rand_y] = flora
        print(f"Placed {flora.name} at position ({rand_x}, {rand_y})")

    def print_grid(self):
        """Print the planet grid with flora names in boxes"""
        cell_width = 12
        horizontal_line = "+" + "+".join(["-" * cell_width for _ in range(len(self.grid[0]))]) + "+"

        for row in self.grid:
            print(horizontal_line)
            row_str = "|"
            for cell in row:
                if cell is None:
                    content = "."
                else:
                    content = cell.name
                row_str += f"{content:^{cell_width}}|"
            print(row_str)
        print(horizontal_line)