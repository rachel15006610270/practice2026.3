def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def generate_subsets(arr):
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()

    result = []
    backtrack(0, [])
    return result
a=list(map(int, input().split()))
print(generate_subsets(a))
#上述代码中，fibonacci_recursive 函数每次递归都会分裂成两个子问题，递归树的节点总数为 2^n，因此时间复杂度为O(2^n)generate_subsets 函数通过回溯法枚举所有子集，每个元素有选或不选两种选择，子集总数为2^n,所以整体时间复杂度也是O(2^n)