class CombinationSumII:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        # Sorting is required to place duplicate numbers adjacent to each other
        candidates.sort()
        self._backtrack(result, [], candidates, target, 0)
        return result

    def _backtrack(
        self,
        result: list[list[int]],
        temp_list: list[int],
        candidates: list[int],
        remain: int,
        start: int,
    ):
        if remain == 0:
            result.append(list(temp_list))
            return

        for i in range(start, len(candidates)):
            # Early pruning: if the current candidate exceeds the remaining target, stop
            if candidates[i] > remain:
                break

            # Skip duplicate elements at the same depth level of the recursion tree
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            temp_list.append(candidates[i])
            # Pass 'i + 1' to move to the next index, ensuring each unique element is used once
            self._backtrack(
                result, temp_list, candidates, remain - candidates[i], i + 1
            )
            # Backtrack
            temp_list.pop()

    # --- Test Logic Framework ---

    def combinationSum2V2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        self.backtraceV2(result, [], candidates, target, 0)
        return result

    def backtraceV2(
        self,
        result: list[list[int]],
        tempList: list[int],
        candidates: list[int],
        remain: int,
        start: int,
    ):
        if remain == 0:
            result.append(list(tempList))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            tempList.append(candidates[i])
            self.backtraceV2(
                result, tempList, candidates, remain - candidates[i], i + 1
            )
            tempList.pop()


class TestCase:
    def __init__(self, candidates: list[int], target: int, expected: list[list[int]]):
        self.candidates = candidates
        self.target = target

        # Normalize the expected matrix layout (sort internally and externally)
        sorted_expected = [sorted(comb) for comb in expected]
        self.expected = sorted(sorted_expected)


if __name__ == "__main__":
    solver = CombinationSumII()

    # Defining multiple test cases matching the problem description
    test_cases = [
        TestCase(
            candidates=[10, 1, 2, 7, 6, 1, 5],
            target=8,
            expected=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        ),
        TestCase(candidates=[2, 5, 2, 1, 2], target=5, expected=[[1, 2, 2], [5]]),
        TestCase(candidates=[2, 4, 6], target=5, expected=[]),
    ]

    print("Executing Combination Sum II Automation Suite...\n")
    passed_count = 0

    for idx, tc in enumerate(test_cases, 1):
        # Call implementation method ONLY ONE time per test case execution
        # actual_result = solver.combinationSum2(tc.candidates, tc.target)
        actual_result = solver.combinationSum2V2(tc.candidates, tc.target)

        # Sort actual elements to avoid false negatives due to list ordering permutations
        sorted_actual = sorted([sorted(comb) for comb in actual_result])

        is_passed = sorted_actual == tc.expected
        if is_passed:
            passed_count += 1

        status = "✅ PASS" if is_passed else "❌ FAIL"
        print(f"Test Case {idx}: {status}")
        print(f"  Candidates: {tc.candidates} | Target: {tc.target}")
        print(f"  Expected  : {tc.expected}")
        print(f"  Actual    : {sorted_actual}")
        print("-" * 67)

    print(f"Test Run Complete: {passed_count}/{len(test_cases)} Passed.")
