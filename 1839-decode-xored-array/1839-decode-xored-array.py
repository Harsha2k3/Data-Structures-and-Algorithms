class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        # a xor b = c
        # (a xor b) xor a = c xor a
        # (a xor a) xor b = c xor a
        # 0 xor b = c xor a
        # b = c xor a

        # Since that encoded[i] = arr[i] XOR arr[i+1], then arr[i+1] = encoded[i] XOR arr[i].

        arr = [first] * (len(encoded) + 1)

        for i in range(len(encoded)):
            arr[i+1] = encoded[i] ^ arr[i]

        return arr