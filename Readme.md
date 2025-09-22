Automate content generation and posting to X (Twitter) and LinkedIn using LangGraph, MultiServer MCP, and Groq AI. The system leverages a modular workflow with tools registered in an MCP server, integrated via LangGraph’s state graph orchestration.
---

---
###This project automates social media posting using a multi-step workflow:
- 1.Generate post content automatically based on a topic using Groq API.
- 2.Post the content to X (Twitter).
- 3.Post the content to LinkedIn.
- All tasks are orchestrated using LangGraph StateGraph, and the actual tools are registered in an MCP server for modular and reusable execution.
---

## 📁 Project Structure

```
mcp/
├─ main.py                 # Entry point of the project
├─ workflow.py             # Defines LangGraph workflow and nodes
├─ mcp_server.py           # MCP server registering all social media tools
├─ content_generator.py    # Uses Groq API to generate post content
├─ post_to_x.py            # Posts content to X (Twitter) via Tweepy
├─ post_to_linkedin.py     # Posts content to LinkedIn via REST API
├─ linkedin_auth.py        # Optional: LinkedIn OAuth flow
├─ .env                    # Environment variables (API keys, secrets)
├─ README.md               # Project documentation

```
