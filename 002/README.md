# Day 002 - A Forgiving IP Network Checker

## The Original Challenge

Write a script that takes in an IP network specification (of the form "XXX.XXX.XXX.XXX/XX") and prints out the valid IP addresses in that network.

[Example Solution](https://github.com/pybites/100DaysOfCode/blob/master/002/get_ips.py)

## Extra Challenge

Make this script have super helpful error messages that teach a beginner user about IP address spaces and IP networks and masking.

Possible example usage

    $ python valid_ips 123.123.123.0/24
    123.123.123.1
    123.123.123.2
    ...
    123.123.123.254

    $ python valid_ips 999.999.999.0/24
    Invalid network.  (Your extremely insightful help message here...)

