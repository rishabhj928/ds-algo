
from typing import List
def nextGreaterElement(nums1: List[int]) -> List[int]:
    d, st = {}, []
    for x in nums1:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)
    return d.values()
print(nextGreaterElement([3, 5, 4, 7, 8, 1, 9]))
