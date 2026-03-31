# LeetCode 刷题笔记生成器

为每道 LeetCode 题目生成一份结构化 Markdown 笔记，保存为文件。

---

## 输出文件格式

保存路径：`D:\coding\leetcode\high\{题号:03d}\notes\{题号}-{英文短标题}.md`

---

## Markdown 模板

```markdown
---
tags: leetcode
difficulty: {难度}
created: {YYYY-MM-DD}
---

# {题号}. {中文题目名}

## 题目描述

{题目原文，保留示例和提示，格式化为 Markdown}

---

## 思路

使用 **{方法名}**。

{2-4 句核心思路说明，可加决策树 / 示意图辅助理解}

> 其他思路：{一句话简要提及其他做法及其取舍，不展开}

---

## 复杂度分析

**时间复杂度：O(...)**

{推导过程：分点说明搜索空间、每步开销、总结公式，3-5 行}

**空间复杂度：O(...)**

{推导过程：说明递归栈、辅助数组等，2-3 行}

---

## 测试集

### 基础用例

```javascript
输入: {示例1输入}
输出: {示例1输出}
解释: {示例1解释}
```

```javascript
输入: {示例2输入}
输出: {示例2输出}
解释: {示例2解释}
```

### 边界用例

```javascript
// 空数组 / 单元素 / 全相同 / 全不同
输入: {边界输入}
输出: {边界输出}
```

### 扩展用例（可选）

```javascript
// 大规模输入、特殊格式等
输入: {扩展输入}
输出: {扩展输出}
```

---

## JavaScript 题解

```javascript
/**
 * @param {输入类型} 参数名
 * @return {返回类型}
 */
var 函数名 = function(参数) {
    // 适量注释，说明关键步骤
};
```

---

## Python 题解

```python
from typing import ...

class Solution:
    def 函数名(self, 参数: 类型) -> 返回类型:
        # 使用最 Pythonic 的写法
        # 适量注释
        pass
```

> {如果 Python 写法与 JS 有明显差异（如省去 used 数组、用切片等），在这里一句话说明取舍}

---

## 本地测试脚本

```python
# tests/test_{题号}.py
import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic(self):
        # 基础用例
        ...

    def test_boundary(self):
        # 边界用例
        ...

if __name__ == "__main__":
    unittest.main()
```

---

## 写作规范

**思路部分**
- 开头直接点明核心方法（回溯、动态规划、双指针……）
- 用 2-4 句话说清楚"为什么这样做"和"怎么做"
- 如果有决策树或状态转移图能帮助理解，用代码块画出来
- 用 `>` 引用块简要提一句其他思路，不展开实现

**测试集部分**
- 基础用例：来自题目官方的示例，确保每个都有
- 边界用例：空数组、单元素、全相同值、全不同值等
- 扩展用例：大规模输入、特殊格式（可选）
- 每条测试用例注明输入、输出、必要时加解释

**复杂度分析**
- 分时间 / 空间两部分，各自给出推导过程
- 时间：先说搜索空间（排列数、状态数等），再说每步开销，最后给结论
- 空间：说明递归栈深度、辅助数据结构，是否计入输出
- 结论用加粗 `**O(...)**` 标出

**JavaScript 题解**
- 保留 LeetCode 标准函数签名注释
- 注释量：关键步骤一句话，不逐行注释
- 变量命名清晰，逻辑分层

**Python 题解**
- 优先使用最 Pythonic 的写法（列表推导、切片、itertools 等）
- 如果 Pythonic 写法有额外开销（如每次创建新列表），在题解后用 `>` 说明
- 加 `from typing import ...` 类型注解

---

## 执行步骤

1. 从 `high/{题号}/solution.py` 或 `solution.js` 读取用户已有代码
2. 从 `high/{题号}/solution.py` 头部注释读取题目描述
3. 提取题号、中文名、英文名、难度
4. 判断用户是否提供了题解：
   - **有题解**：保留原有逻辑和变量命名，整理格式、补充注释、修正 bug，不替换为其他写法
   - **无题解**：生成最简洁的解法，优先可读性，避免过度优化
5. 根据题目描述构造测试集（基础 + 边界，2-5 条）
6. 按模板生成完整 Markdown 内容
7. 获取当前日期填入 `created` 字段（格式 `YYYY-MM-DD`）
8. 将文件保存为 `D:\coding\leetcode\high\{题号:03d}\notes\{题号}-{英文标题}.md`
9. 用 `present_files` 工具把文件呈现给用户
