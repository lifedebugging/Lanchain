# Welcome again.
Note : This one is gonna long but hear me out it's worth the pain.

# Manual ReAct

We have already talked about ReAct pattern in detail while we were creating our first basic agent but bruh here's the recap anyway.
> Reason + Act : Agents iteratively reason about what to do, acting by using tools, observe results, and repeat until they have the answer.
It's the simple and common chain pattern of agents to solve complex problem. Standard LLM's are not capable of doing that only agents can pull this kind of thinking process.

We will solely focus of `manual_ReAct.py` to understand **under the hood** of agents.

Sit tight open the code block and read this side by side by the end of this explanation you will have a solid grasp of how agents work(no money back guarrantee).

Importing required functions and libraries as ususal except this time we are importing one extra function  called `ToolMessage` from `langchain.messages`

creating Pydantic input class called `CalInput` 

using `@tool` to create tools. Here are two tools being created:

1. `calculator` function with string as an expression input.

Look at `eval(expression, {__builtin__ : {},{}}` eval() is a python function that takes a string and executes it as python code.

but why do we in need this at first place? 

Well to answer we have to take another boat, think of that statement as restriction access, it is the jail cell for the code.

You see *eval* is not just a function it's the *interpreter* python itself when you run the python_script.py.
      
     (1) python read the file
     (2) Convert it to a machine instructions
     (3) executes it (evaluate)
     
*eval* function exposes the 3rd step, a mini-python inside a python that's why it has a **exact same permissions** as the python.

So, what? Why is it needed in our code?

`def calculator(expression : str) -> str:`

The calculator function takes *string* as an input, why not int? Well to avoid built in operator conflict.

So, when you pass "4+4" (string) eval take the string and execute it.

If you pass `eval("__import__('os').system('rm -rf /')")`, it deletes your hard drive. Because *eval()* doesn't care about that the function is named
"calculator" it executes whatever you pass it.

    Note : DO NOT RUN THE FUNCTION


So, that's where the role of `__builtins__` come in play. This module contains all the basic functions you use in python without importing them.
    
    1. print()
    2. __import__()
    3. len()
    4. open(), etc..
      
   When you run the python script, `__builtins__` function is already is available in background for use.

When we do {__builtins__ : {}}, we're restrcting access of those built in functions and isolating {__builtins__ :{}} in {} followed by comma.


2. `is_prime` tool it's a simple and smart way to check if the result is prime number. If you don't understand it feel free to beg me I might just explain it to you.

`def run_react_loop(query: str, tools: list, max_iterations: int = 5):`

Takes two argument, `query` as a *str* and `tools` as a *list*

After that we call our model,

Then saving tools name and their function in a dictionary {key : value} format.
By doing `tools_by_name = {t.name: t for t in tools}` to allow the function to access tools, this all happens behind the scene of `create_agent` or
`create_agents_with_tool` function, we're hard coding it in our function because hey that's what it means to create manual agent right?

After that we bind the model with tools using `bind_tools()`

Create messages with `HumanMessage`

And finally our iteration start with `in range`  because we can't have our model infinite looping hence (max_iterations = 5)

Then we *invoke* our model
and `append` the response back to *messages*
because we need the llm to know it's result for the iteration.

step - 2 is we check if there are tool calls with `if not` response.tool_calls, here tool_calls is just a list of tools in dictionary format it contain
three important information about each tools inside tool_calls in response

       1. name of the tool, tool_calls['name']
       2. input of the tool, tool_calls['args']
       3. id of the tool, tool_calls ['id']

If there is no tool call meaning llm did not called any tool at all it solved the problem by itself so we print("no tools were called") and the output.

Moving on if there's any tool call we iterate over it as well assuming there are multi tools in use.

Using `for` loop iterating over `tool_calls` 

We get tool_call['name'] saved in tool_name variable and tool_call['args'] (input to the tool) in tool_args variable.

Next we execute the tool:

`tool_result = tools_by_name[tool_name].invoke(tool_args)`

