class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        for i in arr1:
            if i in arr2:
                if i in arr3:
                    res.append(i)
        return res