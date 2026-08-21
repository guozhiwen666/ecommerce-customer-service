from typing import Any

from backend_service.domain.state import DialogueState
from backend_service.task.action.base import Action, ActionResult


class ActionListener(Action):
    name = "action_listen"

    async def run(self, action_kwargs: dict[str, Any], state: DialogueState) -> ActionResult:
        return ActionResult()