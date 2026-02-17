*2/17/26*

Today we're talking about Agents. Yeah,  agents in `Langchain` not MIB agents.

# Agents
Before I explain anything look at the picture down below:
![Uploading llm-vs-agent.png…]()

*Reference : Microsoft/langchain-for-beginners*

An **Standard LLM** is good for expremient, local chat and simple factual question (depending on how frequent upto date it's knowledge base is).
Where An Agent has many advantages over **standard LLM**.

Before we talk about an  LLM `agent` advantages. We need to answer what is agent anyway?

An Agent is LLM in steroids. An agent is an LLM impowered with tools.

To understand what that means, here's the anology:

> Tony Stark (Standard LLM): He is genius, he knows everything, he can solve math problems, write poetry about his assitant and answer almost any question. But he can't fly because he's just a man.

> Iron Man (Agent with tools): Tony Stark + The suit(tools) now he can fly. fire missiles and talk to Jarvis from anywhere like making an external  connection using his suit(tools).

In short, what makes an Agent better from Standard LLM is it's *ability to use tools* which allow it to access real-time data and take actions, while standard LLMs are limited to their training data.

 Standard LLM: Input -> Process -> Output. (One shot).
 
 Agent (With Tools): Input -> Think -> Act -> Output.

 Agents follow this iterative loops also called (**ReAct Pattern**):
 
1. Thought: What should I do next?
2. Action: Use a specific tool
3. Observation: What did the tool return?
4. (Repeat 1-3 as needed)
5. Final Answer: Respond to the user

A question that I m going to answer free of charge. What is an Agent without tools?

The answer is: functionally it's like an *Standard LLM*, however it will still try to think or reason but since it has no tools it will fail and fall back to *guessing*.

That's all about for an agent introduction.

I have created a simple agent check out `basic-agent.py`

Here we import an specfic function `create_agent`

> from lagnchain.agents import create_agent

In standard LLM we used to `invoke` our model directly but while creating agent first we call our model inside an agent.

```
agent = create_agent(
model = ...,
tools = [],
..
)
```
Yup that's it, that create our agent now we just *invoke* the agent. While invoking an agent it's always best practice to use  dictionary 
{key : pair} format, check out code for more detail.

Before we move forward to `state_full_agent.py` let's talk more about `create_agent()` - first of all it's an high-level API that handle the ReAct pattern automatically. This is the *recommended approach* for building production agents.

But I second that, why you ask?

Because Langchain is too linear A -> B -> C

While `create_agent` is the ""langchain way"".

LangGraph is the ""Modern Industry way""

Langchain agents are too rigid for a loop, modern agents should be able to self repair, self prompting which requier cyclic loop. That's where LangGraph shines bright.

LangGraph is an Langchain in steriods. What does that even mean? 

That's for another day!!

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Continue to `state_full_agent`


