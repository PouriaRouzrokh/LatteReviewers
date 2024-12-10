from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class BaseAgent(BaseModel):
    response_format: Any
    provider: Optional[Any] = None
    max_concurrent_requests: int = 20
    name: str = "BaseAgent"
    backstory: str = "a generic base agent"
    temperature: float = 0.2
    max_tokens: int = 150
    review_type: str = "title/abstract"
    review_criteria: Optional[str] = None
    scoring_schema: str = "[0, 1]"
    scoring_rules: str = "Your scores should follow the defined schema."
    help_criteria: str = "Seek help when uncertain."
    memory: List[Dict] = []
    review_prompt: str = "Default review prompt."
    identity: dict = dict()

    def build_identity(self) -> None:
        """
        Build the agent's identity based on its attributes.
        """
        raise NotImplementedError("This method must be implemented by subclasses.")

    def reset_memory(self) -> None:
        """
        Reset the memory of the agent.
        """
        raise NotImplementedError("This method must be implemented by subclasses.")

    async def review_items(self, items: List[str]) -> List[Dict]:
        """
        Review a list of items asynchronously.
        """
        raise NotImplementedError("This method must be implemented by subclasses.")

    async def review_item(self, item: str) -> Dict:
        """
        Review a single item asynchronously.
        """
        raise NotImplementedError("This method must be implemented by subclasses.")