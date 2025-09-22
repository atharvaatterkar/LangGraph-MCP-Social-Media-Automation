
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, END

class PostState(dict):
    topic: str
    content: str

async def create_workflow():
    
    client = MultiServerMCPClient(
        {
            "social": {
                "command": "python",
                "args": ["mcp_server.py"],  
                "transport": "stdio",
            }
        }
    )

    tools_list = await client.get_tools()
    tools = {tool.name: tool for tool in tools_list}


    async def generate_content_node(state: PostState):
        tool = tools["generate_content_tool"]
        result = await tool.ainvoke({"topic": state["topic"]})
        state["content"] = result
        print(f"Generated Content: {result}")
        return state

    async def post_to_x_node(state: PostState):
        tool = tools["post_to_x_tool"]
        await tool.ainvoke({"content": state["content"]})
        return state

    async def post_to_linkedin_node(state: PostState):
        tool = tools["post_to_linkedin_tool"]
        await tool.ainvoke({"content": state["content"]})
        return state

    workflow = StateGraph(PostState)
    workflow.add_node("generate", generate_content_node)
    workflow.add_node("post_x", post_to_x_node)
    workflow.add_node("post_linkedin", post_to_linkedin_node)

    workflow.set_entry_point("generate")
    workflow.add_edge("generate", "post_x")
    workflow.add_edge("post_x", "post_linkedin")
    workflow.add_edge("post_linkedin", END)

    return workflow.compile(), client
