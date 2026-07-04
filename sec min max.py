def secmin(arr):
    if len(arr) < 2:
        print("Array too small")
        return

    min1 = max1 = arr[0]

    # Find min and max
    for num in arr:
        if num < min1:
            min1 = num
        if num > max1:
            max1 = num

    # Edge case: all elements are the same
    if min1 == max1:
        print("All elements are the same")
        return

    min2 = float('inf')
    max2 = float('-inf')

    # Find second min and second max
    for num in arr:
        if min1 < num < min2:
            min2 = num
        if max1 > num > max2:
            max2 = num

    if min2 == float('inf'):
        print("No second minimum")
    else:
        print("Second minimum:", min2)

    if max2 == float('-inf'):
        print("No second maximum")
    else:
        print("Second maximum:", max2)

# Input
arr = list(map(int, input("Enter elements separated by commas: ").split(",")))
secmin(arr)
