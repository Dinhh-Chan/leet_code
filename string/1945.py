class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convert(number):
            res = 0 
            for i in number :
                res += int(i)
            return str(res)
        string='abcdefghijklmnopqrstuvwxyz'
        res_string = ''
        for i in s :
            res_string += str(1 + string.find(i))
        for i in range(k):
            res_string = convert(res_string)
        return int(res_string)