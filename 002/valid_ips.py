"""Prints out the valid IP addresses given an IP network."""

import ipaddress
import re
import sys


def print_ips(network_string):
    """Prints the valid IP addresses for the provided network, or a very
    forgiving error message."""
    pattern = re.compile(
        r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})$'
    )
    match = pattern.match(network_string)
    if not match:
        print(BAD_INPUT_MESSAGE)
        exit(2)
    numbers = [int(group) for group in match.groups()][:4]
    if any(num > 255 for num in numbers):
        print(GROUP_TOO_BIG_MESSAGE)
        exit(3)
    try:
        network = ipaddress.ip_network(network_string)
    except ValueError:
        print(MASK_OUT_OF_RANGE_MESSAGE)
        exit(4)

    # Otherwise, we're looking good!
    for address in network.hosts():
        print(address)


BAD_INPUT_MESSAGE = """
Your IP network isn't in the correct format.  The desired format follows
the pattern:

X.X.X.Y/Z

Where:

X is an integer between 0 and 255.
Y is an integer between 0 and 254.
Z is an integer between 24 and 32.
"""

GROUP_TOO_BIG_MESSAGE = """
One of your first three groups of digits was too large.  These three
values can be anything between 0 and 255 (8 bits), so if you had something
larger than 255 for these numbers (e.g. 123.456.1.0/24), that won't be valid.
"""

MASK_OUT_OF_RANGE_MESSAGE = """
Your network mask attempted to mask over already specified bits or was too big.

While IP addresses may look like a sequence of numbers less than 255, they're
really one long string of bits.  For instance, 192.168.0.1 is really:

    11000000 10101000 00000000 00000001

When you make a mask, you're telling it which numbers are locked down and
which numbers it is allowed to use as its network.  For instance, a mask
of 24 is the same as 24 1's or

    11111111 11111111 11111111 00000000

The network then knows that it has 8 bits to iterate through for its valid
hosts (256 values).  Thus, if you want to specify a starting IP address of
125.186.243.200 which is also written as

    01111101 10111010 11110011 11001000

then only the last three bits are left unspecified.  Therefore, only a mask
between 29 and 32 would be reasonable.
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} XXX.XXX.XXX.XXX/XX")
        exit(1)
    network_string = sys.argv[1]
    print_ips(network_string)
    exit(0)
