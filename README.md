# Nodetool Ollama Nodes

A collection of nodes for integrating Ollama language models into Nodetool workflows. This package provides powerful nodes for text generation, embeddings, and model predictions using Ollama's local LLM capabilities.

## Features

### Text Generation Node

The `Ollama` node provides advanced text generation capabilities:

- Support for chat and completion modes
- Configurable model parameters (temperature, top_k, top_p)
- Context window management
- System prompt support
- Message history handling
- Image analysis capabilities

### Embedding Nodes

Two specialized nodes for text embeddings:

1. `Embedding` Node

   - Generates vector representations of text
   - Supports semantic similarity analysis
   - Configurable context window
   - Model selection options

2. `AggregateEmbeddings` Node
   - Aggregates multiple embeddings into a single vector
   - Supports multiple aggregation methods:
     - Mean
     - Max
     - Min
     - Sum
   - Ideal for batch processing and semantic analysis

## Use Cases

- Creative writing and story generation
- Question answering and explanations
- Code assistance and problem-solving
- Open-ended dialogue
- Semantic search implementation
- Text clustering and categorization
- Recommendation systems
- Anomaly detection
- Text classification
- Semantic similarity analysis

## Configuration

The nodes support various configuration options:

- Model selection
- Context window size (64 to 65536 tokens)
- Temperature (0.0 to 1.0)
- Top-k sampling (1 to 100)
- Top-p sampling (0.0 to 1.0)
- Number of predictions (1 to 10000)

## Requirements

- Ollama installed and running locally
- Python 3.10+
- Nodetool framework

## Installation

Install in the Nodetool UI or manually:

```bash
nodetool-package install nodetool-ai/nodetool-ollama
```

## Usage

1. Ensure Ollama is running locally
2. Import the nodes in your Nodetool workflow
3. Configure the nodes with your desired parameters
4. Connect the nodes to create your workflow

## Best Practices

1. **Context Window Management**

   - Keep context windows within reasonable limits (4096 tokens default)
   - Consider using the AggregateEmbeddings node for longer texts

2. **Temperature Settings**

   - Lower temperatures (0.0-0.3) for more focused, deterministic outputs
   - Higher temperatures (0.7-1.0) for more creative, diverse outputs

3. **System Prompts**

   - Use clear, specific system prompts to guide model behavior
   - Consider the task type when setting the system prompt

4. **Message History**
   - Maintain relevant conversation history for better context
   - Clear history when starting new topics or tasks

## License

AGPL
