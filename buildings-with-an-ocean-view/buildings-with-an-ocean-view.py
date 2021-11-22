class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        s = []
        m = 0
        i = len(heights) - 1
        while (i >= 0):
            if heights[i] > m:
                m = heights[i]
                # i -= 1
                s.append(i)
            i -= 1
        # print(s)
        return sorted(s)
                
    
        # s = []
        # for i in range(len(heights)):
        #     signal = True
        #     for j in range(i+1,len(heights)):
        #         if heights[i] <= heights[j]:
        #             signal = False
        #             break
        #     if signal:
        #         s.append(i)
        # return s
            
                    
                
                
        
        