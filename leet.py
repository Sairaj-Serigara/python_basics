class Solution(object):
    def isPalindrome(self, x):
        while (x==0):
                y=[x%10]
                x=x/10
        if(x==y):
            print("YES")
        else:
            print("NO")
obj=Solution()
obj.isPalindrome(120)