from collections import defaultdict
from typing import List, Dict, Tuple

def group_and_count(tuple_list: List[str]) -> Dict[str, int]:
    totals = defaultdict(int)

    for value in tuple_list:
        totals[value] += 1

    return totals


def group_and_sum(tuple_list: List[Tuple[str, float]]) -> Dict[str, float]:
    totals = defaultdict(float)

    for key, value in tuple_list:
        totals[key] += value

    return totals
