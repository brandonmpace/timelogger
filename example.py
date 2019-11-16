# Set up your root logger, or use logcontrol
import logcontrol

# Import the package
import timelogger

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
