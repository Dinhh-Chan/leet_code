class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        index1 = [1]
        if numRows == 1 :
            arr.append(index1)
            return arr
        index2 = [1,1]
        index=3
        if numRows == 2:
            arr.append(index1)
            arr.append(index2)
            return arr
        arr.append(index1)
        arr.append(index2)
        for i in range(2,numRows):
            temp_arr = arr[i-1]
            current_arr = [0]*(len(temp_arr)+1)
            current_arr[0]=1 
            current_arr[-1]=1
            for j in range(1,len(current_arr)-1):
                current_arr[j]= temp_arr[j-1]+ temp_arr[j]
            arr.append(current_arr)
        return arr