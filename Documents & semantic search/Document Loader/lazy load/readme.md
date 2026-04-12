# Output  
```
First_name: first
Last_name: last
First_name: Edna
Last_name: Moss
...
```
**All the rows get printed.**

# lazy_load

lazy_load is a generator used for streaming document lazily or large datasets, for production.

# What happens when you call `lazy_load()?`

`print(loader.lazy_load())` <- This will print the generator object.

**To print content of lazy_load** you have to iterate over it.

```
for doc in loader.lazy_load():
    print(doc.page_content)
```


