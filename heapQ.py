#encoding:utf-8
from typing import List
from collections import deque


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        value = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                now_diff = nums[i] + nums[j] + nums[k] - target
                if abs(now_diff) < abs(value - target):
                    value = nums[i] + nums[j] + nums[k]
                    print(value)
                    print(i, j ,k)
                if now_diff == 0:
                    return target
                elif now_diff > 0:
                    k -= 1
                else:
                    j += 1
        return value


if __name__ == '__main__':
    a =     deque(range(10))
    import heapq
    a.append(1000)
    print(a)
    s = Solution()
    print(s.threeSumClosest([0,2,1,-3], 1))