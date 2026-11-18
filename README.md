# LeetCode

My personal repository of [LeetCode](https://leetcode.com/) problems: my solutions, notes on how it works, and more efficient alternative solutions I found afterwards.

## Structure

Problems are grouped by difficulty. Each problem has its own folder, named with the number LeetCode assigns to it plus its title.

```
leetcode/
├── README.md
├── easy/
│   ├── 0001-two-sum/
│   │   ├── solution.py
│   │   ├── extra_solution.py
│   │   └── notes.md (if they or the code are too big to fit)
│   └── 0009-palindrome-number/
│       ├── ...
├── medium/
└── hard/
```

### What each folder contains

| File | Description |
|---|---|
| `solution.py` | My solution, the one I solved on my own. |
| `extra_solution.py` | Solutions I found that may be more efficient, but that I did **not** solve myself. |
| `notes.md` | Key ideas, the pattern used, edge cases, complexity, and what I learned. |

If a problem has no `extra_solution.py`, it means I haven't found (or haven't reviewed) a better alternative.

Each problem lists its tags in the tables below and in the header of its `notes.md`.

## Conventions

- **Language:** Python 3.
- **Complexity:** written in Big O notation (for example `O(n)`), without constants.

## Problem Index

### Easy

| # | Problem | Tags | Status | Solution | Notes |
|---|---|---|---|---|---|
| 1 | Two Sum | `Array` `Hash Table` | 💡 | [solution.py](easy/0001-two-sum/solution.py) | [notes.md](easy/0001-two-sum/notes.md) |
| 9 | Palindrome Number | `Math` | 💡 | [solution.py](easy/0009-palindrome-number/solution.py) | [notes.md](easy/0009-palindrome-number/notes.md) |

## Progress

| Difficulty | Solved |
|---|---|
| Easy | 2 |
| Medium | 0 |
| Hard | 0 |
| **Total** | **2** |

## `notes.md` Template

```markdown
# 0000 - Problem Title

- **Difficulty:** Easy / Medium / Hard
- **Tags:** Tag1, Tag2
- **Link:** https://leetcode.com/problems/...

## Idea
A few lines explaining how I solved it.

## Complexity
- Time: O(...)
- Space: O(...)

## Edge Cases
- ...

## More Efficient Alternative (if any)
What it does differently, why it is better, and where I found it.

## What I Learned
- ...
```

## Adding a New Problem

1. Create the folder under the matching difficulty: `easy/0000-problem-name/`.
2. Save my solution in `solution.py`.
3. Write `notes.md` using the template above.
4. If I find a better solution, save it in `extra_solution.py` and cite the source.
5. Add the row to the table for its difficulty and update the progress table.