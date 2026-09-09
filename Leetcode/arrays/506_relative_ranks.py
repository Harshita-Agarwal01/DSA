# TC=O(nlogn)  SC=O(n)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = []
        for i in range(n):
            arr.append((score[i], i))
        arr.sort(reverse=True)  # O(nlogn)
        answer = [""] * n
        for i in range(n):
            value = arr[i][0]
            index = arr[i][1]
            if i == 0:
                answer[index] = "Gold Medal"
            elif i == 1:
                answer[index] = "Silver Medal"
            elif i == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(i + 1)

        return answer
