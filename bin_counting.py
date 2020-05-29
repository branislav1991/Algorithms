from typing import List

def convToBin(num: int) -> List[int]:
        output = []
        while num > 0:
            output.append(num % 2)
            num = num // 2
        return output
    
def countBits(num: int) -> List[int]:
    output = []
        j = 2
        i = 0
        k = 0
        while i <= num:
            k = k + 1
            if i < 2: output.append(i)
            else:
                output.append(bin(i).count("1"))
                if k == j:
                    output.extend(output[-j:])
                    i = i + j
                    j = 2**j
                    k = 0
            i = i + 1
                    
        return output

countBits(20)