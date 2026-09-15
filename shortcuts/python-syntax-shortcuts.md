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
# a dictionary maps keys to values, like a lookup table
# the main advantage over a list is that lookup by key is O(1)
# instead of searching through elements, Python hashes the key and jumps straight to it
# keys must be immutable (strings, numbers, tuples) — lists cannot be keys

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

# remove last element — also returns the removed value
nums = [10, 20, 30]
last = nums.pop()      # nums becomes [10, 20], last = 30

# remove element at a specific index — also returns the removed value
removed = nums.pop(0)  # nums becomes [20], removed = 10

# remove first occurrence of a value
nums.remove(val)               # crashes if not found

# check if value exists
if val in nums:

# length
len(nums)

# slice — extracts a portion of the list without modifying it
# syntax: list[start:stop] — includes start, excludes stop
nums = [10, 20, 30, 40, 50]
nums[1:4]   # [20, 30, 40]  — index 1 up to (not including) 4
nums[:3]    # [10, 20, 30]  — from beginning up to index 3
nums[2:]    # [30, 40, 50]  — from index 2 to the end
nums[-1]    # 50            — last element; -1 counts from the end
nums[-2:]   # [40, 50]      — last 2 elements

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

# unpack — assign each element to a separate variable in one line
# number of variables must match the number of elements or it crashes
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

## Set Manipulation

```python
# a set stores unique values only — duplicates are automatically ignored
# the main reason to use a set over a list is speed:
# "x in list" scans every element → O(n)
# "x in set" uses a hash lookup → O(1)

# create an empty set — do NOT use {} because that creates a dictionary
seen = set()

# add and remove
seen.add(value)
seen.remove(value)              # crashes if value is missing
seen.discard(value)             # does nothing if value is missing — safer

# check membership — this is the main reason to use a set
if value in seen:               # O(1) regardless of how large the set is

# number of unique values
len(seen)

# set operations — useful for comparing two groups of values
common = set_a & set_b          # intersection: only values that appear in BOTH
combined = set_a | set_b        # union: all values from either
only_a = set_a - set_b          # difference: values in set_a that are NOT in set_b
```

---

## String Manipulation

```python
# strings behave like lists for reading but cannot be changed in place
# to "change" a string you have to build a new one
word = "Hello"
char = word[0]       # "H"  — first character
last_char = word[-1] # "o"  — last character (negative index counts from the end)
part = word[1:4]     # "ell" — characters at index 1, 2, 3 (stops before 4)

# loop through characters
for char in word:

# build a string from pieces — append to a list then join at the end
# this is more efficient than concatenating with += inside a loop
characters = []
characters.append(char)
result = "".join(characters)   # glues all list items into one string with no separator
result = ", ".join(characters) # glues with ", " between each item

# split and combine
words = sentence.split(" ")    # breaks a string apart at every space → returns a list
sentence = " ".join(words)    # joins a list of strings back together with spaces

# searching inside a string
# str.find returns the index of the first match, or -1 if not found
# str.index does the same but crashes if not found — use when you're sure it exists
pos = s.find("#")              # returns -1 if "#" is not in s
pos = s.index("#")            # crashes if "#" is not in s
pos = s.index("#", i)         # same but starts searching from position i, not from 0
                               # critical when you need the NEXT occurrence, not the first

# type conversion — necessary because Python treats text and numbers as different things
# "5" is a string: you can concatenate it but not do math with it
# 5 is an integer: you can do math with it but not use it as a string directly
int("5")                       # "5" → 5    needed when a number was stored as text
str(5)                         # 5 → "5"    needed when you want to build a string from a number
float("3.14")                  # "3.14" → 3.14

# f-strings — embed values directly inside a string without concatenating
# anything inside {} is evaluated and converted to text automatically
f"{len(word)}#{word}"          # e.g. word="Hello" → "5#Hello"
f"index {i} has value {nums[i]}"  # expressions work too

# useful checks
if word.isdigit():             # True if every character is a digit: "123" yes, "12a" no
if char.isalpha():             # True if the character is a letter, False for digits or symbols
if word == word[::-1]:         # palindrome check — reversed string equals original

# convert between cases — these return a NEW string, the original is not changed
word.lower()                   # "Hello" → "hello"
word.upper()                   # "Hello" → "HELLO"
```

---

## Range and Conditions

```python
# range stops BEFORE the second number
range(5)                       # 0, 1, 2, 3, 4
range(2, 5)                    # 2, 3, 4
range(0, 10, 2)                # 0, 2, 4, 6, 8
range(4, -1, -1)               # 4, 3, 2, 1, 0

# combine conditions
if 0 <= i < len(nums):         # i is a valid index
if value in seen and value > 0:
if not nums:                   # list is empty

# conditional expression
larger = a if a > b else b
```

---

## Sorting and Custom Keys

```python
# sort in-place — modifies the original list, returns nothing
nums.sort()

# sort without changing the original — returns a new list
ordered = sorted(nums)

# sort descending
nums.sort(reverse=True)

# sort by a calculated value instead of the element itself
# key= takes a function that transforms each element before comparing
words.sort(key=len)                                        # sort by string length
ordered = sorted(words, key=len, reverse=True)

# lambda — an anonymous one-line function, used when you need a quick transformation
# lambda x: x[1] means "take x, return x[1]"
ordered = sorted(freq_map.items(), key=lambda pair: pair[1])  # sort dict items by count
ordered = sorted(nums, key=lambda x: abs(x))                  # sort by absolute value

# when to use key= vs writing your own loop:
# use key= when you just need to reorder — it's cleaner and faster
# write your own logic when the comparison itself is complex
```

---

## Stack and Heap Syntax

```python
# stack — last in, first out (LIFO)
# use when you need to process things in reverse order, or track "what came before"
# a plain list works as a stack in Python
stack = []
stack.append(value)             # push: add to top
top = stack.pop()               # pop: remove and return from top
top = stack[-1]                 # peek: view top without removing it

# heap — always gives you the smallest (or largest) value first
# use when you repeatedly need the min or max without sorting the whole list
# Python only has min heap built in
import heapq
heap = []
heapq.heappush(heap, value)    # add a value, heap reorders itself automatically
smallest = heapq.heappop(heap) # remove and return the smallest value

# max heap workaround — store values as negatives
# heapq always pops the smallest, so storing -5 means -5 comes out first
# negate again when reading to get the real value back
heapq.heappush(heap, -value)
largest = -heapq.heappop(heap)
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
# ord() gives the Unicode number for a character
# chr() gives the character for a Unicode number
# subtracting ord('a') normalizes so a=0, b=1, ..., z=25
# this lets you use a character as an array index
idx = ord('a')                   # 97
char = chr(97)                   # 'a'
position = ord('c') - ord('a')   # 2  (c is the 3rd letter, 0-indexed)
```
