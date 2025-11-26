# Two Sum - Learning Session Notes

## Problem Summary
Given an array of integers and a target, return indices of two numbers that sum to target.
- Each input has exactly one solution
- Cannot use same element twice

## Solutions Developed

### Solution 1: Two-Pass Hashmap
```python
def two_sum_first_solution(self, list: List[int], target: int):
    hashmap = {}

    # Pass 1: Build hashmap (num → index)
    for i, num in enumerate(list):
        hashmap[num] = i

    # Pass 2: Find complement
    for i, num in enumerate(list):
        desired = target - num
        if desired in hashmap and hashmap[desired] != i:
            return [hashmap[desired], i]
```

**Bug Fixed**: Originally had `else: return []` inside loop → caused early exit on first iteration.

### Solution 2: Single-Pass Hashmap
```python
def two_sum_second_solution(self, list: List[int], target: int):
    hmap = {}

    for i, num in enumerate(list):
        desired = target - num

        if desired in hmap and hmap[desired] < i:
            return [i, hmap[desired]]
        else:
            hmap[num] = i
```

**Bug Fixed**: Originally stored `hmap[desired] = i` instead of `hmap[num] = i`.

## Key Insights

### Why `!= i` vs `< i` Are Equivalent (Single-Pass)

**Loop Invariant**: In single-pass, we only store indices *before* current `i`.

```
Timeline visualization:
i=0: hmap = {}           → check, then store 0
i=1: hmap = {0}          → check, then store 1
i=2: hmap = {0,1}        → check, then store 2
```

When checking at index `i`, hmap only contains indices `{0, 1, ..., i-1}`.
Therefore `hmap[desired]` is ALWAYS `< i`, making both checks equivalent.

### Why Two-Pass Needs `!= i` Check

For duplicates like `[3, 3]` with target `6`:
- Hashmap after Pass 1: `{3: 1}` (second 3 overwrites first)
- Pass 2 at i=0: desired=3, `hmap[3]=1`, and `1 != 0` ✓
- Without check: `[3]` target `6` would incorrectly match index 0 with itself

### Python Concepts Learned

**`self` keyword**: Explicit instance reference (like implicit `this` in JS)
```python
class Solution:
    def method(self):  # self = the instance calling this method
        pass
```

**`enumerate()`**: Returns (index, value) pairs
```python
for i, num in enumerate([2, 7, 11]):
    # i=0,num=2 → i=1,num=7 → i=2,num=11
```

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Brute Force (nested loops) | O(n²) | O(1) |
| Two-Pass Hashmap | O(n) | O(n) |
| Single-Pass Hashmap | O(n) | O(n) |

## Test Cases to Remember

| Input | Target | Output | Why |
|-------|--------|--------|-----|
| `[2,7,11,15]` | 9 | `[0,1]` | Basic case |
| `[3,2,4]` | 6 | `[1,2]` | Answer not at start |
| `[3,3]` | 6 | `[0,1]` | Duplicate values |

## Next Steps
- [ ] Practice similar hashmap problems (3Sum, 4Sum)
- [ ] Try solving without hashmap (two-pointer on sorted array)
