from pathlib import Path

from backend_service.chitchat.handler import ChitChatHandler
from backend_service.clarify.responder import ClarifyResponder
from backend_service.engines.dialogue_engine import DialogueEngine
from backend_service.knowledge.handler import KnowledgeHandler
from backend_service.plan.planner import TurnPlanner
from backend_service.plan.validator import TurnPlanValidator
from backend_service.task.flows.loader import FlowLoader
from backend_service.task.handler import TaskHandler

PROJECT_ROOT_DIR = Path(__file__).resolve().parents[2]
FLOW_CONFIG_DIR = PROJECT_ROOT_DIR / "flow_config"

def build_dialogue_engine():
    # 1.加载流程
    flow_list = FlowLoader().load_multi_yaml([FLOW_CONFIG_DIR / yaml for yaml in ("system_flows.yml", "user_flows.yml")])

    return DialogueEngine(
        turn_planner=TurnPlanner(),
        turn_plan_validator=TurnPlanValidator(),
        clarify_responder=ClarifyResponder(),
        task_handler=TaskHandler(flow_list=flow_list),
        knowledge_handler=KnowledgeHandler(),
        chitchat_handler=ChitChatHandler()
    )