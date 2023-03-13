---
title: "Testing"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---

## Test your code
```
Finding your bug is a process of confirming the many things that you believe are true — until you find one which is not true.
```
— Norm Matloff

The only thing that people write less than documentation is test code.

Pro-tip: Both documentation and test code is easier to write if you do it as part of the development process.

Ideally:
1. Write function definition and basic docstring
2. Write function contents
3. Write test to ensure that function does what the docstring claims.
4. Update code and/or docstring until (3) is true.

Exhaustive testing is rarely required or useful.
Two main philosophies are recommended:
1. Tests for correctness (eg, compare to known solutions)
2. Tests to avoid re-introducing a bug (regression tests)
