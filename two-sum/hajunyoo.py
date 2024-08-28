class Solution1:
    # Brute Force
    # time complexity: O(n^2)
    # space complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        for x1 in range(n):
            for x2 in range(x1, n):
                if x1 == x2:
                    continue
                tmp = nums[x1] + nums[x2]
                if tmp == target:
                    return [x1, x2]


class Solution2:
    # time complexity: O(n)
    # space complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 키: 숫자, 값: 인덱스
        seen = {}
        for i in range(len(nums)):
            # 목표 숫자에서 현재 값을 뺀 값이 seen에 있다면
            diff = target - nums[i]
            if diff in seen:
                # 해당 값의 인덱스와 현재 인덱스를 반환
                return [seen[diff], i]

            # 현재 값을 seen에 추가
            seen[nums[i]] = i
