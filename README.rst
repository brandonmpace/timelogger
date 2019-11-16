**timelogger:** A stopwatch-like time logger for Python programs

It provides:  
  * Tracking time spent throughout a program in a method similar to a stopwatch
  * Output via standard Python logger for simplicity

Original use case:  
  * Python program containing many packages and modules
  * Needed ability to log time gaps in a centralized way.

    * e.g. time consumed for imports or function calls
  
Installation:  
  * pip install timelogger
  
    (Tested for Python >=3.6.5 on Linux (Ubuntu) and Windows 7/10)

Usage:
    * short example::

        # Set up your root logger, or use logcontrol
        import logcontrol

        # Import the package
        import timelogger

        # Customize the package logger, if needed
        logcontrol.register_logger(timelogger.logger, "timelogger")
        logcontrol.set_level(logcontrol.DEBUG, group="timelogger")
        logcontrol.log_to_console(group="timelogger")

        # Add a start time with a relevant name
        timelogger.start("imports")

        # imports of other packages for example purposes
        import binascii
        import decimal
        import hashlib
        import requests

        # To log the time differential, set a stop time for the same name
        timelogger.stop("imports")

        # To set a specific log level for the time differential logs: (default is logging.INFO)
        timelogger.set_log_level(logcontrol.DEBUG)


