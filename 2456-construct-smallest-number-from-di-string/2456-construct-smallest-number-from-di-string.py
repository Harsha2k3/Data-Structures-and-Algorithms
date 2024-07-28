class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        self.res = None

        def fun(ind , res_so_far):

            if self.res:
                return

            if ind >= len(pattern):
                self.res = ''.join(str(item) for item in res_so_far)
                return

            last_digit = res_so_far[-1]
            
            for i in range(1 , 10):

                appended = False

                if pattern[ind] == 'I' and i > last_digit and i not in res_so_far:
                    appended = True
                    res_so_far.append(i)
                    fun(ind+1, res_so_far)
                
                elif pattern[ind] == 'D' and i < last_digit and i not in res_so_far:
                    appended = True
                    res_so_far.append(i)
                    fun(ind+1, res_so_far)

                if appended:
                    res_so_far.pop(-1)

        for i in range(1 , 10):
            if not self.res:
                fun(0 , [i])
        
        return self.res