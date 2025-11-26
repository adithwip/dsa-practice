from typing_extensions import List


class Solution:
    def two_sum_first_solution(self, list: List[int], target: int):
        hashmap = {}

        for i, num in enumerate(list):
            hashmap[num] = i

        for i, num in enumerate(list):
            desired = target - num

            if desired in hashmap and hashmap[desired] != i:
                return [hashmap[desired], i]

    def two_sum_second_solution(self, list: List[int], target: int):
        hmap = {}

        for i, num in enumerate(list):
            desired = target - num

            if desired in hmap and hmap[desired] < i:
                return [i, hmap[desired]]
            else:
                hmap[num] = i
