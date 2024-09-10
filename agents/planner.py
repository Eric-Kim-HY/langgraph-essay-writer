from config import model
from langchain_core.messages import SystemMessage, HumanMessage
from utils.prompts import PLAN_PROMPT

def plan_node(state):
    messages = [
        SystemMessage(content=PLAN_PROMPT),
        HumanMessage(content=state['task'])
    ]
    response = model.invoke(messages)
    return {"plan": response.content}