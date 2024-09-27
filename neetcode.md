## Given an integer array nums, return true if any value appears more than once in the array, otherwise return false

```
def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```

## Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false

### An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = dict()
        h2 = dict()
        for i in s:
            if i in h1:
                h1[i]+=1
            else: h1[i]=0
        for i in t:
            if i in h2:
                h2[i]+=1
            else: h2[i]=0
        if h1==h2: return True
        else: return False
```

## Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = dict()
        ind = 0
        for i in nums:
            diff = target - i
            if diff in prevMap:
                return [prevMap[diff],ind]
            prevMap[i] = ind
            ind +=1
```

## Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order

```
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        f = dict()
        for i in strs:
            s = "".join(sorted(i))
            if  s not in f:
                f[s] = [i]
            else:
                f[s]+=[i]
        print(f.values())
        ans = list(f.values())


        return ans
```

### or

```

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
```

## Given an integer array nums and an integer k, return the k most frequent elements within the array

```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
                continue
            d[i]+=1
        #print(list(d.values()))

        l = sorted(d.keys(), key = lambda h:d[h])
        return (l[::-1][:k:])
```

### or

```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```
