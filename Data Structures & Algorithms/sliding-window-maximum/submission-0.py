class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque_ = deque()
        n = len(nums)
        result = [0] * (n - k + 1)
        for r in range(n):
            while deque_ and deque_[0] <= r - k:
                deque_.popleft()
            while deque_ and nums[deque_[-1]] < nums[r]:
                deque_.pop()
            deque_.append(r)

            if r >= k - 1:
                result[r - k + 1] = nums[deque_[0]] 
        return result 

        