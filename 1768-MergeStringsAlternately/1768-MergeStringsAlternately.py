class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=[]
        for i ,j in zip(word1,word2):
            output.append(i)
            output.append(j)
        if len(word1)>len(word2):
            output.append(word1[len(word2):])
        else:

            output.append(word2[len(word1):])

        return ''.join(output)    
