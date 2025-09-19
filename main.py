from models.alien_flora import AlienFlora
from models.planet import Planet

planet = Planet("Glasgovaar")
flora_list = [
    AlienFlora("Zoraphoty", rarity=3),
    AlienFlora("Weeflumpsa", rarity=5),
    AlienFlora("Uisgebeatha", rarity=8)
]

for flora in flora_list:
    planet.place_flora(flora)
    print(flora.describe())

planet.print_grid()