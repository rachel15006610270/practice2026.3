def generate_permutations(arr):
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return

        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]  # 交换
            backtrack(start + 1)  # 递归
            arr[start], arr[i] = arr[i], arr[start]  # 恢复

    result = []
    backtrack(0)
    return result
#每一层递归会将当前位置与后续每个元素交换，递归深度为 n层。第 1 层有 n种选择，第 2 层有 n−1种选择，依此类推，总共 n!种排列，因此时间复杂度为 O(n!)
