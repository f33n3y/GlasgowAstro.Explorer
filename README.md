# GlasgowAstro.Explorer AI Agent 🌌👽

Welcome to the **GlasgowAstro.Explorer**, an intelligent explorer designed to traverse alien biomes and collect virtual samples for scientific analysis. 
This project leverages the [smolagents framework](https://github.com/huggingface/smolagents) to create an agent that can move, investigate, and catalog extraterrestrial life forms and ecosystems - all from the safety of your computer.

![GlasgowAstro Explorer](images/GlasgowAstroExplorer.png)

---

### ⚠️ Current Challenges & Observations

- The agent sometimes loops endlessly or revisits the same planet positions instead of covering new ground.  
- Certain models (e.g., `deepseek-r1:7b`, `qwen2.5-coder:7b`) struggle to follow tool-calling rules, skipping or misusing available tools.  
- The agent occasionally invents discoveries or “simulates” exploration rather than relying on actual tool output.  
- Large models (e.g., `qwen3-coder:30b`) perform better reasoning but can be too slow or memory-intensive on local hardware.  
- Maintaining a consistent exploration pattern (e.g., avoiding circular or stuck movement) has required increasingly explicit prompting and structured traversal strategies (like “snake” or “zigzag” paths).  

---