# Streamable-http

This is interesting so far I thought that creating custom server is all about **stdio** transport, I was learning and find it's just that creating 
custom server with **streamable-http** transport is easy as creating it with **stdio** transport.

# Points to note:
1. **Stdio** server is still most safe since you know it's running as a sub process.
2.  **stdio** is fast because there's no delay in client-server communication.
3.  **stdio** more reliable because if internet crashes and you go offline that's it for your custom server.

# Then why?
Personally, I cannot think of **streamable-http** transport uses in custom server, I mean sure if you have a dedicated that never goes offline or
if you want to share your "custom server" with the world so they can just fetch using internet.

# Code

    mcp.run(transport = "streamable-http")

Yes, this is the only difference between a **stdio** based and a **streamable-http** based server.

At the very end you define the method of transport to be used in your custom server that's it.

# Client side

        "myCalculator" : {
            "transport" : "streamable_http",
            "url": "http://localhost:8000/mcp"  #Remote docs server
            },

Well, you already know the client side since I m running it locally. It is running in port *8000*.
You just slap the url and boom it works.

 The only thing that bothering me is I don't have a **SSE port** control.

 As soon as I learn anything about it you will get an update. 

 Don't forget this is just the begining!


