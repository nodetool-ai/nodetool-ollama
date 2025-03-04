import asyncio
from nodetool.dsl.graph import graph, run_graph
from nodetool.dsl.nodetool.output import StringOutput
from nodetool.dsl.ollama.text import Ollama
from nodetool.metadata.types import LlamaModel

# Example text to classify
text = """
The new smartphone features a 6.7-inch OLED display, 256GB storage, and a powerful A15 chip. 
It comes with advanced camera capabilities including night mode and portrait photography. 
The battery life is impressive, lasting up to 18 hours on a single charge. 
The device runs the latest version of iOS and includes 5G connectivity.
"""

# Generate classification using Gemma
classification = Ollama(
    prompt=f"""Classify the following text into one of these categories: 
    - Product Review
    - Technical Specification
    - Marketing Copy
    - User Manual
    
    Text to classify: {text}
    
    Respond with just the category name.""",
    model=LlamaModel(repo_id="llama3.2:3b"),
    system_prompt="You are a text classifier. Respond with only the category name.",
    context_window=4096,
    temperature=0,
    top_k=50,
    top_p=0.95,
)

output = StringOutput(
    name="classification",
    description="Classification of the input text",
    value=classification,
)

classification_result = asyncio.run(run_graph(graph(output)))
print(f"Classification: {classification_result}")
