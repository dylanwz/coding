# Array Methods
Array methods involve <mark style="background-color:#E5CCFF80">different ways of iterating over an array</mark> in order to achieve a goal. They often result in $O(n)$ solutions.

The methods include:
- hash maps: reduce sub-searches into lookups,
- prefix sum: reduce summing an interval into lookups,
- binary search: reduce full searches to log time,
- pointer methods: reduce location searches into lookups,
- sliding window: .

### Hash Maps
The idea is to <mark style="background-color:#CCE5FF80">reduce searches into lookups</mark>.

<mark style="background-color:#f9e79f80">Example</mark>: <mark style="background-color:#f9e79f80">Two Sum</mark><br>Return the number of pairs of numbers that sum to k.

```
hashmap = {} // prefix sum base case
count = 0

for n in array:
    num_needed = k - n
    if hashmap[num_needed] > 0:
        count += hashmap[num_needed]
    hashmap[n] += 1

return count
```

### Prefix Sum
The idea is to <mark style="background-color:#CCE5FF80">reduce summing an interval into lookups</mark>.

<mark style="background-color:#f9e79f80">Example</mark>: <mark style="background-color:#f9e79f80">Subarray Sum Equals K</mark><br>Given an array of integers, return the number of subarrays whose sum equals k.

```
count = 0
prefixSum = 0
hashmap = {0: 1} // prefix sum base case

for each number in array:
    prefixSum += number
    if (prefixSum - k) in hashmap:
        count += hashmap[prefixSum - k]
    hashmap[prefixSum] += 1 (or initialize to 1 if not exists)

return count
```

### Difference Arrays
The idea is to <mark style="background-color:#f9e79f80">sreduce range updates to constant-time</mark>.

<mark style="background-color:#f9e79f80">Example</mark>: <mark style="background-color:#f9e79f80">Zero Array Transformation</mark><br>Given an array of integers and a series of queries `[ql, qr]` where all indices between `ql` and `qr` are decremented by one, return whether the remaining array is all zeros.

```python
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n+1)

        for q in queries:
            ql = q[0]
            qr = q[1]
            diff[ql] += 1
            diff[qr + 1] -= 1
        
        # turn it into a prefix-sum
        for idx in range(1, n+1):
            diff[idx] = diff[idx - 1] + diff[idx]

        for idx in range(n):
            if (nums[idx] - diff[idx]) > 0:
                return False
        
        return True
```

| i | diff\[i] | prefix sum |
| - | -------- | ---------- |
| 0 | 0        | 0          |
| 1 | +1       | 1          |
| 2 | 0        | 1          |
| 3 | 0        | 1          |
| 4 | -1       | 0          |
| 5 | 0        | 0          |


### Binary Search
The idea is to <mark style="background-color:#CCE5FF80">perform monotonic searches in logarithmic time</mark>.

<mark style="background-color:#f9e79f80">Implementation</mark>:

```
low = 0
high = n - 1

while low <= high:
    m = low + floor((high - low)/2)
    if array[m] < target then:
        low = m + 1
    else if array[m] > target then:
        high = m - 1
    else:
        return m
```

### Pointer Methods
The idea is to <mark style="background-color:#CCE5FF80">maintain pointers to different positions</mark> in array that iterate and walk in different ways, e.g. at different speeds or over specific intervals.

<mark style="background-color:#f9e79f80">Example</mark>: <mark style="background-color:#f9e79f80">Sort Colours</mark><br>Given an array of red, white and blue objects, sort the array in-place so that the objects are in that order.

```
red_idx = 0
        white_idx = 0
        blue_idx = len(nums) - 1

        while (white_idx <= blue_idx):
            if nums[white_idx] == 0:
                 temp = nums[red_idx]
                 nums[red_idx] = nums[white_idx]
                 nums[white_idx] = temp

                 red_idx += 1
                 white_idx += 1
            else if nums[white_idx] == 1:
                white_idx += 1
            else:
                temp = nums[white_idx]
                nums[white_idx] = nums[blue_idx]
                nums[blue_idx] = temp

                blue_idx -= 1
```
Pointers indicate where the last red/white/blue colour was.

### Sliding Window
The idea is to <mark style="background-color:#CCE5FF80">maintain a subarray of fixed size with desired properties</mark>.