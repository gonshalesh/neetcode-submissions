# Python Syntax Shortcuts for Leetcode

## Iterating Through a List

```python
# forward — by element
for num in nums:

# forward — by index
for i in range(len(nums)):

# forward — both index and element
for i, num in enumerate(nums):

# backward — by index (last to first)
for i in range(len(nums) - 1, -1, -1):
#              start           stop  step
#              last index       -1    go backwards
# e.g. len=5 → i = 4, 3, 2, 1, 0

# backward — by element
for num in reversed(nums):

# two lists at once
for a, b in zip(list1, list2):
```

---

## N-Pointer Patterns

```python
# two pointers — opposite ends (palindrome, sorted two-sum)
left, right = 0, len(nums) - 1
while left < right:
    # do something with nums[left] and nums[right]
    left += 1   # move left forward
    right -= 1  # move right backward

# two pointers — same direction (slow/fast, remove duplicates)
slow = 0
for fast in range(len(nums)):
    if some_condition:
        nums[slow] = nums[fast]
        slow += 1

# sliding window — variable size
left = 0
for right in range(len(nums)):
    # expand window: add nums[right]
    while window_is_too_big:
        # shrink window: remove nums[left]
        left += 1

# sliding window — fixed size k
for right in range(len(nums)):
    if right >= k:
        # remove nums[right - k] (element leaving the window)
    # add nums[right] (element entering the window)
```

---

## Avoiding "Index Out of Bounds"

```python
# WRONG — crashes when i is the last index
if nums[i] == nums[i + 1]:

# FIX 1 — stop one early
for i in range(len(nums) - 1):       # stops before last element
    if nums[i] == nums[i + 1]:

# FIX 2 — start one later
for i in range(1, len(nums)):         # starts at second element
    if nums[i] == nums[i - 1]:

# FIX 3 — guard with a bounds check
if i + 1 < len(nums) and nums[i] == nums[i + 1]:

# when using two pointers — always check before accessing
while left < right:                   # ensures both are valid
while i < len(nums) and nums[i] == target:  # check bounds FIRST

# empty array guard
if not nums:
    return []
```

---

## Dictionary Manipulation

```python
# create
freq_map = {}

# add / update a key
freq_map[key] = value
freq_map[key] += 1             # only works if key already exists

# safe increment (two ways)
freq_map[key] = freq_map.get(key, 0) + 1     # .get returns 0 if key missing
# or
if key in freq_map:
    freq_map[key] += 1
else:
    freq_map[key] = 1

# check if key exists
if key in freq_map:

# get value (crashes if missing)
val = freq_map[key]

# get value (safe, returns default)
val = freq_map.get(key, 0)

# delete a key
freq_map.pop(key)              # removes and returns the value
del freq_map[key]              # just removes it

# loop through keys
for key in freq_map:

# loop through values
for val in freq_map.values():

# loop through both
for key, val in freq_map.items():

# get key with highest value (useful for "most frequent")
max_key = max(freq_map, key=freq_map.get)

# defaultdict — auto-creates missing keys
from collections import defaultdict
freq_map = defaultdict(int)    # missing keys default to 0
freq_map[key] += 1             # no need to check if key exists

group_map = defaultdict(list)  # missing keys default to []
group_map[key].append(val)     # no need for "if key not in"
```

---

## List Manipulation

```python
# create
nums = []
nums = [0] * 26                # 26 zeros: [0, 0, 0, ..., 0]
nums = [[] for _ in range(n)]  # n empty lists: [[], [], [], ...]
# WARNING: [[]] * n creates n references to the SAME list — don't use it

# add to end
nums.append(val)

# add at specific index
nums.insert(i, val)

# remove last element
last = nums.pop()

# remove element at index
removed = nums.pop(i)

# remove first occurrence of a value
nums.remove(val)               # crashes if not found

# check if value exists
if val in nums:

# length
len(nums)

# slice (does NOT modify original)
nums[1:4]                      # elements at index 1, 2, 3
nums[:3]                       # first 3 elements
nums[2:]                       # everything from index 2 onward
nums[-1]                       # last element
nums[-2:]                      # last 2 elements

# sort
nums.sort()                    # in-place, modifies nums
sorted_copy = sorted(nums)    # returns a new list

# reverse
nums.reverse()                 # in-place
reversed_copy = nums[::-1]    # returns a new list
```

---

## Tuple Manipulation

```python
# create
pair = (1, 2)
triple = (1, 2, 3)

# access (same as lists)
pair[0]                        # 1
pair[1]                        # 2

# unpack
a, b = pair                   # a=1, b=2
x, y, z = triple              # x=1, y=2, z=3

# why tuples matter for leetcode:
# — lists CANNOT be dictionary keys (mutable)
# — tuples CAN be dictionary keys (immutable)
key = tuple([1, 0, 1, 0])     # convert list → tuple for use as dict key

# convert back
lst = list(some_tuple)         # tuple → list
```

---

## Common Patterns from Your Solutions

```python
# "have I seen this before?" — use a set
seen = set()
if num in seen:                # O(1) lookup
    return True
seen.add(num)

# "how many times has this appeared?" — use a dict
freq_map = {}
freq_map[num] = freq_map.get(num, 0) + 1

# "find the complement" — store what you've seen, check for what you need
seen = {}
diff = target - num
if diff in seen:
    return [seen[diff], i]
seen[num] = i

# "group things by a shared property" — dict with list values
groups = {}
if key not in groups:
    groups[key] = []
groups[key].append(item)

# "do something only once per loop" — underscore
for _ in range(k):             # loop k times, don't need the counter

# convert char to number and back
idx = ord('a')                 # 97
char = chr(97)                 # 'a'
position = ord(char) - ord('a')  # a=0, b=1, c=2, ...
```
