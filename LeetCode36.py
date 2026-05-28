class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                number = board[r][c]

                # Skip empty cells
                if number != ".":
                    # Construct unique string markers for each constraint group
                    row_key = f"{number} in row {r}"
                    col_key = f"{number} in col {c}"
                    box_key = f"{number} in box {r // 3}-{c // 3}"

                    # If any of these keys are already in the set, it's a duplicate
                    if (row_key in seen) or (col_key in seen) or (box_key in seen):
                        return False

                    # Store the markers in the set
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)

        return True

    def isValidSudokuV2(self, board: list[list[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                number = board[r][c]
                if number != ".":
                    row_key = f"{number} in row {r}"
                    col_key = f"{number} in col {c}"
                    box_key = f"{number} in box {r//3}-{c//3}"

                    if (row_key in seen) or (col_key in seen) or (box_key in seen):
                        return False

                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)

        return True


# --- Test Logic ---
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Valid Board
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    # Example 2: Invalid Board (Has two '8's in the top-left 3x3 sub-box)
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    test_cases = [
        ("Example 1 (Valid Board)  ", valid_board, True),
        ("Example 2 (Invalid Board)", invalid_board, False),
    ]

    print("=" * 60)
    print(f"{'TEST CASE':<25} | {'EXPECTED':<10} | {'ACTUAL':<10} | {'STATUS'}")
    print("=" * 60)

    for name, board, expected in test_cases:
        # actual = solution.isValidSudoku(board)
        actual = solution.isValidSudokuV2(board)
        status = "✅ PASS" if actual == expected else "❌ FAIL"
        print(f"{name:<25} | {str(expected):<10} | {str(actual):<10} | {status}")

    print("=" * 60)
