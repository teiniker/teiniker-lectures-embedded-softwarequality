# Logging

Logging is a very useful tool in a programmer’s toolbox. It can help you develop 
a better understanding of the flow of a program and discover scenarios that you 
might not even have thought of while developing.

By logging useful data from the right places, you can not only debug errors easily 
but also use the data to analyze the performance of the application to plan for scaling
or look at usage patterns.

# Python logging Module

``` 
import logging
``` 

The **logging module** in Python is a ready-to-use and powerful module that is designed 
to meet the needs of beginners as well as enterprise teams. 
It is used by most of the third-party Python libraries, so you can integrate your 
log messages with the ones from those libraries to produce a homogeneous log for your application.

By default, there are **5 standard levels** indicating the severity of events. 
Each has a corresponding method that can be used to log events at that level of severity.
The logging module provides you with a default logger that allows you to get started without 
needing to do much configuration.

The defined levels, in order of increasing severity, are the following:
* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`
* `CRITICAL`

By **default**, the logging module logs the messages with a severity level of **WARNING** or above. 

We can use the `basicConfig()` method to configure the logging.
Some of the commonly used parameters are the following:
* `level`: The root logger will be set to the specified severity level.
* `filename`: This specifies the file.
* `filemode`: If filename is given, the file is opened in this mode. The default is a, which means append.
* `format`: This is the format of the log message.


## References
* [YouTube (Schafer): Logging Basics - Logging to Files, Setting Levels, and Formatting](https://youtu.be/-ARI4Cz-awo)
* [YouTube (Schafer): Logging Advanced - Loggers, Handlers, and Formatters](https://youtu.be/jxmzY9soFXg)

* [Logging in Python](https://realpython.com/python-logging/)
* [Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
* [Logging facility for Python](https://docs.python.org/3/library/logging.html)

*Egon Teiniker, 2020-2022, GPL v3.0*
