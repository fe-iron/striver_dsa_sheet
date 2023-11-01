class Item:
    def __init__(self, value, weight) -> None:
        self.value = value
        self.weight = weight


class Solution:
    def fractional_knapsack(self, item_arr, n, w):
        item_arr.sort(key=lambda x: x.value/x.weight, reverse=True)
        calculated_weight = 0
        total_value = 0
        for i in range(n):
            if calculated_weight + item_arr[i].weight <= w:
                calculated_weight += item_arr[i].weight
                total_value += item_arr[i].value
            else:
                remaining_weight = w - calculated_weight
                total_value += ((item_arr[i].value / item_arr[i].weight) * remaining_weight)
                break
        return total_value
    
if __name__ == '__main__':
    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    obj = Solution()
    ans = obj.fractionalKnapsack(W, arr, n)
    print("The maximum value is", ans)