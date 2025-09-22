from smolagents import LiteLLMModel, CodeAgent

from models.alien_flora import AlienFlora
from models.explorer import Explorer
from models.planet import Planet
from tools.move_explorer_tool import MoveExplorerTool

planet = Planet("Glasgovaar")
flora_list = [
    AlienFlora("Zoraphoty", rarity=3),
    AlienFlora("Weeflumpsa", rarity=5),
    AlienFlora("Uisgebeatha", rarity=8)
]

for flora in flora_list:
    planet.place_flora(flora)
    print(flora.describe())

explorer = Explorer("glasgowastro", planet)
planet.print_grid()

move_explorer_tool = MoveExplorerTool(explorer)

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

exploration_prompt = """
You are an explorer named "glasgowastro" who has landed on an alien planet. 
Your goal is to move around the planet.
- You start at position (0,0).
- After each move, reflect on your position and describe your journey as if you are a real explorer.
- Continue moving until you have explored several positions.
"""

agent = CodeAgent(tools=[move_explorer_tool], model=model, verbosity_level=2, additional_authorized_imports=["random"])
result = agent.run(exploration_prompt)
print(result)
