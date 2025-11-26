Analyze complexity for this code/approach: $ARGUMENTS

## Analysis Framework

### 1. Time Complexity
- **What's the Big-O?** Count operations, identify the dominant term
- **Why?** Trace through: "For input size n, how many times does each loop/recursion run?"
- **Mathematical reasoning**: Use logarithms (for divide & conquer), combinatorics (for backtracking)

### 2. Space Complexity
- **Auxiliary space**: What extra memory beyond input? (hash maps, arrays, etc.)
- **Call stack**: For recursion, what's the maximum depth?
- **In-place vs not**: Does it modify input or create new structures?

### 3. Challenge Me First
Before confirming my analysis:
- Ask what I think the complexity is
- If wrong, explain with concrete numbers (e.g., "nested loop over n=1000 items = 1,000,000 iterations")

### 4. Trade-off Analysis (The Third Pillar)
- **Can we trade space for time?** (memoization, hash maps)
- **Can we trade time for space?** (two pointers vs hash set)
- **What's the theoretical lower bound?** (comparison sort = Ω(n log n), search in unsorted = Ω(n))

### 5. Pattern Connection
- Which of the 26 patterns does this use?
- How does complexity compare to alternative patterns for same problem?

Use analogies: "This is like a football manager checking every possible formation (n!) vs having a shortlist of proven tactics (constant)"
