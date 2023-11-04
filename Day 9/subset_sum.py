def recursion_sum(index, sum, arr, subset_sum, n):
    if index == n:
        subset_sum.append(sum)
        return
    # picking the element
    recursion_sum(index + 1, sum+arr[index], arr, subset_sum, n)
    # not picking the element
    recursion_sum(index + 1, sum, arr, subset_sum, n)



def get_subset_sum(arr, n):
    subset_sum = []
    recursion_sum(0, 0, arr, subset_sum, n)
    subset_sum.sort()
    return subset_sum


if "__main__" == __name__:
    print(get_subset_sum(arr=[5, 2, 1], n=3))