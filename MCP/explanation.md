# MCP (Model Context Protocol)

A long awaited Module I wanted to learn, I might get carried away with explanation because this is the real deal.

Starting with `firstmcpclient.py` It's the first client I created using mcp. It uses `MultiServerMCPClient` from `langchain_mcp_adapters.Server`.

Also we will be using lot's of Async function, creating coroutines and await fetching. Because you know MCP is all about tool fetching detail in real time hence we using *Async* function 
in every mcptool.

It is pretty simple though since this is our first time we are using url and only creating client, so in the code as you can see
we pulling server from `mcp_server_url`, creating client, fetching tools from the server and using agent to *invoke* it. That's it you see, pretty easy right?

Well it's not now let's dive deeper about what is MCP anyway?

MCP stands for *Model Context Protocol*, this is where you use the real tool in your model or agent, basically MCP is a stndardized way for AI agents to
connect tools, you can't connect to external services without MCP I bet.

Why MCP though?

Well think of MCP like a translator or a middle-man who can talk to any tools written in any language. Yes you heard me right, you can write the *server* side of the 
tools in **Java** and I can write *client* side in Python.

let's recall: 

            1. One standard protocol.
            2. Unified approach.
            3. Quicker to add services.


Now, MCP has two way to handle tool calls or **transport**
1. HTTP transport
2. stdio Transport
   
<img width="1536" height="778" alt="image" src="https://github.com/user-attachments/assets/7dc73bff-5109-4f03-abd9-e8c91d0d0277" />
*refrence* : Microsoft github post langchain for beginners.

What you're seeing in `firstmcpclient.py` is HTTP transport approach, server lives on the internet we fetch the URL and pass it to the config.

The pattern is always:

            1. Identify the URL: Where is the server?
            2. Identify the Transport: How do we talk to it? (streamable_http is best for web).
            3. Pass the Config: Feed it into MultiServerMCPClient.
            
**Note** : It's not the same with the *stdio Transport* approach

*stdio* transport approach is for local services, the server sits on your machine along with your client and model. This is what we will be 
focusing on the most.

In *stdio* approach you have to write your own server and client, it create's a subprocess in your CPU which then allow talking to client.

Advantages of *stdio* :

             1. NO latency, crazy fast like Flash because it is inside your system.
             2. More secured compared to HTTP transport.
             3. Requires no internet connection for the server - client communication.
             4. Standard way in to create production ready servers and client.

`mcpwithstdio.py` uses stdio aproach, since it's only a client script it won't do anything at all, it's just a *prototype*. 
```
client = MultiServerMCPClient({
        "localCalculator" : {   #servername
            "transport" : "stdio", #local subprocess, not http
            "command" : "python",        #Tells your computer to start the Python interpreter.
            "args" : [str(Path(__file__).parent / "servers" / "stdio_calculator_server.py")]
        }
    })
```
Look at this piece of code block, Starting with very first is the servername or serverID, it can be anything **"batman"** as well.

`"transport" : stdio` is what allow client to know the type of transport you change it to `"transport" : "streamable_http"` for http transport.

`"command" : "python"` this is where it get's interesting, remember I told you we can write server in Java and client in Python,
this is where you tell the cient to start the interpreter based on **what language server is written on**.

`"args" : "path_to_you_server"` here you write the *absolute path* to your server, if it's in different folder or *relative path* if it's in the same folder.
I say get used to writing *absolute path* because while creating production ready projects you will have server in different folder's to keep the server and client sorted.

Now both transports can:

        ✅ Authenticate users (Streamable HTTP: tokens/keys, stdio: subprocess credentials)
        ✅ Access network resources (Streamable HTTP: directly, stdio: subprocess can make network calls)
        ✅ Be used in production (choice depends on architecture and needs)


