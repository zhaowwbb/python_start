class CombinationSum:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        # Sorting allows for early pruning of the search space
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
            # Found a valid combination, append a copy to the results
            result.append(list(temp_list))
            return

        for i in range(start, len(candidates)):
            # If the current candidate exceeds the remaining target, stop searching this branch
            if candidates[i] > remain:
                break

            temp_list.append(candidates[i])
            # Notice we pass 'i' to allow reusing the same number multiple times
            self._backtrack(result, temp_list, candidates, remain - candidates[i], i)
            # Backtrack: remove the last element before checking the next branch
            temp_list.pop()

    def combinationSumV2(self, candidates: list[int], target: int) -> list[list[int]]:
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
            tempList.append(candidates[i])
            self.backtraceV2(result, tempList, candidates, remain - candidates[i], i)
            tempList.pop()

    def combinationSumV3(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        self.backtraceV3(result, [], candidates, target, 0)
        return result

    def backtraceV3(
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
            tempList.append(candidates[i])
            self.backtraceV3(result, tempList, candidates, remain - candidates[i], i)
            tempList.pop()


# --- Test Logic Framework ---


class TestCase:
    def __init__(self, candidates: list[int], target: int, expected: list[list[int]]):
        self.candidates = candidates
        self.target = target

        # Ensure inner lists are sorted, then sort the outer list to safely compare results
        sorted_expected = [sorted(comb) for comb in expected]
        self.expected = sorted(sorted_expected)


if __name__ == "__main__":
    solver = CombinationSum()

    # Defining multiple test cases
    test_cases = [
        TestCase(candidates=[2, 3, 6, 7], target=7, expected=[[2, 2, 3], [7]]),
        TestCase(
            candidates=[2, 3, 5], target=8, expected=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        ),
        TestCase(candidates=[2], target=1, expected=[]),
        TestCase(candidates=[5, 10, 15], target=5, expected=[[5]]),
    ]

    print("Executing Automation Test Suite...\n")
    passed_count = 0

    for idx, tc in enumerate(test_cases, 1):
        # SINGLE execution call per test case requirement
        # actual_result = solver.combinationSum(tc.candidates, tc.target)
        actual_result = solver.combinationSumV3(tc.candidates, tc.target)

        # Sort actual result lists to confidently match against standard structured expected data
        sorted_actual = sorted([sorted(comb) for comb in actual_result])

        is_passed = sorted_actual == tc.expected
        if is_passed:
            passed_count += 1

        # Print Test Execution Summary
        status = "✅ PASS" if is_passed else "❌ FAIL"
        print(f"Test Case {idx}: {status}")
        print(f"  Candidates: {tc.candidates} | Target: {tc.target}")
        print(f"  Expected  : {tc.expected}")
        print(f"  Actual    : {sorted_actual}")
        print("-" * 67)

    print(f"Test Run Complete: {passed_count}/{len(test_cases)} Passed.")
