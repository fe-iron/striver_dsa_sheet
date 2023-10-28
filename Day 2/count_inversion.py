def merge(arr, low, mid, high):
    count = 0
    left = low
    right = mid + 1
    temp = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            count += (mid - left) + 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i - low]
    return count

def merge_sort(arr, low, high):
    if low >= high:
        return 0
    count = 0
    mid = (low + high) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count

def getInversions(arr):
	# Write your code here.
    return merge_sort(arr, 0, len(arr)-1)

getInversions(arr=[2, 5, 1, 3, 4])