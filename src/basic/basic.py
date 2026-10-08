#!/usr/bin/env python3

"""
Description.

The script presented here is a simple Nagios check example, employing a set of
utility functions to guarantee accurate output and exit codes. Although this
version uses fixed values, suitable for straightforward checks, we also offer a
more sophisticated variant that demonstrates how to handle command-line
arguments for more elaborate or flexible scripting.
"""

import random  # Only required for the template demo - can be removed
import sys
from typing import NoReturn


def main() -> NoReturn:
    """Run the sample check against hard-coded warning and critical levels."""
    critical_level = 90
    warning_level = 75

    test_value: int = random.randint(1, 100)  # nosec B311

    if test_value >= critical_level:
        handle_critical(f"Test Value = {test_value}")
    elif test_value >= warning_level:
        handle_warning(f"Test Value = {test_value}")
    elif test_value >= 0:
        handle_ok(f"Test Value = {test_value}")
    else:
        handle_unknown(f"Test Value = {test_value}")


# -------------------------------------------------------------------------------- #
# STOP HERE!                                                                       #
# -------------------------------------------------------------------------------- #
# The functions listed below are integral to the template and do not necessitate   #
# any modifications to use this template. If you intend to make changes to the     #
# code beyond this point, please make certain that you comprehend the consequences #
# of those alterations!                                                            #
# -------------------------------------------------------------------------------- #


def handle_ok(message: str = "") -> NoReturn:
    """Print an OK line when a message is given, then exit 0."""
    if message.strip():
        print(f"OK - {message}")
    sys.exit(0)


def handle_warning(message: str = "") -> NoReturn:
    """Print a WARNING line when a message is given, then exit 1."""
    if message.strip():
        print(f"WARNING - {message}")
    sys.exit(1)


def handle_critical(message: str = "") -> NoReturn:
    """Print a CRITICAL line when a message is given, then exit 2."""
    if message.strip():
        print(f"CRITICAL - {message}")
    sys.exit(2)


def handle_unknown(message: str = "") -> NoReturn:
    """Print an UNKNOWN line when a message is given, then exit 3."""
    if message.strip():
        print(f"UNKNOWN - {message}")
    sys.exit(3)


# -------------------------------------------------------------------------------- #
# The Core                                                                         #
# -------------------------------------------------------------------------------- #
# This is the central component of the script.                                     #
# -------------------------------------------------------------------------------- #


if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------------- #
# End of Script                                                                    #
# -------------------------------------------------------------------------------- #
# This is the end - nothing more to see here.                                      #
# -------------------------------------------------------------------------------- #
