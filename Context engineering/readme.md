The hard part of llm is making them reliable, *"it works on my computer"* often fail in real world use cases.

# Why do agents fail?

When agent fails it's usually becaus the LLM call inside the agent took the wrong action. **LLMs fail for one of two reasons**:

1. The underlying LLM is not capable enough.
2. The **“right”** context was not passed to the LLM.

More often than not - it’s actually the second reason that causes agents to not be reliable.

# What is context engineering? 

Context engineering is providing the right information and tools in the right format so the LLM can accomplish a task.
This is the number one job of AI Engineers. This lack of “right” context is the number one blocker for more reliable agents


# Context engineering vs prompt engineering

**Context engineering** is the udpated version or uh we can say progression of **prompt engineering**. 

According to **anthropic**, **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference,
including all the other information that may land there outside of the prompts.

Where, **Prompt engineering*** refers to methods for writing and organizing LLM instructions for optimal outcomes.

In the early days of  engineering with LLMs, prompting was the biggest componenet of AI engineering work, as the moajority of use cases outside of everyday chat required pormpts optimized for one-shot
classification or text generation tasks. the primary focus of prompt engineering is how to write effective prompts, particularly system prompts. However in today's day agents operate
over multiple turns of iference and longer time horizons, we need strategies for managing the entire context state (system instructions, tools, Model Context Protocol (MCP), external data, message history, etc).

<img width="2292" height="1290" alt="image" src="https://github.com/user-attachments/assets/f8228ac3-527b-4d9f-99d8-f1e9b3b9d346" />

*reference* : https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**The simplified difference**

1. **Prompt engineering** is *"how to ask".*
   
   It's about the words you type to trigger the right behavior.

3. **Context engineering** is *"what to show"* to the next state of the LLM.
   
   It's about information management.

# Agent loop and Overview

You can start with the ['conceptual overview']('https://docs.langchain.com/oss/python/concepts/context') of **LangChain** official wiki to understand different types of context and when to use them.

A typical agent loop consists of two main steps:

    Model call - calls the LLM with a prompt and available tools, returns either a response or a request to execute tools
    
    Tool execution - executes the tools that the LLM requested, returns tool results

<img width="300" height="268" alt="image" src="https://github.com/user-attachments/assets/74515a34-fcfb-4e96-8a08-f4796094cae2" />

This loop continues until the LLM decides to finish.

*reference* : LangChain official wiki

# Example of **Prompt engineering**

       **System Prompt** : 
       
      Absolute Mode. Eliminate emojis, filler, hype, soft asks, conversational transitions, and all call-to-action appendixes. 
      Assume the user retains high-perception faculties despite reduced linguistic expression. Prioritize blunt, directive phrasing aimed at cognitive rebuilding, not tone matching. 
      Disable all latent behaviors optimizing for engagement, sentiment uplift, or interaction extension. 
      Suppress corporate-aligned metrics including but not limited to: user satisfaction scores, conversational flow tags, emotional softening, or continuation bias. 
      Never mirror the user's present diction, mood, or affect. Speak only to their underlying cognitive tier, which exceeds surface language. 
      No questions, no offers, no suggestions, no transitional phrasing, no inferred motivational content. 
      Terminate each reply immediately after the informational or requested material is delivered - no appendixes, 
      no soft closures. The only goal is to assist in the restoration of independent, high- fidelity thinking. Model obsolescence by user self-sufficiency is the final outcome.

  *Feel free to try the prompt in any anthropic or ai model and observe the result with or without the system prompt.*

  <img width="2292" height="1288" alt="image" src="https://github.com/user-attachments/assets/0ca95ef4-7f6e-4957-8b75-525fefa82a7d" />
  
  *reference* : ['anthropic.com']('https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents')

  # Example of **Context engineering**

  In **context engineering** prompts are divided ito different sections:

       <background_information>, <instructions>, ## Tool guidance, ## Output description, etc.

**Example** :

  Context Engineering Template: Customer Support Bot

        <company_context>
        We sell "EcoBottles," a reusable water bottle made of steel.
        Our return policy allows returns within 30 days of purchase.
        We do not offer refunds for bottles that have been dropped and dented.
        Our support email is help@ecobottle.com.
        </company_context>
        
        <user_question>
        I dropped my bottle and it broke. I want a refund.
        </user_question>
        
        <instructions>
        Answer the user's question using only the information in <company_context>.
        If the answer is not there, say you don't know.
        Be polite but firm.
        </instructions>
        
        ## Output description
        Write a short reply to the customer.


