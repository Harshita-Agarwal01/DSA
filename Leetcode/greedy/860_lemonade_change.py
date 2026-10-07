# TC=O(n)  SC=O(1)
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        n = len(bills)
        note5 = 0
        note10 = 0
        for i in range(n):
            if bills[i] == 5:
                note5 += 1
            elif bills[i] == 10:
                note10 += 1
                if note5 > 0:
                    note5 -= 1
                else:
                    return False
            else:
                if note5 > 0 and note10 > 0:
                    note10 -= 1
                    note5 -= 1
                elif note5 >= 3:
                    note5 -= 3
                else:
                    return False
        return True
