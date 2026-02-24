Phase 1: Microsoft Tutorial → Read + run examples, come back with doubts

Phase 2: Project Janus Rebuild → Apply MCP to your existing project, identify friction points

Phase 3: Custom MCP Server → Build one tool server (FastMCP), test with your agent

Phase 4: Transports → Start with stdio (simpler debugging), then streamable-http for production parity

Phase 5: Resources + Auth + Basic Interceptor → One interceptor that injects an API key is enough

Phase 6: Stateful Session → Use client.session() when you need context across multiple tool calls

Phase 7: Structured Output → Tools returning {"result": ..., "metadata": ...} instead of just text

The Only Missing Piece (The "Tool Selection" Problem)

Bidirectional Sampling: This is the biggest update to MCP in 2026. It allows the server to ask the host (your agent) to perform a task.[1] (e.g., A database server asks the agent to "summarize this schema" before it executes a query). You must learn how to handle sampling/createMessage requests.

Prompt Primitives: Don't just focus on tools. MCP servers can now serve "standardized prompts."[2] This is how you build reusable "agent personas" that can be shared across different systems.

LangGraph Integration: Since my goal is LangGraph, do not just use create_react_agent. Learn how to manually map MCP tools to nodes in a LangGraph state machine. This is where the real "architect" level work happens.

