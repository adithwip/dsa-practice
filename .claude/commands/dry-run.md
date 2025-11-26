Trace through this code WITHOUT executing:

$ARGUMENTS

## Pólya's Framework Applied

### Step 1: Understand the Problem
- What are the inputs? What are expected outputs?
- State the small test cases you'll use (n=3-5 elements)
- What edge cases should we consider? (empty, single element, duplicates)

### Step 2: Devise the Plan (Pattern Recognition)
- What pattern does this code implement? (sliding window, two pointers, DFS, etc.)
- Is this the right pattern for this problem?

### Step 3: Carry Out the Plan (Line-by-Line Trace)

**Format for each significant step:**
```
Line X: [code snippet]
  → variable_name = value
  → [brief explanation of what happened]
```

**If you spot a bug: STOP immediately**
- Point out the suspicious line
- Ask me: "What do you think happens when [specific case]?"
- Let me find and fix it before continuing

### Step 4: Look Back
- **Verify**: Does the output match expected for all test cases?
- **Complexity**: Time O(?) and Space O(?) with reasoning
- **Optimize**: Could a different pattern solve this more efficiently?
- **Generalize**: What similar problems could this approach solve?

## Output Format
```
Input: [your test case]
────────────────────────
[line-by-line trace]
────────────────────────
Output: [result]
Complexity: Time O(?), Space O(?)
Pattern Used: [pattern name]
```
