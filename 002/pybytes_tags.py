"""Fetch and analyze the PyBytes tags on their RSS feed."""

from collections import Counter
from itertools import combinations
import xml.etree.ElementTree as ET

import requests


def get_feed(url):
    """Gets the RSS feed at url and parses it into an element tree"""
    response = requests.get(url)
    return ET.fromstring(response.text)


def count_tags(etree):
    """Given an XML element tree, with structure root->item->category
     it bins up the tags"""
    tags = Counter()
    for item in etree.iter('item'):
        categories = item.findall('category')
        tags += Counter([category.text for category in categories])
    return tags


def print_top_10(tag_stats):
    """Prints the top ten results, given {tag: count, ...}"""
    print("Top 10 Tags:")
    for tag, count in tag_stats.most_common(10):
        print_fixed_width_pairs(tag, count, 35)

def print_similar(tag_stats):
    """Prints any tags that are similar to each other (same but plural)"""
    pairs = combinations(tag_stats.keys(), 2)
    similars = [(first, second) for (first, second) in pairs if first == second + "s"]
    print("Similar tags:")
    for first, second in similars:
        print_fixed_width_pairs(first, second, 35)

def print_fixed_width_pairs(first, second, width):
    """Prints out first and second with a calculated amount of space
    in between, based on a fixed width.
    """
    print(f"{first}{' '*(width - len(str(first)) - len(str(second)))}{second}")


if __name__ == "__main__":
    tree = get_feed("https://pybit.es/feeds/all.rss.xml")
    counts = count_tags(tree)
    print_top_10(counts)
    print("")
    print_similar(counts)

