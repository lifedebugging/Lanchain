# Structured output

Structured output is something that use less **tokens**, make it more human readable and asthetic presentable.

You see there are two ``code.py`` in the folder. Both provide the same result.
```
Output :
Name: Sam  
Age: 20  
Occupation: assassin 
```
However I want you to notice the difference in those two block of codes. You will see that in `code1.py` the strucutred output is achieved by using a **prompt** where the `code2.py` does that by 
using `Pydantic` framework it import `BaseModel` and allow user to define a Class/function to create an strucutred output as we please.

The question is which one should you use?

Well, that depends on usecases ofcourse the `code2.py` is more reliable because it has well defined a class/function for the strucutred output.
Prompt is fine for experiment but you will be using something like a Template or Pydantic framework for Custom models where you need the output in specific way.

I will be updating this folder with more ways to achieving the same result. 

Stay tuned!
