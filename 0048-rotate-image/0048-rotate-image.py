import numpy as np

class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        
        rows = len(m)
        columns = len(m[0])

        m_ = np.empty((rows, columns))

        for i in range(len(m)):
            for j in range(len(m[0])):
                m_[i][j] = m[i][j]

        for i in range(len(m_)-len(m)*len(m[0])):
            m_.pop(0)

        i_ = len(m_)-1
        j_ = 0

        m__ = len(m)
        n = len(m[0])

        for i in range(m__):
            for j in range(n):
                m[i][j] = int(m_[i_][j_])
                i_ -= 1
            i_ = len(m_)-1
            j_ += 1