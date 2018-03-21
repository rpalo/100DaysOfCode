import pandas as pd

import sys

REMOTE_URL = "https://t.co/oARrOmrin7"


def load_tips(url):
    return pd.read_csv(REMOTE_URL)


def search_submissions(submissions, search_terms):
    search_string = "|".join(search_terms)
    return submissions[
        submissions["Python Tip:"].str.contains(search_string)
    ]


def interpret(results):
    if len(results) == 0:
        print("No rows were found with those search terms.")
        return False
    else:
        print("Results:\n-------------")
        for ind, row in results.iterrows():
            print(f"Tip #{ind + 1}:==================================")
            print(row['Python Tip:'])
            print(f"Submitted {row['Timestamp']} | By: {row['Your name or Twitter id:']}")
            print("")
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} SEARCH_TERMS...")
        exit(1)
    terms = sys.argv[1:]
    current_tips = load_tips(REMOTE_URL)
    matching_tips = search_submissions(current_tips, terms)
    if interpret(matching_tips):
        exit(0)
    else:
        exit(1)
