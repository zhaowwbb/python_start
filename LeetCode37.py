from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                
                # Find an empty cell
                if board[row][col] == '.':
                    
                    # Try placing digits '1' through '9'
                    for char in map(str, range(1, 10)):
                        if self.is_valid(board, row, col, char):
                            board[row][col] = char  # Tentative assignment
                            
                            # Recursively try to solve the rest of the board
                            if self.solve(board):
                                return True
                            
                            board[row][col] = '.'  # Backtrack: undo our choice
                            
                    return False  # Triggers backtracking to the previous level
        return True  # Board is fully solved

    def is_valid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
        for i in range(9):
            # 1. Check Row constraint
            if board[row][i] == char:
                return False
            
            # 2. Check Column constraint
            if board[i][col] == char:
                return False
            
            # 3. Check 3x3 Box constraint
            box_row = 3 * (row // 3) + i // 3
            box_col = 3 * (col // 3) + i % 3
            if board[box_row][box_col] == char:
                return False
                
        return True

    def solveSudokuV2(self, board: List[List[str]]) -> None:
        if not board or len(board) == 0:
            return
        self.solveV2(board)
    
    def solveV2(self, board: List[List[str]]) -> bool :
        for row in range(9):
            for col in range(9):
                # number = board[row][col]
                if board[row][col] == '.':
                    for c in map(str, range(1, 10)):
                        if self.isValidV2(board, row, col, c):
                            board[row][col] = c
                            if self.solveV2(board):
                                return True
                            else:
                                board[row][col] = '.'
                    
                    return False    

        return True
    
    def isValidV2(self, board: List[List[str]], row: int, col: int, number: str) -> bool:
        
        for i in range(9):
            # check row
            if board[row][i] == number:
                return False
            # check column
            if board[i][col] == number:
                return False
            
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        
        for r in range(boxRow, boxRow + 3):
            for c in range(boxCol, boxCol + 3):
                if board[r][c] == number:
                    return False
             
        return True  
    
    def solveSudokuV3(self, board: List[List[str]]) -> None:
        if not board or len(board) == 0:
            return
        self.solveV3(board)
    
    def solveV3(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for c in map(str, range(1, 10)):
                        if self.isValidV3(board, row, col, c):
                            board[row][col] = c
                            if self.solveV3(board):
                                return True
                            board[row][col] = '.'
                    
                    return False
        return True
    
    def isValidV3(self, board: List[List[str]], row: int, col: int, number: str) -> bool:
        for i in range(9):
            #check row
            if board[row][i] == number:
                return False
            #check column
            if board[i][col] == number:
                return False
            
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        for r in range(boxRow, boxRow + 3):
            for c in range(boxCol, boxCol + 3):
                if board[r][c] == number:
                    return False    
        
        return True      

# --- Local Test Case Execution ---
if __name__ == "__main__":
    # 1. Setup Input Data
    input_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    expected_output = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]

    # 2. Run the Solver
    solver = Solution()
    # solver.solveSudoku(input_board)
    # solver.solveSudokuV2(input_board)
    solver.solveSudokuV3(input_board)

    # 3. Verify Results
    print("--- Checking Sudoku Result ---")
    if input_board == expected_output:
        print("Success! The puzzle was solved correctly and matches expected output.")
    else:
        print("Failure! The solved board does not match.")
        print("Got:")
        for row in input_board:
            print(row)