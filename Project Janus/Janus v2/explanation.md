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


