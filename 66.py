class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def digits_to_int(self, digits):
        res = 0
        for digit in digits:
            res = res * 10 + digit
        return res
    
    def int_to_digits(self, num):
        digits = []
        while num > 0:
            digits.insert(0, num % 10)
            num = num / 10
        if len(digits) == 0:
            digits = [ 0 ]
        return digits
        
    def plusOne(self, digits):
        return self.int_to_digits(self.digits_to_int(digits) + 1)