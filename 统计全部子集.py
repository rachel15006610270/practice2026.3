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