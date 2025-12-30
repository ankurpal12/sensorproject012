import logging # it used to keep track of the events log messages that happen during the execution of a program.
import os # it provides functionality to read and write to file system.
from datetime import datetime # it provides functionality to work with date and time.

LOG_FILE = f"{datetime.now().strftime("%d_%m_%y_%h_%m_%s")}.log" # here we are creating a log file with current date and time.

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # here we are creating a path for the log file in the logs directory.
# here we mention how our logpath will look like.
# getcwd() function returns the current working directory of a process.
# os.path.join() function joins one or more path components intelligently. & add 'logs' mention by us with LOGS_FILE.
os.makedirs(logs_path, exist_ok=True) # here we are creating the logs directory if it does not exist.
# exist_ok=True means that if the directory already exists, do not raise an error.


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # here we are creating the full/final path for the log file.

logging.basicConfig(
    filename=LOG_FILE_PATH, # here we are specifying the log file path.
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # here we are specifying the format of the log messages.
    level=logging.INFO, # here we are specifying the log level.
# (lineno)d - to log the line number where the log message is generated.
# (name)s - to log the name of the logger.
# (levelname)s - to log the level of the log message.
# (message)s - to log the actual log message.
)   