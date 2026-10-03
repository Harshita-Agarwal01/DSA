# TC=O(n)+O(nlogn)+O(n)=O(nlogn)  SC=O(n)
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        # code here
        ratio = []
        for i in range(len(wt)):
            ratio.append([val[i] / wt[i], val[i], wt[i]])
        ratio.sort(reverse=True)
        result = 0
        i = 0
        while capacity > 0 and i < len(ratio):
            if capacity - ratio[i][2] >= 0:
                capacity = capacity - ratio[i][2]
                result += ratio[i][1]
            else:
                result += ratio[i][0] * capacity
                break
            i += 1
        return result
