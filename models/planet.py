import random
from typing import Optional

from models.alien_life import AlienLife


class Planet:
    def __init__(self, planet_name: str, grid_size: int):
        self.planet_name = planet_name
        self.grid = self._create_grid(grid_size)

    @staticmethod
    def _create_grid(grid_size: int) -> list[list[Optional['AlienLife']]]:
        """Initialize an empty grid of None values"""
        return [[None for _ in range(grid_size)] for _ in range(grid_size)]

    def place_life(self, life: AlienLife):
        """Place an AlienLife on the grid"""
        placed = False
        attempt = 0

        while not placed and attempt < 3:
            rand_x = random.randint(0, len(self.grid) - 1)
            rand_y = random.randint(0, len(self.grid[0]) - 1)

            if self.grid[rand_x][rand_y] is None:
                self.grid[rand_x][rand_y] = life
                placed = True
                print(f"Placed {life.name} at position ({rand_x}, {rand_y})")
            attempt += 1


    def print_grid(self):
        """Print the planet grid with alien life names in boxes"""
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

    def is_within_grid(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def check_grid(self, x: int, y: int) -> Optional[AlienLife]:
        if not self.is_within_grid(x, y):
            raise ValueError(f"Coordinates ({x}, {y}) are outside the grid.")

        return self.grid[x][y]