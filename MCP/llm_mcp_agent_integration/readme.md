# Structured Output Via MCP

It's been quite a while and I apologise for my absence lots been going on but I m back!

Today we are talking about structured output using MCP

# Difference
Usually when we talk about **Strucutred output** we think of *Pydantic* module and it's **BaseModel** integration.

The real difference would be where the data lives and how it is used.

**Pydantic** : Local code structure
1. Role : It is the local validator, it ensures that the data inside your script is correct. IF you try to put a string into an
`int` field, you get an error, ususally done by defining *class* and inheriting from *BaseModel*.

2. LLM visibility : The LLM does not "see the pydantic class directly. Instead the MCP SDK converts your
Pydantic class into a JSON schema so the LLM knows what format to follow.

3. Usage : Local to your code, generally used for serialization(turning objects into JSON) and 
desrialization (turning JSON back into objects).

**MCP** : Protocol standard
1. Role : It tells the MCP client *this specific part of the response is machine-readable data,
not just text for the LLM.*

2. LLM visibility : Usually, `StructuredContent` is hidden from LLM prompt but visible to **Application** i.e : the client.
This is why you can use it to to show UI elements.

3. Scope : Cross-plateform. It allows a server written in python to send data to a client written in TypeScript/React.

#The code 
Let's talk about the code and it's working.

``import``'s are in code make sure you import `MultiServerMCPClient` and `create_agent`

The only important thing we need to talk about is here:

    async with mcp_client.session("structured_data") as session:
          result = await session.call_tool("validate_tool", arguments={})

1. **async with** : It's the context manager for managing resources, ensures automatic clean up.

2. **mcp_client.session("strucutred_data")** : Look at the code in :

    mcp_client = MultiServerMCPClient({
        "structured_data": {...})}

Here inside `mcp_client` there can be more than servers to create connection with the specifc
server we use it's name hence *mcp_client.session* followed by : *("strucutred_data")*

3. **as session** : So you can use it to interact with the server.
Use session :

1. Direect control over a specific server connection.

2. To call tools directly on that particular server.

**result = await session.call_tool("validate_tool", arguments={})** :

Here we're using `call_tool` to invoke *specific* tool inside the MCP server and the name of the
tool is **Validate_tool**, where arguments={} refers to empty dictionary of arguments passed because no paramters or any value
needed for this tool. We storing the responsed from the tool in the `result` variable.

# Note
The LLM doesn't actually "see" `validate_tool`'s response during its reasoning. The agent uses
tools from `get_tools()` to answer the question. The `session.call_tools()` call happen after the agent completes.
It's a manual invocation. 

Check the `strurctured_mcp.py` for server script.

# Core lesson:
 MCP lets you give LLMs structured tool capabilities while also allowing you to leverage those same tools programmatically. You're not choosing one or the other—you can do both in the same flow.
