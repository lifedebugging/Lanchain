# Multi tools

Multi tools are helpful based on your model capabilities it can also anchor the judgment of your model if you try to use lots of tools. Model hallucinates unable to decide which tool to use.

The tools are great for multiple questions like in my code I am asking math, factual and a forcast question at once.

Before this I've been using 20-b model which is a small model and gave me hard time calling tools. Ending up in lot's of `Error : 400`. I managed to get tools through **prompting** 
forcing model to choose tool to answer my questions however I finally decided to change the model still free but better.

Currently I m using `llama-3.3-70b-versatile` which I still have long way to test it limits.

The second best part is **"asynchronous version of multi tool calling"** I managed to write a fine asynchronous call for multi tools. 
Simple as using `asyncio.gather` The performance is **3x Faster** the answer is printed quite different but yeah it is faster.

I made the tool slept for 1 second each, but it happens fast in asynchronous code because of it's parallelism.

Think of it like:

Slept for 1 second, in the old code, 1 second + 1 second + 1 second = 3 seconds.

In the new code, the 1 second happens simultaneously.

Output of asynchronous multi tool:

```
Query : what is 353*464-353, use calculator tool to solve?
 Tool : calculator
Query : what is the capital of France?, use search tool to answer
 Tool : search
Query : what's the weather in Tokyo?, use get_weather tool to answer
 Tool : get_weather
163439
Result of the capital of France : 
Weather in Tokyo : 72 degree, sunny
```
