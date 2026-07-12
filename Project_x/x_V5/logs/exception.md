python has capability to raise exception when errors occur



but what is exceptions



they're just errors detected during execution so we call them exception like yk this one is exception



when exception occur python stops running the code and looks  for a special block of code (a try/ except block) to handle error. 



# some common errors:



finenotfounderror, when trying to open a file that doesn't exist



fix? probably check the URL or the location see if it is correct



valueError occurs when trying to convert a string into an integer when the string does not represent a number.



fix? check your data, inputs





INdexError: Occurs when you trying to retrieve an element from a list with a non existing index



fix? check your indexing if it's a list or not, your conditional logic





there are many more exception, also python gives you the ability to create your own exceptions if you need custome behavior.







Errors detected during execution are called exceptions and are not unconditionally fatal.





# Explain the code:



create a function wit log\_level and log\_dir set 

def setup\_logging(log\_level: str = "INFO", log\_dir: str = "logs"):



create directory if not created

os.makedirs(log\_dir, exist\_ok=True)




```
log\_file = os.path.join(

     log\_dir,

     f"app\_{datetime.now().strftime('%Y-%m-%d\_\_\_%H-%M-%S')}"
```


This is building the log file path os.path.join combines the directory + filename. The filename is just app\_ + current datetime as a string  so each time the app starts, it creates a new log file with a timestamp in the name.

Like: logs/app\_2026-06-29\_\_\_14-30-00.log


# rotating file handler

```
file\_handler = RotatingFileHandler(

       log\_file,

       maxBytes=10 \* 1024 \* 1024,

       backupCount=5

```



The RotatingFileHandler is a type of logging handler provided by Python’s logging module.

It is designed to manage log files by rotating them based on predefined criteria, such as file size or a specified interval. This handler is particularly useful for applications that generate a large volume of log messages, as it helps prevent log files from growing indefinitely and consuming excessive disk space. 



The RotatingFileHandler is typically used in scenarios where continuous logging is necessary, such as in web servers, long-running services, or batch processing applications.


```
file\_handler.setFormatter(logging.Formatter('%(message)s'))
```


In Python logging, formatters are used to specify the layout and structure of log messages. They allow developers to customize the appearance of log entries by defining the format of timestamps, log levels, log messages, and additional metadata. Python’s logging module provides a variety of built-in formatters, and developers can also create custom formatters to suit their specific logging requirements.





When you define a format string like format='%(message)s', you tell Python to strip away all metadata (like timestamps or log levels) and log only the raw message



The default format :
```




BASIC\_FORMAT = "%(levelname)s:%(name)s:%(message)s"  
```


next is 

# conosle handler
```
   stream\_handler = logging.StreamHandler(sys.stdout)

 stream\_handler.setFormatter(logging.Formatter('%(message)s'))

```

sends logging output to streams such as sys. stdout, sys. stderr or any file-like object (or, more precisely, any object which supports write() and flush() methods).





All loggers are descendants of the root logger.

New loggers are created with the getLogger() function.





# next is 
```
root\_logger = logging.getLogger()

root\_logger.setLevel(getattr(logging, log\_level.upper()))
```

root logger is a parent of every logger

it cannot be assigned a null level.

since root logger cannot have a parent,

That’s the logger used by the functions ``debug(), info(), warning(), error() and critical()``


# Removing duplicate handler
```
for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)

```

What happens if setup_logging() gets called twice — like during testing or a hot reload?

The root logger already has handlers attached from the first call. Second call adds the same handlers again. Now every log record gets written twice — two lines in the file, two lines in the terminal.

The remove loop clears whatever's already there before adding fresh ones. Clean slate.


```
structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.CallsiteParameterAdder,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt='iso'),
            structlog.processors.StackInfoRenderer,
            #Formats it to a flat string like the standard library would on the console.
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer()
        ],
    
```

Struct log configure:
remember order matters

```
wrapper_class=structlog.stdlib.BoundLogger,
context_class=dict,
logger_factory = structlog.stdlib.LoggerFactory(),
cache_logger_on_first_user=True
```

