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


# 9/2/26

After experimenting BaseModel and sturucutred output I realiased that AI models love to guess. 

Look at `BaseModel-experiment.py`

There are few changes:

Instead of One, there are two Classes and a dynamic input text so knock yourself out and try the prompt.

It guesses some things like Car and food, while the name and age is must given as input, ofcourse you can choose not to and see what happens.
There is a `ValueError` at work in age `Field`

Below are the inputs and outputs of the  `BaseModel-experiment.py`

Input :  `I like fast cars and non spicy food the name is Sam turned 21 this year and age for you to guess.`

(ofcourse it's not me)

Output : 

```
Name : Sam
Age : 21
gender : Male
tone : Casual
car : BMW M3
food : Aloo Paratha

```

According to what I was expecting the car is pretty darn accurate I like BMW M3 infact I love it and the food as well.
However I have seen the food were either "Aloo Paratha" or "Paneer Butter Masala" for the input  `non spicy food`.

That said what I know so far is:
1. LLMs reflect majority patterns.
2. “Common” beats “creative” unless you force diversity.

Try this prompt:

`“Guess a food an Indian person might like, but avoid common Indian dishes.”`

You’ll see it struggle.


# 10/2/26

`advanced_pydantic.py`

Output:
```
Company : Microsoft Corporation
Industry : Technologia
Employees_count : 220000
Location : One Microsoft Way, Redmond, USA
Public : True
```

More sophisticated schemas with nested objects, enums.

Using nested models : Defining `Address` and using it inside `Company`

Using Literal types for **enum** like constraints

Python validate types automatically

Accessing nested data via dot notation like `result.headquarters.city`

From this point onwards I will be using Pydantic BaseModel for the strucutred_output because reliable data is important.

Ofcourse, this is not the end I have few mini projects in mind I will be posting soon.

Thankyou.






