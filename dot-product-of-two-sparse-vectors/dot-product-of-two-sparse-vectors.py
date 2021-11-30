class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        c = 0
        # elements = len(vec[0])
        elements = len(self.nums)
        for i in range(elements):
            c += self.nums[i] * vec.nums[i]
        return c
        # loop and multiply nums1[i] with nums2[i]

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)