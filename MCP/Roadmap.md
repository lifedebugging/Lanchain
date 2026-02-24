Phase 1: Microsoft Tutorial → Read + run examples, come back with doubts

Phase 2: Project Janus Rebuild → Apply MCP to your existing project, identify friction points

Phase 3: Custom MCP Server → Build one tool server (FastMCP), test with your agent

Phase 4: Transports → Start with stdio (simpler debugging), then streamable-http for production parity

Phase 5: Resources + Auth + Basic Interceptor → One interceptor that injects an API key is enough

Phase 6: Stateful Session → Use client.session() when you need context across multiple tool calls

Phase 7: Structured Output → Tools returning {"result": ..., "metadata": ...} instead of just text

The Only Missing Piece (The "Tool Selection" Problem)
