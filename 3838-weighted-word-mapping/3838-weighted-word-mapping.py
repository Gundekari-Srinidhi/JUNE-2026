class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d = {}
        val = 0
        for i in weights:
            d[chr(97+val)] = i
            val += 1
        s = ""
        for word in words:
            sum1 = 0
            for i in range(len(word)):
                sum1 += d[word[i]]    
            sum1 = sum1 % 26
            s += chr(ord('z')-sum1)
        return s


        