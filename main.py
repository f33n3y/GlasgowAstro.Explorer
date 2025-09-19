from models.alien_flora import AlienFlora
from models.planet import Planet

planet = Planet("Glasgovaar")
flora1 = AlienFlora("Zoraphoty", rarity=3)
flora2 = AlienFlora("Weeflumpsa", rarity=5)
flora3 = AlienFlora("Uisgebeatha", rarity=8)
planet.place_flora(flora1)
planet.place_flora(flora2)
planet.place_flora(flora3)
print(flora1.describe())
print(flora2.describe())
print(flora3.describe())
planet.print_grid()