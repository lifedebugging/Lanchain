**Template-Based Translator**

This is a small translator project built using *langchain* to explore how prompt templates work.

Instead of hardcoding translation logic, the behavio is defined using a *prompt template*.
The same template can be reused for different languages and input just by changing variables.


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/54c3cc5d-0742-424c-a568-52f8d23913a5" />


Templates work like *fill-in-the-blanks*:
1. Create a template once with placeholders ({name}, {value}).
2. Reuse it with different values.
3. Perfect for consistent, repeatable prompts.


Example code : ``Template.py``

Expected output : 

```
french: Bonjour, comment allez‑vous ?
Russian: Привет, как дела?
```

Makes changes to ``input_language``,``output_language``,``text`` in the ``Template.py`` to translate different languages.

```
  result1 = chain.invoke({
        "input_language": "English",
        "output_language" : "French",
        "text" : "Hello, how are you?",
    })
```
