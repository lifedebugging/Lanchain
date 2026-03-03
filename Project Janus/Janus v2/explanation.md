# Janus v2
Hey, new day it is and a right time to understand what changes has been made to *Janus v2*. If you ever wondered why it is called "Janus" then I want
you to keep wondering because I m gonna tell you about it in *Janus v3* or later.

*Janus v1* was a good start but it was incomplete in many ways to undestand what am I talking about, go and read *Janus v1* `explanation.md`, anyways
*Janus v2* was needed now it has a big advantage over v1 and that is new Janus has **tools** real time tools.

# Tools In Janus

Before MCP was introduced to me by me I was creating @tool which is all good and cool but it doesn't do anything in real time it does not have it's own server.

I am introducing Janus v2 with MCP tools and the very first tool I created is `datetime`. Yes, you can ask Janus for today's date or time given where you are it 
may give you right answer.

You see there are two way's to achieve tools in MCP before I explain that let's get a quick explanation about MCP.

MCP stands for *Model Context Protocol*. It is a robust moethod introduced in Langchain to connect external services to your or our model. 
Without it you would have to write your own configuration which is pain to deal with and prone to lot's of error. MCP provide a library called
`FastMCP` from fastmcp.server. This library does all the heavy lifting for you from creating session's to handling handshake with the client.

MCP has two ways to handle transport.
1. StreamingHTTP
2. stdio

To know more about MCP go to `MCP` folder in Langchain repo.

Note : I am using *stdio* transport approach in Janus and probably it will be like that in later version's as well.

# Standard Method

Creating MCP tool require's *client* - *server* method. In which `Janus_v2.py` is the client, client stays where your main model is defined.
Server can be anywhere in your system since we're working with *stdio* transport basically it's the server stays locally in your computer instead of internet. 

# The Twist

`janus-server.py` is our server where the mcp tools has been defined. Now here's the twist instead of using `FastMCP` library, I m creating tool with standard method, writing all the configuration by myself, why? Well it's not that I am ~~Masochist~~ who love to deal with syntax errors, 
It's because Janus is all about writng Native programming.

# The Reason

*Janus* is a project where I am going to write my own ways to do things the same way Langchain libraries handle model configuration, so far I a have:
1. My own multi model decision router.
2. My own mcp standard server that contain single tool for now.

*Janus v2* does not have very drastic changes yet but it finally has hand's now and it's not a just a useless bot anymore.

I m going to explain how `janus-server` work in great detail in MCP folder, so look forward to it.

# What's next?

*Janus v3* is already in production, it will have drastic changes. look forward to that as well.


