from models.planet import Planet

class Explorer:
    def __init__(self, name: str, planet: Planet):
        self.name = name
        self.planet = planet
        self.x_pos = 0
        self.y_pos = 0
        print(f"Explorer {self.name} initialised at {self.x_pos},{self.y_pos}")

    def move(self, dx: int, dy: int) -> bool:
        new_x = self.x_pos + dx
        new_y = self.y_pos + dy
        if self.planet.is_within_grid(new_x, new_y):
            self.x_pos = new_x
            self.y_pos = new_y
            print(f"Explorer moved to position {self.x_pos},{self.y_pos}")
            return True
        print(f"Explorer cannot move outside planet bounds. Explorer remains at {self.x_pos},{self.y_pos}")
        return False

    def get_position(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos