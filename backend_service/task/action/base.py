from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from backend_service.domain.messages import BotMessage
from backend_service.engines.dialogue_engine import DialogueEngine


@dataclass
class ActionResult:
    messages: list[BotMessage] = field(default_factory=list)
    updated_slots: dict[str, Any] = field(default_factory=dict)


class Action(ABC):
    name: str

    @abstractmethod
    async def run(self, action_kwargs: dict[str, Any], state: DialogueEngine) -> ActionResult:
        pass