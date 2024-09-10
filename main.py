from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from models.state import AgentState
from agents import planner, generator, reflector, researcher
from utils.prompts import PLAN_PROMPT, WRITER_PROMPT, REFLECTION_PROMPT
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

def main():
    memory = SqliteSaver.from_conn_string(":memory:")

    builder = StateGraph(AgentState)

    builder.add_node("planner", planner.plan_node)
    builder.add_node("generate", generator.generation_node)
    builder.add_node("reflect", reflector.reflection_node)
    builder.add_node("research_plan", researcher.research_plan_node)
    builder.add_node("research_critique", researcher.research_critique_node)

    builder.set_entry_point("planner")

    builder.add_conditional_edges(
        "generate",
        generator.should_continue,
        {END: END, "reflect": "reflect"}
    )

    builder.add_edge("planner", "research_plan")
    builder.add_edge("research_plan", "generate")
    builder.add_edge("reflect", "research_critique")
    builder.add_edge("research_critique", "generate")

    graph = builder.compile(checkpointer=memory)
    
    # 그래프 실행 코드
    task = input("질문을 입력하세요: ")
    thread = {"configurable": {"thread_id": "1"}}
    for event in graph.stream({
        'task': task,
        "max_revisions": 2,
        "revision_number": 1,
    }, thread):
        print(event)

if __name__ == "__main__":
    main()