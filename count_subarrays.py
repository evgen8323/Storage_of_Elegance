def countSubarrays(A, minK, maxK):
        res = j = 0
        jmin = jmax = -1
        for i,a in enumerate(A):
            if not minK <= a <= maxK:
                jmin, jmax, j = -1, -1, i + 1
            if a == minK: jmin = i
            if a == maxK: jmax = i
            res += max(0, min(jmin, jmax) - j + 1)
        return res
        

nums = [355,398,945,945,820,945,35,1945,171,945,35,109,790,441,552]
minK = 35
maxK = 945

print(countSubarrays(nums, minK, maxK))
