class Solution:
    def romanToInt(self, s: str) -> int:

        s=s.replace("IV","IIII").replace("IX","VIIII")
        s=s.replace("XL","XXXX").replace("XC","LXXXX")
        s=s.replace("CD","CCCC").replace("CM","DCCCC")

        total = 0
        for i in range(len(s)):
            
            match s[i]:
                case "M":
                    total+=1000
                case "D":
                    total+=500
                case "C":
                    total+=100
                case "L":
                    total+=50
                case "X":
                    total+=10
                case "V":
                    total+=5
                case "I":
                    total+=1
        
        return total
        