class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)[::-1]
        if str(x) == temp:
            return True
        else:
            return False
    
if __name__ == "__main__":
    print(Solution().isPalindrome(-121))