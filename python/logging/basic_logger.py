import logging
import sys

formatter = logging.Formatter(
    fmt="[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(filename)s] [%(funcName)s():%(lineno)s] %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S")

hndl_console = logging.StreamHandler(stream=sys.stdout)
hndl_console.setLevel(logging.ERROR)
hndl_console.setFormatter(formatter)

hndl_file = logging.FileHandler("logfile.log", "w")
hndl_file.setLevel(logging.NOTSET)
hndl_file.setFormatter(formatter)

logging.basicConfig(
    level=logging.NOTSET,
    handlers=[
        hndl_console,
        hndl_file
    ]
)
logger = logging.getLogger(__name__)

logger.debug("we should see this only in the logfile")
logger.error("this one is also visible on the console")

