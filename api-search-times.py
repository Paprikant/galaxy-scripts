#!/usr/bin/env python3
import time
import json
from bioblend.galaxy import GalaxyInstance
from random_word import Wordnik

GALAXY_URL = "http://localhost:8080"
GALAXY_KEY = "36719d39063e1398c6672da9f5c09c33"

# how many searches should be performed
SEARCHES = 1


def main():
    """
    main queries galaxy histories by random search terms and measures the time it takes
    """
    gi = GalaxyInstance(GALAXY_URL, key=GALAXY_KEY)
    wn = Wordnik()

    execution_times: List[int] = []

    for i in range(SEARCHES):
        # SQL databases will cache results - therefore change to a new search term every time
        search_term = wn.get_random_word()

        start = time.time()
        resp = gi.make_get_request(f"{gi.base_url}/api/histories?q=name&qv=sad&all=true")
        duration = (time.time() - start)

        execution_times.append(duration)
        print(f"Found {len(json.loads(resp.content)):1} histories for term {search_term:15} in {duration}s")

    print("\n")
    print(f"max: {max(execution_times)}")
    print(f"min: {min(execution_times)}")
    print(f"avg: {sum(execution_times) / len(execution_times)}")


if __name__ == '__main__':
    """
    Execute the script
    """
    main()

