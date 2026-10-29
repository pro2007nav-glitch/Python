
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logging.debug("This is a debug message")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("Critical error detected")

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Exception occurred during division")

print("Logging demonstration completed")
