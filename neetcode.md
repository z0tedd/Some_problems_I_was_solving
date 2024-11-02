## Kth Largest Integer in a Stream

Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

```Python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
```

```cpp
class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
    }

    int add(int val) {
        minHeap.push(val);
        if (minHeap.size() > k) {
            minHeap.pop();
        }
        return minHeap.top();
    }
};
```

## Given an array nums of unique integers, return all possible subsets of nums

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset += [nums[i]]
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
```

## You are given the root of a binary tree root. Invert the binary tree and return its root

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = [root]

        while stack:
            curr = stack.pop(0)
            if curr:
                print(curr.left, curr.right)
            if curr is None:

                stack.append(None)
                break

            curr.left, curr.right = curr.right, curr.left
            if curr.right != None:stack.append(curr.right)
            if curr.left != None:stack.append(curr.left)

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

```

## You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

```python
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    res= 0
    lowest = prices[0]

    for price in prices:
      lowest = min(lowest,price)
      res = max(res, price -lowest)
    return res
```

## You are given an array of distinct integers nums, sorted in ascending order, and an integer target

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
```

## Given a string s, return true if it is a palindrome, otherwise return false

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        alpanumeric = "qwertyuiopasdfghjklzxcvbnm1234567890".upper()
        i = 0
        j = len(s)-1
        while j>i:
            if s[j] not in alpanumeric:
                j-=1
                continue
            if s[i] not in alpanumeric:
                i+=1
                continue
            if s[j]!=s[i]:return False
            j-=1
            i+=1
        return True
```

## You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.`

```python
class Solution:
  def isValid(self,s:str)-> bool:
    Map = {")":"(","}":"{","]":"["}
    stack = []
    for i in s:
      if i not in Map:
        stack.append(i)
      if not stack or stack[-1]!=Map[i]:
        return False
    return not stack
```

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
