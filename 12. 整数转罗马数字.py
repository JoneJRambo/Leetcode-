class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"] # 1000，2000，3000
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100~900
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10~90
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1~9
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
