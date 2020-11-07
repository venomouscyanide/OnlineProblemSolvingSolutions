"""
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
https://www.hackerrank.com/challenges/count-triplets-1/forum/comments/516189?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
from collections import defaultdict
from itertools import combinations


def triplets(arr, r):
    triplets = 0
    occurance_v_count = defaultdict(int)
    followed_by_r = defaultdict(int)
    for val in arr[::-1]:
        triplets += followed_by_r[r * val]
        followed_by_r[val] += occurance_v_count[r * val]
        occurance_v_count[val] += 1
    # print(occurance_v_count)
    # print(followed_by_r)
    return triplets


if __name__ == '__main__':
    print(triplets([1, 1, 3, 9], 3))
