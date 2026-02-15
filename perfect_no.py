class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        summ = 1  
        i = 2
        while i * i <= num:
            if num % i == 0:
                summ += i
                if i != num // i:  
                    summ += num // i
            i += 1
        
        return summ == num
