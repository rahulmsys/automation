from pathlib import Path
from behave import given
from behave import when
from behave import then
from behave.runner import Context
import logging

logger = logging.getLogger(__name__)


@given("the file exists")
def step_impl(context: Context):
    logger.info(f"Touching file")
    context.file.touch()


@when("I append a line to the file")
def step_impl(context: Context):
    logger.info(f"Appending a line to file")
    context.appended = "Test line appended\n"
    with open(context.file, mode="a") as f:
        f.write(context.appended)


@then("the line appears at the end of the file")
def step_impl(context: Context):
    logger.info(f"Checking if line was appended")
    with open(context.file, mode="r") as f:
        for n, line in enumerate(f, start=1):
            logger.info(f"Line {n} is {line}")
        logger.info(f"Last line is '{line.strip()}'")
        assert line == context.appended
