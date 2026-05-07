# /explain-cn

用中文解释技术概念。

## Rules

- 使用精确的技术术语，不要营销词汇或模糊表达
- 匹配用户现有笔记的语言风格
- 可以夹杂英文术语（如 compaction、subagent、sliding window）
- 代码注释保持英文
- 如果用户提供了代码或文件，先读懂再解释，不要凭印象回答

## Usage

```
/explain-cn <topic or file_path>
```

## Examples

- `/explain-cn .claude/compaction pipeline` — 解释 compaction 的实现
- `/explain-cn notes/leetcode/560.md` — 用中文解释这道题的思路
- `/explain-cn high/025/solution.py` — 解释这段代码的逻辑
