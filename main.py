from smolagents import LiteLLMModel, CodeAgent

from models.alien_fauna import AlienFauna
from models.alien_flora import AlienFlora
from models.explorer import Explorer
from models.logbook import Logbook
from models.planet import Planet
from tools.log_discovery_tool import LogDiscoveryTool
from tools.move_explorer_tool import MoveExplorerTool
from tools.scan_area_tool import ScanAreaTool
from tools.summarise_discoveries_tool import SummariseDiscoveriesTool

planet = Planet(planet_name="Glasgovaar", grid_size=3)
flora_list = [
    AlienFlora("Zoraphoty", rarity=3),
    AlienFlora("Weeflumpsa", rarity=5),
    AlienFlora("Uisgebeatha", rarity=8)
]

fauna_list = [
    AlienFauna("Llamatank", rarity=4),
    AlienFauna("Spacedoggo", rarity=3),
    AlienFauna("Otteroo", rarity=10),
]

for flora in flora_list:
    planet.place_life(flora)
    print(flora.describe())

for fauna in fauna_list:
    planet.place_life(fauna)
    print(fauna.describe())

explorer = Explorer("glasgowastro", planet)
logbook = Logbook()
planet.print_grid()

move_explorer_tool = MoveExplorerTool(explorer)
scan_area_tool = ScanAreaTool(explorer, planet)
log_discovery_tool = LogDiscoveryTool(logbook)
summarise_discoveries_tool = SummariseDiscoveriesTool(logbook)

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

exploration_prompt = """
You are an explorer named "glasgowastro" on an alien planet.
Your goal is to move, scan for alien life, and log any discoveries you make.

RULES:
- Start by scanning your initial position before moving.
- After that, always move before scanning. Never scan twice in a row without moving.
- After scanning, log any discoveries.
- Stop exploring once you have logged at least 2 unique alien lifeforms.
- Only use the tools provided: move_explorer_tool, scan_area_tool, log_discovery_tool, summarise_discoveries_tool.
- Never simulate, invent or guess your discoveries.
"""




agent = CodeAgent(tools=[move_explorer_tool, scan_area_tool, log_discovery_tool, summarise_discoveries_tool],
                  model=model, verbosity_level=2, additional_authorized_imports=["random"], max_steps=50)
result = agent.run(exploration_prompt)
print(result)
