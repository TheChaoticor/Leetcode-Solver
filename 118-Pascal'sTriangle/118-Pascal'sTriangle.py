class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out=[[1]]

        for i in range(2,numRows+1):
            temp=[1]
            for c in range(1,i-1):
                temp.append(out[-1][c]+out[-1][c-1])
            temp.append(1)    
            out.append(temp)

        return out        
        
