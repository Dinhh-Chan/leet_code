class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        string = ''
        current_index = 0 
        for i in words :
            string += i 
            if string == s :
                return True 
            if not s.startswith(string):
                break
        return False 