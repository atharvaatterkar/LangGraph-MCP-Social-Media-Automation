from mcp.server.fastmcp import FastMCP
from content_generator import generate_post
from post_to_x import post_to_x
from post_to_linkedin import post_to_linkedin

mcp = FastMCP("social_media_tools")

@mcp.tool()
async def generate_content_tool(topic: str) -> str:
    return generate_post(topic)

@mcp.tool()
async def post_to_x_tool(content: str) -> str:
    post_to_x(content)
    return f"Posted to X: {content}"

@mcp.tool()
async def post_to_linkedin_tool(content: str) -> str:
    post_to_linkedin(content)
    return f"Posted to LinkedIn: {content}"

if __name__ == "__main__":
    print("Starting MCP server... waiting for client connections.")
    mcp.run(transport="stdio")
