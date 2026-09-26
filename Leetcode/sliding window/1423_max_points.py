# TC=O(2n)  SC=O(1)
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        left_sum=0
        maxi=0
        for i in range(k):
            left_sum+=cardPoints[i]
            maxi=left_sum
        right_index=n-1
        right_sum=0
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_index]
            maxi=max(maxi,right_sum+left_sum)
            right_index-=1
        return maxi