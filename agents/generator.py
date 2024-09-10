from config import model
from langchain_core.messages import SystemMessage, HumanMessage
from utils.prompts import WRITER_PROMPT
from langgraph.graph import END

def generation_node(state):
    content = "\n\n".join(state['content'] or [])
    user_message = HumanMessage(
        content=f"{state['task']}\n\nHere is my plan:\n\n{state['plan']}")
    messages = [
        SystemMessage(
            content=WRITER_PROMPT.format(content=content)
        ),
        user_message
    ]
    response = model.invoke(messages)
    return {
        "draft": response.content,
        "revision_number": state.get("revision_number", 1) + 1
    }

def should_continue(state):
    if state["revision_number"] > state["max_revisions"]:
        return END
    return "reflect"
