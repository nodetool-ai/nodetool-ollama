import asyncio
from nodetool.dsl.graph import graph, run_graph
from nodetool.dsl.nodetool.output import StringOutput
from nodetool.dsl.ollama.text import Ollama
from nodetool.metadata.types import LlamaModel

text = """
The Artificial Intelligence (AI) landscape has evolved dramatically over the past decade. What was once the domain of specialized researchers has now become accessible to developers and businesses of all sizes. This democratization of AI has been driven by several factors: the availability of powerful open-source models, decreasing computational costs, and the emergence of user-friendly frameworks and tools.

Large Language Models (LLMs) like GPT-4, Claude, and Llama have particularly transformed how we interact with AI systems. These models can understand and generate human language with remarkable fluency, enabling applications from content creation to code generation, from customer service to data analysis.

However, this rapid advancement comes with challenges. Ethical considerations around bias, privacy, and the environmental impact of training large models remain significant concerns. Additionally, as AI becomes more capable, questions about governance, safety, and alignment with human values grow increasingly important.

The future of AI development will likely focus on making models more efficient, transparent, and aligned with human needs. Techniques like fine-tuning, retrieval-augmented generation, and human feedback mechanisms are already improving how these systems perform in specialized domains. As these technologies continue to mature, the ability to create AI-powered solutions that are both powerful and responsible will be crucial for developers and organizations alike.
"""

# Generate summary using Gemma
summary = Ollama(
    prompt=f"Summarize the following text: {text}",
    model=LlamaModel(repo_id="llama3.2:3b"),
    system_prompt="You are a summarizer.",
    context_window=4096,
    temperature=0,
    top_k=50,
    top_p=0.95,
)

output = StringOutput(
    name="summary",
    description="Summary of the emails",
    value=summary,
)

summary_str = asyncio.run(run_graph(graph(output)))
print(summary_str)
