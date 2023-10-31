class Solution:
    def minimum_platform(self, arrival, departure, n):
        arrival.sort()
        departure.sort()
        plat_needed = 1
        result = 1
        i, j = 1, 0
        while i < n and j < n:
            if arrival[i] <= departure[j]:
                plat_needed += 1
                i += 1
            elif arrival[i] > departure[j]:
                plat_needed -= 1
                j += 1
            if plat_needed > result:
                result = plat_needed
        return result
                


