🐛 Troubleshooting

Common issues you might encounter when building agents: "Agent loops forever or hits max iterations"

Cause: Agent doesn't have a stopping condition or tools don't return useful results

Fixes:

Check your stopping condition:

if not response.tool_calls or len(response.tool_calls) == 0: # Agent has finished - no more tools needed break

Lower max_iterations to fail fast during development:

max_iterations = 3 # Start small, increase if needed

Ensure tools return meaningful results - vague outputs confuse the agent

"Tool not found" error

Cause: Tool name mismatch between what LLM generates and what you defined

Fix: Verify the tool name exactly matches:

@tool def calculator(expression: str) -> str: # Name must match exactly """Perform mathematical calculations.""" # ...

Agent makes wrong tool choices

Cause: Tool descriptions aren't clear enough

Fix: Improve tool descriptions with specific use cases:
❌ Vague

"""Does calculations"""
✅ Clear

"""Perform mathematical calculations like addition, multiplication, percentages. Use this when you need to compute numbers."""

Agent gets stuck repeating the same tool

Cause: Tool doesn't provide enough information for agent to progress

Fix: Ensure tool results are descriptive:
❌ Not helpful

return "42"
✅ Descriptive

return "The calculation result is 42. This is the answer to 6 * 7."
