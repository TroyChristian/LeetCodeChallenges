class Solution:
   
    def romanToInt(self, s: str) -> int:
        hash_table = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        numerals = []
        arabic_numbers = []
        
        
        subtraction_pairs = {"I":["V","X"],
                             "X":["L","C"],
                             "C":["D", "M"]
                            
                            }
        penalty_values = {"I":-1,
                          "X":-10,
                          "C": -100
            
        }
        
        
        for numeral in s:
            numerals.append(numeral)
        end_array = len(numerals) - 1
        for idx,numeral in enumerate(numerals):
            print("index:{}".format(idx))
            print("numeral:{}".format(numeral))
            
            if idx < end_array:
                print("numerals[idx +1] = {}".format(numerals[idx+1]))
                if numeral in subtraction_pairs.keys() and numerals[idx + 1] in subtraction_pairs[numeral]:
                    arabic_numbers.append(penalty_values[numeral])
                else:
                    arabic_numbers.append(hash_table[numeral])
            if idx == end_array:
                arabic_numbers.append(hash_table[numeral])
            print(numerals)
            print(arabic_numbers)
            #print(subtraction_pairs.keys())
            #print(subtraction_pairs.values())
        result = sum(arabic_numbers)
            
        print(result)
        return result
s = "MCMXCIV"
roman = Solution()
print(roman.romanToInt(s))