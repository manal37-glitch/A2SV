from collections import Counter
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        return Counter(a)== Counter(b)
