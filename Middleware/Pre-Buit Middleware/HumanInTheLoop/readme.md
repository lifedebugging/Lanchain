# Human in the Loop
The Human-in-the-Loop (HITL) middleware lets you add human oversight to agent tool calls. When a model proposes an action that might require review — for example, writing to a file or executing SQL — the middleware can pause execution and wait for a decision.

It does this by checking each tool call against a configurable policy. If intervention is needed, the middleware issues an interrupt that halts execution. The graph state is saved using LangGraph’s persistence layer, so execution can pause safely and resume later.

The middleware defines three built-in ways a human can respond to an interrupt:

    approve - the action is approved as-is and executed without changes
    edit - the tool call is executed with modification
    reject - the tool call is rejected, with an explanation added to the conversation

When multiple tool calls are paused at the same time, each action requires a separate decision. Decisions must be provided in the same order as the actions appear in the interrupt request.

# Demo configuration File
You will get an error :

           NameError: name 'write_file_tool' is not defined

code :

     HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file" : True, #All decisions (approve, edit, reject)
                "execute_sql" : {"allowed_decisions" : ["approve", "reject"]}, #No editing
                "read_data" : False, #Safe operation no approval needed
                
This defines where we allow the interrupt of human in our code block.

Use cases :

Imagine you creating an Email writing llm. You approve it to write the email however to send the email it requires Human Interruption.

Supposed you attaching an document to another email, again you require Human Interruption to allow the llm to access your database and attach the file.


# Conclusion 

Responding to interrupts :

When you invoke the agent, it runs until it either completes or an interrupt is raised. An interrupt is triggered 
when a tool call matches the policy you configured in interrupt_on. I
n that case, the invocation result will include an interrupt field with the actions that require review. 
You can then present those actions to a reviewer and resume execution once decisions are provided.













