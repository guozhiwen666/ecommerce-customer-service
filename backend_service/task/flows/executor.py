from backend_service.domain.messages import BotMessage


class FlowExecutor:

    async def execute_flow(self, dialogue_state, flow_list) -> list[BotMessage]:
        pass