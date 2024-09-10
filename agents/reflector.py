from config import model
from langchain_core.messages import SystemMessage, HumanMessage
from utils.prompts import REFLECTION_PROMPT

def reflection_node(state):
    messages = [
        SystemMessage(content=REFLECTION_PROMPT),
        HumanMessage(content=state['draft'])
    ]
    response = model.invoke(messages)
    return {"critique": response.content}