
# Given sorted row's matrix, return index of row with maximum number of 1s in O(m+n) complexity.

# Step1: Get the index of first (or leftmost) 1 in the first row.
# Step2: Do following for every row after the first row 
#        IF the element on left of previous leftmost 1 is 0, ignore this row. 
#        ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.
# The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.

def rowWithMax1s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_idx = 0
    col_idx = cols - 1
    for i in range(rows):
        flag = False
        while col_idx >= 0 and matrix[i][col_idx] == 1:
            flag = True
            col_idx -= 1
        if flag:
            row_idx = i
        if row_idx == 0 and matrix[0][cols-1] == 0:
            return 0
    return row_idx

matrix = [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
print(rowWithMax1s(matrix))
