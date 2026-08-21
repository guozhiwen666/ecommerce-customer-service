from backend_service.domain.messages import BotMessage
from backend_service.domain.state import DialogueState
from backend_service.knowledge.intents import KnowledgeIntent


class KnowledgeHandler:
    def __init__(self, knowledge_intents: dict[str, KnowledgeIntent]):
        self.knowledge_intents = knowledge_intents

    async def handle(self, intent: list[str], dialogue_state: DialogueState) -> list[BotMessage]:
        pass