look at tools_by_name[tool_name] this is why we created `tools_by_name` earlier in our loop.

Because if you pass calculator.invoke() pr "calculator".invoke or if tools_by_name was just a string containing the name of tools in string format "calculator"
it would not be able to invoke anything you will get an error because python can't access the tool *calculator*.

Hence doing `tools_by_name = {t.name: t for t in tools}` is actually creates a **dictionary: {'calculator': <calculator_func>, 'is_prime': <prime_func>}**.

# The concept is called "The Look up" table

t for t in tools

     "for t in tools": Go through your list of tools one by one. Let's call the current item t.
     "t.name": Look at t and get its name (e.g., "calculator").
     "t": Just take t itself (the whole function object).


that's it then we just print the result of `tool_result` and append the result again to `messages` for iteration.

Using `ToolMessage(content=str(tool_result), tool_call_id["id"])` here we use `ToolMessage` basically saying "hey llm take this response as a *Tools message*" 
so it doesn't mistake the output as user output. Result as str and providing tool_call['id'] for the llm to know this output belongs to this tool to avoid conflict.

that's about it for tool iteration loop.

Last but not least our main() function providing list of tools and query for the input and printing the final output.

# Questions I asked myself

 1. Why model.bind_tools(tools) takes a List, not the Dictionary?

        The Logic: 

        bind_tools is a method created by LangChain/OpenAI. It is smart. You just give it the raw list of tools (tools).
        It looks inside the tools, reads their names and schemas automatically. It doesn't need your manual dictionary (tools_by_name).
        Why create the dictionary then?
         The Model (bind_tools) only needs to know the tools exist (to decide which one to pick).
         WE need the dictionary (tools_by_name) to actually run the code when the Model picks one. We can't run a function based on a string name "calculator" without a lookup table!
         

2. I tried print the `response.content` as an experiment after the first *llm.invoke()* but I got output as None it was an empty
   so, Why is `response.content` empty?

                This is the key to Agents. 

              When an LLM decides to use a tool, it stops talking. 

               Normal Behavior: You ask "What is the capital of France?" -> response.content = "Paris".
               Tool Behavior: You ask "Calculate 25*15" -> The LLM thinks "I can't do that, I need a tool." -> It fills out a Tool Call Request (JSON) -> response.content = "" (Empty).
     
               It puts all its energy into the response.tool_calls list. It has no text left for content because the "text" is the tool call. 


3. Why tools_by_name[...].invoke instead of llm.invoke? Which I alredy explained but I like this anology.

       Analogy: 

       LLM (llm.invoke): The Manager. He sits at the desk. He reads, writes, and decides.
   
       Tool (tool.invoke): The Worker (Calculator). He knows how to do math, but he can't read emails.
     

        The Flow: 

        We ask the Manager (llm.invoke) "What is 25 * 15?"
   
        The Manager says "I don't know. Let me ask the Worker."
   
        He creates a tool_call.
          
         Now we must talk to the Worker.
   
         If we use llm.invoke again, we are just asking the Manager again.
   
         We must use tool.invoke to actually run the math code.
          

        Why the dictionary?
   
        We only have the name "calculator" (a string). Python doesn't know which function that is. 
 
         tools_by_name["calculator"] finds the actual function in the dictionary.
         .invoke(...) runs it.
     
4.  Why str(tool_result) and tool_call_id?

           Why str():
    
          The LLM is a text-based creature. Even if your calculator returns the number 375 (Integer), the LLM prefers to read "375" (String). It avoids data type errors. 

         Why tool_call_id:
          Imagine the Manager sends out 5 requests at once. 

          "Calculator, do 2+2" (ID: #101)
    
            "Weather, get temp" (ID: #102) 

           When the results come back: 

         "The result is 4" -> Which request was this? If we don't attach ID #101, the Manager won't know if 4 is the sum or the temperature.
         The tool_call_id links the Answer back to the specific Question the LLM asked. 







     
     


