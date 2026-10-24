# Learning DSA in C++

A starting plan for the week of **26 October 2026**.

The goal: understand the idea, implement it clearly, and explain why it works.
Move on when a topic makes sense; the phases below are not weekly deadlines.

## 1. Get comfortable with the language

- Values, types, references, functions, scope, and `const`.
- Input/output, compilation, warnings, and reading compiler errors.
- `std::vector`, `std::string`, iterators, and range-based loops.
- `std::sort`, `std::lower_bound`, maps, sets, stacks, and queues.
- Time and space complexity; when a container copies, grows, or invalidates an iterator.

Practice ideas: frequency counting, removing duplicates, finding a pair with a
specified sum, and comparing a simple solution with a faster one.

## 2. Build a foundation

- Arrays and strings: two pointers, sliding windows, and prefix sums.
- Searching and sorting: binary search, comparison sorts, and boundary cases.
- Recursion and backtracking: base cases, state, and the call stack.
- Linked lists, stacks, and queues: implement the basics, then compare them with
  the standard library's containers.

For each topic, write down the invariant or key observation before optimizing.

## 3. Connect the ideas

- Trees and binary search trees: traversals and recursive structure.
- Heaps: priority queues and selecting the next best candidate.
- Graphs: representations, breadth-first search, and depth-first search.
- Dynamic programming: define a state, derive a transition, then compare
  memoization and tabulation.

## A useful practice loop

1. Restate the problem and its constraints in plain language.
2. Work through a small example by hand.
3. Write the simplest correct solution you can explain.
4. Identify the bottleneck and choose a better approach when needed.
5. Implement it in C++ and check edge cases.
6. Record time and space complexity, the key idea, and one mistake to remember.
7. Revisit it later without copying the previous solution.

A short note for each exercise is enough:

```text
Problem / source:
Key observation:
Approach:
Time:
Extra space:
Edge cases checked:
What I would change next time:
```

Useful edge cases include empty input where allowed, one element, duplicates,
negative values, already sorted input, and values near the problem's limits.
Use small counterexamples to challenge an explanation rather than relying only
on a few passing examples.

[Back to the profile](../README.md#learning)
