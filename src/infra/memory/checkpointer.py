from langgraph.checkpoint.memory import MemorySaver
import os


class CheckpointerFactory:
    def __init__(self):
        self.backend = os.getenv("MEMORY_BACKEND", "memory")

    def create(self):
        if self.backend == "memory":
            return MemorySaver()

        raise ValueError(f"Unsupported memory backend: {self.backend}")