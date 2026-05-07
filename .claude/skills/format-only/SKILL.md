# /format-only

Reformat the specified file WITHOUT changing any content.

## Rules

- Only modify: headings, spacing, callouts, tables, lists, indentation
- Do NOT: add, remove, or reword any text
- Do NOT: merge or split paragraphs
- Do NOT: change word choice or sentence structure
- If a formatting decision could alter meaning (e.g., turning a sentence into a list changes emphasis), ask before acting

## Usage

```
/format-only <file_path>
```

## Examples

- `/format-only notes/leetcode/560.md` — reformat a LeetCode note
- `/format-only docs/architecture.md` — clean up document structure
