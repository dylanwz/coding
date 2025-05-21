'''
# TAG-HASH
# N.B. instead of setting marking with duplicates, we can 
'''
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited_rows = set()
        visited_cols = set()
        changed_idxs = set()
        for idx_row in range(len(matrix)):
            for idx_col in range(len(matrix[0])):
                if matrix[idx_row][idx_col] == 0:
                    if (idx_row, idx_col) not in changed_idxs:

                        for it in range(len(matrix[0])): # it goes along columns
                            if idx_row not in visited_rows:
                                if matrix[idx_row][it] != 0:
                                    changed_idxs.add((idx_row, it))
                                matrix[idx_row][it] = 0
                        for it in range(len(matrix)):
                            if idx_col not in visited_cols:
                                if matrix[it][idx_col] != 0:
                                    changed_idxs.add((it, idx_col))
                                matrix[it][idx_col] = 0
                        visited_rows.add(idx_row)
                        visited_cols.add(idx_col)