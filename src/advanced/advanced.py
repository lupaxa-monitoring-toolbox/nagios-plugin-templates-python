#!/usr/bin/env python3

"""
Description.

This Nagios check script serves as a more sophisticated example that uses
utility functions to guarantee the accuracy of the output and exit code.

Unlike the basic version, this one utilizes command-line parameters to override
the default hard-coded values, thereby enabling more advanced or portable
scripting. Nevertheless, we also supply a basic version suitable for checks that
don't demand parameters.
"""

import argparse
import random  # Only required for the template demo - can be removed
import sys
from typing import NoReturn


def main(options: argparse.Namespace) -> NoReturn:
    """Run the sample check against the warning and critical levels."""
    test_value: int = random.randint(1, 100)  # nosec B311

    if test_value >= options.critical_level:
        handle_critical(f"Test Value = {test_value}")
    elif test_value >= options.warning_level:
        handle_warning(f"Test Value = {test_value}")
    elif test_value >= 0:
        handle_ok(f"Test Value = {test_value}")
    else:
        handle_unknown(f"Test Value = {test_value}")


def process_arguments() -> NoReturn:
    """Read warning and critical levels, then run the check."""
    parser = argparse.ArgumentParser(
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-c",
        "--critical",
        help="Critical level",
        type=float,
        dest="critical_level",
        default=90,
    )
    parser.add_argument(
        "-w",
        "--warning",
        help="Warning level",
        type=float,
        dest="warning_level",
        default=75,
    )

    options = parser.parse_args()

    if options.warning_level >= options.critical_level:
        handle_unknown("Warn level MUST be lower than Critical level")

    main(options)


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
    process_arguments()

# -------------------------------------------------------------------------------- #
# End of Script                                                                    #
# -------------------------------------------------------------------------------- #
# This is the end - nothing more to see here.                                      #
# -------------------------------------------------------------------------------- #
