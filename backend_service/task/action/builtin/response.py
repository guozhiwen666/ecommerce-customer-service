from typing import Any

from backend_service.domain.messages import BotMessage
from backend_service.domain.state import DialogueState
from backend_service.task.action.base import Action, ActionResult


class ActionResponse(Action):
    name = "action_response"

    async def run(self, action_kwargs: dict[str, Any], state: DialogueState) -> ActionResult:
        """
        根据action_kwargs的文本内容，解析占位，封装到ActionResult的messages中BotMessage内容

        Args:
            action_kwargs:
            state:
        Returns:
        """
        return ActionResult(messages=[BotMessage(text=
                    "订单{{ slots.order_number }}当前状态是：{{ slots.order_status }}。{{ slots.order_summary }}")])
