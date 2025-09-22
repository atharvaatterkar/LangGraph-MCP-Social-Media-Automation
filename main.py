import asyncio
from workflow import create_workflow, PostState

async def main():
    workflow, client = await create_workflow()
    await workflow.ainvoke({"topic": "LangGraph + MCP automation for X & LinkedIn posting"})


if __name__ == "__main__":
    asyncio.run(main())
