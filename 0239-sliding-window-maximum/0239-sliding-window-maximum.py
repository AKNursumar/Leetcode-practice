class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            if queue and queue[0]<=i-k:
                queue.popleft()
            if queue and nums[i]<=nums[queue[-1]]:
                queue.append(i)
            elif queue and nums[i]>nums[queue[-1]]:
                while queue and nums[i]>nums[queue[-1]]:
                    queue.pop()
                queue.append(i)
            else:
                queue.append(i)

            if i>=k-1:
                ans.append(nums[queue[0]])
        return ans