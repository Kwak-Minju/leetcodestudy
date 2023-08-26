class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for a in range(len(numbers)):
            for b in range(len(numbers)):
                if a<b:
                    if numbers[a]+numbers[b]== target:
                        return [a,b]

            