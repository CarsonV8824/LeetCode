from typing import List
import math

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    combined_array = nums1 + nums2
    combined_array.sort()
    if len(combined_array) % 2 == 0:
        left_item = combined_array[math.floor((len(combined_array)-1)/2)]
        right_item = combined_array[math.ceil((len(combined_array)-1)/2)]
        return float((left_item + right_item) / 2)
    elif len(combined_array) % 2 ==1:
        return combined_array[math.floor((len(combined_array)-1)/2)]
