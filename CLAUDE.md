# CLAUDE.md

## Overview
DSA practice repository - Python solutions organized by problem name. Goal: FAANG-ready in 24 months through deep understanding, not memorization.

---

## First Principles: What Coding Interviews Actually Measure

> The fundamental question: What is a coding interview really testing?
> **Not** "can you solve problem X without ever seeing it before."

### The Three Pillars Being Evaluated

1. **Pattern Recognition** — Can you recognize the problem type and apply the appropriate algorithm?
2. **Communication** — Can you explain your reasoning clearly to the interviewer?
3. **Trade-off Analysis** — Do you understand time/space complexity and alternatives?

### The 2025 Reality: AI Has Changed Everything

The landscape has fundamentally shifted. [Meta now uses AI-enabled coding interviews](https://www.hellointerview.com/blog/meta-ai-enabled-coding) where candidates have access to AI assistants. This tests whether you can **direct AI effectively**, not just code from scratch.

**What this means for preparation:**
- Pure memorization is now worthless — AI can recall solutions instantly
- **Understanding WHY** algorithms work becomes critical — you must validate AI output
- Communication and trade-off analysis matter MORE than ever
- [Code review skills](https://www.linkedin.com/pulse/interviews-age-ai-ditch-leetcode-try-code-reviews-instead-chen) are becoming interview criteria
- [System design emphasis is increasing](https://www.designgurus.io/blog/system-design-interview-guide-2025) at all levels

Sources: [HackerRank 2025 Report](https://www.hackerrank.com/writing/ai-coding-interviews-what-recruiters-should-know), [Blind Discussion](https://www.teamblind.com/post/companies-moving-away-from-leetcode-interviews-with-ai-on-the-rise-uvcz2o31)

---

## Computational Thinking: The Deep Foundation

Before patterns, master the **mental operating system** for problem-solving.

### The Four Components (from CS Education Research)

| Component | What It Means | Interview Application |
|-----------|---------------|----------------------|
| **Decomposition** | Break complex problems into smaller parts | "Let me break this into subproblems..." |
| **Pattern Recognition** | Identify similarities with known problems | "This reminds me of..." |
| **Abstraction** | Focus on relevant details, ignore noise | "The key insight here is..." |
| **Algorithm Design** | Create step-by-step solutions | "My approach would be..." |

Source: [OpenStax Computational Thinking](https://openstax.org/books/introduction-computer-science/pages/2-1-computational-thinking)

### Pólya's Problem-Solving Framework

George Pólya's 1945 classic "[How to Solve It](https://en.wikipedia.org/wiki/How_to_Solve_It)" remains the gold standard:

1. **Understand the problem** — What are inputs? Outputs? Constraints? Edge cases?
2. **Devise a plan** — Which pattern applies? What's the brute force? Can we optimize?
3. **Carry out the plan** — Implement carefully, test with examples
4. **Look back** — Can we verify? Simplify? Use this solution elsewhere?

> "Many questions on StackOverflow are written by people who started 'solving' before understanding the problem." — Applies equally to interviews!

---

## The 26 Essential Patterns

Master these patterns from [Grokking the Coding Interview](https://www.designgurus.io/course/grokking-the-coding-interview) and [Sean Prashad's LeetCode Patterns](https://seanprashad.com/leetcode-patterns/):

### Array/String Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **Sliding Window** | Contiguous subarray/substring problems | "maximum/minimum subarray of size k" |
| **Two Pointers** | Sorted arrays, pairs, partitioning | "find pair that sums to X" |
| **Prefix Sum** | Range sum queries, subarray sums | "sum between index i and j" |

### Linked List Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **Fast & Slow Pointers** | Cycle detection, middle element | "detect cycle", "find middle" |
| **In-place Reversal** | Reverse without extra space | "reverse linked list" |

### Tree/Graph Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **BFS** | Level-order, shortest path (unweighted) | "minimum steps", "level by level" |
| **DFS** | Path finding, exhaustive search | "all paths", "does path exist" |
| **Topological Sort** | Dependency ordering | "course prerequisites", "build order" |
| **Union-Find** | Connected components, grouping | "number of islands", "friend circles" |

### Search Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **Binary Search** | Sorted data, search space reduction | "sorted array", "minimize maximum" |
| **Modified Binary Search** | Rotated arrays, finding boundaries | "rotated sorted", "first/last occurrence" |

### Dynamic Programming Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **0/1 Knapsack** | Choose/not choose with constraint | "maximum value with capacity" |
| **Unbounded Knapsack** | Unlimited choices | "coin change", "rod cutting" |
| **Fibonacci Style** | Current depends on previous states | "climbing stairs", "house robber" |
| **Longest Common Subsequence** | Two sequences comparison | "edit distance", "longest common" |
| **Palindrome** | String symmetry problems | "longest palindromic substring" |

### Heap Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **Top K Elements** | K largest/smallest | "k most frequent", "k closest" |
| **Two Heaps** | Median tracking, scheduling | "find median from stream" |
| **K-way Merge** | Merge sorted lists | "merge k sorted lists" |

### Other Essential Patterns
| Pattern | When to Use | Key Signal |
|---------|-------------|------------|
| **Merge Intervals** | Overlapping ranges | "merge meetings", "insert interval" |
| **Cyclic Sort** | Numbers in range [1, n] | "find missing number", "find duplicate" |
| **Backtracking** | Generate all combinations/permutations | "all possible", "generate all" |
| **Subsets/Combinations** | Power set, combinations | "all subsets", "combination sum" |
| **Bitwise XOR** | Single number problems | "element appearing once" |
| **Monotonic Stack** | Next greater/smaller element | "next greater element", "largest rectangle" |
| **Trie** | Prefix matching, autocomplete | "word search", "prefix match" |

### Pattern Recognition Heuristics

```
If input array is sorted → Binary Search or Two Pointers
If asked for all permutations/subsets → Backtracking
If given a tree → DFS or BFS
If given a graph → BFS, DFS, or Union-Find
If recursion is banned → Use Stack
If must solve in-place → Swap or Store multiple values in pointer
If asked for maximum/minimum subarray → Dynamic Programming or Sliding Window
If asked for top/least K items → Heap
If asked for common strings → HashMap or Trie
```

Source: [14 Patterns to Ace Any Coding Interview](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

---

## Mathematical Prerequisites

Based on [CS education research](https://math.stackexchange.com/questions/198955/prerequisite-mathematics-for-studying-data-structures-and-algorithms):

### Must-Know Fundamentals
- **Logarithms** — Understand why binary search is O(log n)
- **Mathematical Induction** — Essential for proving recursive algorithm correctness
- **Basic Probability** — For randomized algorithms, hashing analysis
- **Modular Arithmetic** — For many number theory problems
- **Combinatorics basics** — Permutations, combinations (for backtracking analysis)

### Discrete Math Concepts (Learn as Needed)
- **Graph Theory** — Trees, cycles, connectivity, paths
- **Recurrence Relations** — Analyzing recursive algorithms
- **Proof Techniques** — Contradiction, induction for algorithm correctness

Recommended: [Concrete Mathematics by Knuth](https://www.amazon.com/Concrete-Mathematics-Foundation-Computer-Science/dp/0201558025)

---

## Data Structure Decision Framework

### When to Use What

| Need | Best Choice | Time | Space | Trade-off |
|------|-------------|------|-------|-----------|
| Fast random access | Array | O(1) access | O(n) | Fixed size, expensive insert/delete |
| Frequent insert/delete | Linked List | O(1) at ends | O(n) | No random access |
| Fast search + insert + delete | Hash Table | O(1) average | O(n) | No ordering, hash collisions |
| Ordered data + all operations | Balanced BST | O(log n) | O(n) | Complex implementation |
| Priority access | Heap | O(log n) insert/extract | O(n) | Only min/max efficient |
| Prefix operations | Trie | O(k) for k-length key | O(ALPHABET * n) | Memory heavy |

### The Time-Space Trade-off Principle

> "If your problem takes long time but not much memory, spend memory to speed it up. If it's fast but memory-heavy, trade time for space."

Classic examples:
- **Memoization** — Store computed results (more space, less time)
- **Two Pointers** — Avoid hash map (less space, same time)
- **Lookup Tables** — Precompute values (more space, less time)

Source: [GeeksforGeeks Time-Space Trade-off](https://www.geeksforgeeks.org/dsa/time-space-trade-off-in-algorithms/)

---

## Learning Resources Hierarchy

### Pattern-Based Learning (Primary)
1. [Grind 75](https://www.techinterviewhandbook.org/grind75/faq) — Curated list by Blind 75 author
2. [Sean Prashad's LeetCode Patterns](https://seanprashad.com/leetcode-patterns/) — 170+ problems by pattern
3. [Grokking the Coding Interview](https://www.designgurus.io/course/grokking-the-coding-interview) — Pattern explanations with problems

### System Design (For L4+)
1. [ByteByteGo](https://bytebytego.com/) — Visual system design
2. [Grokking System Design](https://www.designgurus.io/blog/system-design-interview-guide-2025) — Structured approach

### Deep Understanding
1. "How to Solve It" by Pólya — Problem-solving methodology
2. "Concrete Mathematics" by Knuth — Mathematical foundations
3. CLRS "Introduction to Algorithms" — When you need the theory

---

## Important: Learning Mode Active

**DO NOT run Python files directly.** Instead:
1. Review code and spot potential bugs FIRST
2. If bugs exist, STOP - ask me to find/fix before continuing
3. Confirm expected output (no need for full trace unless I ask)

For detailed line-by-line tracing, I'll use `/dry-run`

## Teaching Style

When explaining DSA concepts:
1. **First principles first** - What problem does this algorithm solve? Why does it exist?
2. **Trace through example** - Walk through with specific small inputs before Big-O
3. **Trade-offs** - Time vs Space, when to use vs alternatives
4. **Pattern recognition** - Connect to similar problems I've solved

Use analogies from: football tactics (formations = data structures, plays = algorithms), web dev (caching = memoization, load balancing = partitioning)

## When I Get Stuck
- Don't give full solution immediately
- Give progressive hints (pattern → approach → pseudocode → code)
- Ask "what have you tried?" before solving

## Code Review Checklist
After I write solution, check:
- Edge cases (empty input, single element, duplicates)
- Time/Space complexity - challenge if I'm wrong
- Cleaner Pythonic alternatives
- Follow-up: "How would you optimize if...?"

## Structure
```
<problem_folder>/<problem_name>.py
```

## Custom Commands & Workflow

### How Commands Work Together

```
Problem arrives
     ↓
/hint → Pattern recognition (Level 1-4 progressive)
     ↓
You attempt solution
     ↓
/dry-run → Trace without executing (Pólya's framework)
     ↓
/complexity → Analyze time/space trade-offs
     ↓
/why → Justify your approach vs alternatives
     ↓
/quiz → Test your understanding (all 3 pillars)
     ↓
/explain → Deep dive if concept unclear
```

### Command Reference

| Command | Purpose | Maps To |
|---------|---------|---------|
| `/hint [problem]` | Progressive hints without spoiling | Pattern Recognition (Pillar 1) |
| `/dry-run [code]` | Trace execution without running | Pólya's Framework |
| `/complexity [code]` | Analyze Big-O with trade-offs | Trade-off Analysis (Pillar 3) |
| `/why` | Justify approach vs alternatives | First Principles + 2025 AI Lens |
| `/quiz [topic]` | Test understanding across all pillars | All Three Pillars |
| `/explain [concept]` | Deep dive using computational thinking | The Four Components |

## Quick Commands
- `python <folder>/<file>.py` - But prefer dry-run over actual execution
