class Solution(object):
   def isPalindrome(self, x):
      x = str(x)
      l = []
      l_ = []

      for i in x:
         l.append(i)
         l_.append(i)

      l.reverse()
          
      return(l == l_)