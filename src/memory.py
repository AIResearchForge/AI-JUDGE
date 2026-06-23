# src/memory.py (simpler version)
from langchain.memory import ConversationBufferMemory


def get_memory_base():
    """Creates and returns a simple memory for Agent 3."""
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        input_key="input",
        output_key="output",
    )
    return memory
