import math
import random

#[-1, 1] -> [0, 255]
# -> remap to ints between 0 and 255
# -> remap each int to a string using chr
# -> join the strings
# -> return the string

def float_arr_to_str_arr(float_arr: list[float]) -> str:
    int_arr = [round((x + 1) * 127.5) for x in float_arr]
    
    char_arr = [chr(x) for x in int_arr]
    
    return "".join(char_arr)

def str_arr_to_float_arr(str_arr: str) -> list[float]:
    int_arr = [ord(x) for x in str_arr]
    
    float_arr = [(x / 127.5) - 1 for x in int_arr]
    
    return float_arr