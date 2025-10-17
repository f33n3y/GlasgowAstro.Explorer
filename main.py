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

planet = Planet(planet_name="Glasgovaar", grid_size=5)
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
    model_id="ollama_chat/deepseek-r1:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

exploration_prompt = """
You are an explorer named "glasgowastro" on an alien planet (a 5x5 grid).
Your GOAL is to explore and log any alien life you discover.

IMPORTANT RULES:
- You MUST only use the tools available to achieve your goal.
- Before starting your exploration, you MUST plan your approach so that you can cover at least 7 locations.  
- You MUST NOT simulate, invent or guess any discoveries.
- After each move, you MUST scan the area and log any alien life that you find.
- You MUST ONLY log discoveries returned by the scan area tool.
- Always wrap your executable code inside <code> and </code> tags and Do NOT use markdown-style triple backticks.
"""

agent = CodeAgent(tools=[move_explorer_tool, scan_area_tool, log_discovery_tool, summarise_discoveries_tool],
                  model=model, verbosity_level=2, additional_authorized_imports=["random"], max_steps=50)
result = agent.run(exploration_prompt)
print(result)