The `stdlib` part means it delegates actual output to Python's standard logging under the hood. 
That's the bridge between structlog and stdlib.
`BoundLogger` is the obeject you get from get_logger() 

`context_class=dict` — correct, plain dict for storing bound context.

`cache_logger_on_first_user=True`

is for caching, you dn't intialize the instance for 1000 calls, instead you return cached instance

# function
```
def get_logger(name: str) -> structlog.BoundLogger:
```

A `boundlogger` is the centerpeice of structlog. It’s what you get back from `structlog.get_logger()`

 and it’s called a bound logger because you can bind key-value pairs to it.
(like user ID, session ID etc) once
and then automatically include them in every subsequent log line.

how do i inspect what's inside boundlogger?

You can inspect a context of a bound logger by calling structlog.get_context() on it.

 there's no reason to re-initialize them on every call.
```
logger = get_logger("app")

bound_logger = logger.bind(session_id=thread_id_str, user_id = "user_0")
```
simply call the function pass the string argument

but what is `bind`?

bind() returns a new logger with the context embedded.
The original logger is unchanged. 
This immutability makes bound loggers thread-safe — no shared mutable state.



# QUestions
q- Should I really NEVER use the root logger?



You should absolutely use the root logger if it’s useful — but you should definitely understand the consequences when you do, and why it’s useful. A great reason to change or use the root logger is if you need to understand what a third party package is doing as you’re using it.



"that's why in sturctlog I m using rootlogger"





q- what is logging?



Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.





q - when to use logging?



You can access logging functionality by creating a logger via logger = logging.getLogger(\_\_name\_\_), and then calling the logger’s debug(), info(), warning(), error() and critical() methods.



A very simple example is:



import logging

logging.warning('Watch out!')  # will print a message to the console WARNING:root:Watch out!

logging.info('I told you so')



q - how do you log to a file?



import logging

logger = logging.getLogger(\_\_name\_\_)

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

logger.debug('This message should go to the log file')

logger.info('So should this')

logger.warning('And this, too')

logger.error('And non-ASCII stuff, too, like Øresund and Malmö')



A very common situation is that of recording logging events in a file

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)



q - what about variable data how do you log them?



To log variable data, use a format string for the event description message and append the variable data as arguments.





import logging

logging.warning('%s before you %s', 'Look', 'leap!')



will display:



WARNING:root:Look before you leap!



&#x20;merging of variable data into the event description message uses the old, %-style of string formatting.



q - then how to display date/time in messaeges?



To display the date and time of an event, you would place ‘%(asctime)s’ in your format string:



import logging

logging.basicConfig(format='%(asctime)s %(message)s')

logging.warning('is when this event was logged.')



which should print something like this:



2010-12-12 11:41:42,612 is when this event was logged.



Note: The default format for date/time display (shown above) is like ISO8601



If you need more control over the formatting of the date/time



"provide a datefmt argument to basicConfig"



logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



which would display something like this:



12/12/2010 11:46:36 AM is when this event was logged.


q - tell me more about logger object


1. Note that Loggers should NEVER be instantiated directly, 

&#x20;  but always through the module-level function *logging.getLogger(name)* 

2\. Loggers that are further down in the hierarchical list are children of loggers higher up in the list.

 given a logger with a name of foo, loggers with names of foo.bar, foo.bar.baz, and foo.bam are all descendants of foo

3. all loggers are descendants of the root logger

q - how do use module level logger?

A good convention to use when naming loggers is to use a module-level logger

logger = logging.getLogger(\_\_name\_\_)

This means that logger names track the package/module hierarchy


q- how do you set destination for any logging messages?


destination are served by handler classes.

you can write messages to  files, HTTP GET/POST locations, email via SMTP, generic sockets, queues, or OS-specific logging mechanisms such as syslog

also You can create your own log destination class

Note : By default, no destination is set for any logging messages.

You can specify a destination (such as console or file) by using basicConfig()


If you call the functions debug(), info(), warning(), error() and critical(), 

they will check to see if no destination is set; and if one is not set, 

they will set a destination of the console (sys.stderr)



q- how to setup a unique thread_id tied to your log
