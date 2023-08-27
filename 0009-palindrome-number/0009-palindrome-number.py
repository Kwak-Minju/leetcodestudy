class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        x_len = len(x_list)
        for i in range(int(x_len/2)) :
            if x_list[i] != x_list[x_len-1-i] :
                return print("false")
        return "true"                  