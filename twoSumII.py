from typing import List
import math

def twoSum(numbers: List[int], target: int):
    left_side = 0
    right_side = len(numbers) - 1
    while left_side < right_side:
        final_sum = numbers[left_side] + numbers[right_side]
        if final_sum == target:
            return [left_side+1, right_side+1]
        
        if final_sum > target: # becuase a right number that is bigger than the sum will skew the answer
            right_side -= 1
        elif final_sum < target: # now the left side is too small after the sum of bigger is below
            left_side += 1

if __name__ == "__main__":
    print(twoSum([-5,-3,0,2,4,6,8], 5))