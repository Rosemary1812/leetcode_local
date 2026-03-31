#!/usr/bin/env python3
"""
批量获取题目描述脚本
从 GitHub azl397985856/leetcode 仓库抓取 LeetCode 题目中文描述

使用方法:
    python scripts/fetch_descriptions.py
"""

import re
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

# 高频.md 中的全部题目（共 41 道）
PROBLEM_IDS = [
    128, 11, 15, 42, 3, 560, 239, 53, 56, 54,
    206, 234, 141, 142, 21, 25, 23,
    94, 101, 107, 105, 236, 437,
    200,
    46, 39, 22, 79, 131,
    215, 347,
    70, 198, 213, 337, 309, 121, 122, 123, 322, 139, 300, 5, 1143, 72,
]

# azl397985856/leetcode 仓库中的文件名映射
AZL_FILENAME_MAP = {
    3:    "3.longest-substring-without-repeating-characters.md",
    5:    "5.longest-palindromic-substring.md",
    11:   "11.container-with-most-water.md",
    15:   "15.3sum.md",
    21:   "21.merge-two-sorted-lists.md",
    22:   "22.generate-parentheses.md",
    23:   "23.merge-k-sorted-lists.md",
    25:   "25.reverse-nodes-in-k-groups-en.md",  # 仅英文版
    39:   "39.combination-sum.md",
    42:   "42.trapping-rain-water.md",
    46:   "46.permutations.md",
    53:   "53.maximum-sum-subarray-cn.md",
    54:   "54.spiral-matrix.md",
    56:   "56.merge-intervals.md",
    70:   "70.climbing-stairs.md",
    72:   "72.edit-distance.md",
    79:   "79.word-search-en.md",
    94:   "94.binary-tree-inorder-traversal.md",
    101:  "101.symmetric-tree.md",
    105:  "105.construct-binary-tree-from-preorder-and-inorder-traversal.md",
    107:  "107.binary-tree-level-order-traversal-ii.md",
    121:  "121.best-time-to-buy-and-sell-stock.md",
    122:  "122.best-time-to-buy-and-sell-stock-ii.md",
    123:  "123.best-time-to-buy-and-sell-stock-iii.md",
    128:  "128.longest-consecutive-sequence.md",
    131:  "131.palindrome-partitioning.md",
    139:  "139.word-break.md",
    141:  "141.linked-list-cycle.md",
    142:  "142.Linked-List-Cycle-II.md",
    198:  "198.house-robber.md",
    200:  "200.number-of-islands.md",
    206:  "206.reverse-linked-list.md",
    213:  "213.house-robber-ii.md",
    215:  "215.kth-largest-element-in-an-array.md",
    234:  "234.palindrome-linked-list.md",
    236:  "236.lowest-common-ancestor-of-a-binary-tree.md",
    239:  "239.sliding-window-maximum.md",
    300:  "300.longest-increasing-subsequence.md",
    309:  "309.best-time-to-buy-and-sell-stock-with-cooldown.md",
    322:  "322.coin-change.md",
    337:  "337.house-robber-iii.md",
    347:  "347.top-k-frequent-elements.md",
    437:  "437.path-sum-iii.md",
    560:  "560.subarray-sum-equals-k.md",
    1143: "1143.longest-common-subsequence.md",
}


def fetch_url(url: str, timeout: int = 15) -> Optional[str]:
    """下载 URL 内容，失败返回 None"""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            charset = "utf-8"
            ct = resp.headers.get("Content-Type", "")
            if "charset=" in ct:
                charset = ct.split("charset=")[-1].split(";")[0].strip()
            return resp.read().decode(charset, errors="replace")
    except Exception:
        return None


def fetch_from_azl(pid: int) -> Optional[str]:
    """从 azl397985856/leetcode 仓库获取题目描述"""
    filename = AZL_FILENAME_MAP.get(pid)
    if not filename:
        return None
    url = f"https://raw.githubusercontent.com/azl397985856/leetcode/master/problems/{filename}"
    content = fetch_url(url)
    if content and len(content) > 100:
        return content
    return None


# 内置描述（当 GitHub 仓库找不到时使用）
BUILTIN_DESCRIPTIONS = {
    54: """给定一个 m × n 的矩阵 matrix ，请以顺时针顺序返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]""",

    70: """假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶""",

    72: """给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数。

你可以对一个单词进行如下操作：
- 插入一个字符
- 删除一个字符
- 替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5""",

    105: """给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的前序遍历，inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1：
输入：preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出：[3,9,20,null,null,15,7]

示例 2：
输入：preorder = [-1], inorder = [-1]
输出：[-1]""",

    107: """给你二叉树的根节点 root ，返回其节点值自底向上的层序遍历结果。即按从左到右、从叶到根的顺序，逐层返回每层节点值。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]""",

    123: """给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天买入，第 6 天卖出，利润为 3；然后在第 7 天买入，第 8 天卖出，利润为 3；总利润为 6。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天买入，第 5 天卖出，利润为 4；总利润为 4。

示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在此情况下，不进行任何交易，最大利润为 0。""",

    141: """给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了确定给定链表中没有环，我们使用 pos 表示链表中尾节点的 next 指针指向的索引。如果 pos 是 -1，则链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。""",

    213: """你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有现金。这个地区所有房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻房屋装有防盗系统，如果两间相邻的房屋在同一晚上被闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，今晚能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃房屋 1（金额 = 2），然后偷窃房屋 3（金额 = 2），因为它们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃房屋 1（金额 = 1）和房屋 3（金额 = 3），偷窃总金额 4。

示例 3：
输入：nums = [1,2,3]
输出：3""",

    234: """给你一个单链表 L，判断它是不是回文的。

示例 1：
输入：head = [1,2,2,1]
输出：true

示例 2：
输入：head = [1,2]
输出：false

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？""",

    300: """给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）一些元素而不改变其余元素的顺序。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，所以长度是 4。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1""",

    347: """给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [1,1,1,2,2,3], k = 2
输出：[1,2]

示例 2：
输入：nums = [1], k = 1
输出：[1]

进阶：你能用 O(n log k) 时间复杂度和 O(n) 空间复杂度解决吗？""",

    1143: """给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

子序列是指由原字符串在不改变字符相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，长度为 3。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，长度为 3。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，长度为 0。""",
}


def extract_question_content(markdown: str) -> str:
    """从 Markdown 中提取题目描述部分"""
    if not markdown:
        return ""
    lines = markdown.split("\n")
    result_lines = []
    in_desc = False
    for line in lines:
        stripped = line.strip()
        # 匹配各种标题格式
        if stripped.startswith("## 题目描述") or stripped.startswith("## Description") \
           or stripped.startswith("## Problem Description") or stripped.startswith("## Problem"):
            in_desc = True
            continue
        if in_desc and stripped.startswith("##"):
            break
        if in_desc:
            result_lines.append(stripped)
    content = "\n".join(result_lines).strip()
    # 移除 markdown 代码块标记
    content = re.sub(r"```[\w]*\n?", "", content)
    return content.strip()


def format_for_py(problem_id: int, title_cn: str, title_en: str,
                  difficulty: str, content: str, source_url: str) -> str:
    lines = [
        f"# ===== {problem_id}. {title_cn} =====",
        f"# 难度: {difficulty}",
        f"# 英文名: {title_en}",
        f"# 来源: {source_url}",
        "#",
    ]
    if content:
        for line in content.split("\n"):
            lines.append(f"# {line}")
    else:
        lines.append("# TODO: 请在此处填写题目描述")
    lines.extend([
        "#",
        "# ---------------------------------------------------------",
        "",
        "class Solution:",
        "    def method_name(self, ...):",
        "        # TODO: implement",
        "        pass",
    ])
    return "\n".join(lines) + "\n"


def format_for_js(problem_id: int, title_cn: str, title_en: str,
                  difficulty: str, content: str, source_url: str) -> str:
    lines = [
        f"// ===== {problem_id}. {title_cn} =====",
        f"// 难度: {difficulty}",
        f"// 英文名: {title_en}",
        f"// 来源: {source_url}",
        "//",
    ]
    if content:
        for line in content.split("\n"):
            lines.append(f"// {line}")
    else:
        lines.append("// TODO: 请在此处填写题目描述")
    lines.extend([
        "//",
        "// ---------------------------------------------------------",
        "",
        "function methodName(...) {",
        "    // TODO: implement",
        "}",
    ])
    return "\n".join(lines) + "\n"


# 题目元数据（从 setup.py 复制）
METADATA = {
    3:    {"title_cn": "无重复字符的最长子串",    "title_en": "Longest Substring Without Repeating Characters", "difficulty": "中等"},
    5:    {"title_cn": "最长回文子串",            "title_en": "Longest Palindromic Substring", "difficulty": "中等"},
    11:   {"title_cn": "盛最多水的容器",          "title_en": "Container With Most Water", "difficulty": "中等"},
    15:   {"title_cn": "三数之和",               "title_en": "3Sum", "difficulty": "中等"},
    21:   {"title_cn": "合并两个有序链表",         "title_en": "Merge Two Sorted Lists", "difficulty": "简单"},
    22:   {"title_cn": "括号生成",               "title_en": "Generate Parentheses", "difficulty": "中等"},
    23:   {"title_cn": "合并K个排序链表",         "title_en": "Merge k Sorted Lists", "difficulty": "困难"},
    25:   {"title_cn": "K 个一组翻转链表",        "title_en": "Reverse Nodes in k-Group", "difficulty": "困难"},
    39:   {"title_cn": "组合总和",               "title_en": "Combination Sum", "difficulty": "中等"},
    42:   {"title_cn": "接雨水",                "title_en": "Trapping Rain Water", "difficulty": "困难"},
    46:   {"title_cn": "全排列",                "title_en": "Permutations", "difficulty": "中等"},
    53:   {"title_cn": "最大子数组和",           "title_en": "Maximum Subarray", "difficulty": "中等"},
    54:   {"title_cn": "螺旋矩阵",               "title_en": "Spiral Matrix", "difficulty": "中等"},
    56:   {"title_cn": "合并区间",               "title_en": "Merge Intervals", "difficulty": "中等"},
    70:   {"title_cn": "爬楼梯",                "title_en": "Climbing Stairs", "difficulty": "简单"},
    72:   {"title_cn": "编辑距离",               "title_en": "Edit Distance", "difficulty": "困难"},
    79:   {"title_cn": "单词搜索",               "title_en": "Word Search", "difficulty": "中等"},
    94:   {"title_cn": "二叉树的中序遍历",        "title_en": "Binary Tree Inorder Traversal", "difficulty": "中等"},
    101:  {"title_cn": "对称二叉树",             "title_en": "Symmetric Tree", "difficulty": "简单"},
    105:  {"title_cn": "从前序与中序遍历序列构造二叉树", "title_en": "Construct Binary Tree from Preorder and Inorder Traversal", "difficulty": "中等"},
    107:  {"title_cn": "二叉树的层序遍历 II",     "title_en": "Binary Tree Level Order Traversal II", "difficulty": "中等"},
    121:  {"title_cn": "买卖股票的最佳时机",       "title_en": "Best Time to Buy and Sell Stock", "difficulty": "简单"},
    122:  {"title_cn": "买卖股票的最佳时机 II",    "title_en": "Best Time to Buy and Sell Stock II", "difficulty": "简单"},
    123:  {"title_cn": "买卖股票的最佳时机 III",   "title_en": "Best Time to Buy and Sell Stock III", "difficulty": "困难"},
    128:  {"title_cn": "最长连续序列",           "title_en": "Longest Consecutive Sequence", "difficulty": "困难"},
    131:  {"title_cn": "分割回文串",             "title_en": "Palindromic Partitioning", "difficulty": "中等"},
    139:  {"title_cn": "单词拆分",               "title_en": "Word Break", "difficulty": "中等"},
    141:  {"title_cn": "环形链表",               "title_en": "Linked List Cycle", "difficulty": "简单"},
    142:  {"title_cn": "环形链表 II",            "title_en": "Linked List Cycle II", "difficulty": "中等"},
    198:  {"title_cn": "打家劫舍",               "title_en": "House Robber", "difficulty": "中等"},
    200:  {"title_cn": "岛屿数量",               "title_en": "Number of Islands", "difficulty": "中等"},
    206:  {"title_cn": "反转链表",               "title_en": "Reverse Linked List", "difficulty": "简单"},
    213:  {"title_cn": "打家劫舍 II",            "title_en": "House Robber II", "difficulty": "中等"},
    215:  {"title_cn": "数组中的第K个最大元素",     "title_en": "Kth Largest Element in an Array", "difficulty": "中等"},
    234:  {"title_cn": "回文链表",               "title_en": "Palindrome Linked List", "difficulty": "简单"},
    236:  {"title_cn": "二叉树的最近公共祖先",      "title_en": "Lowest Common Ancestor of a Binary Tree", "difficulty": "中等"},
    239:  {"title_cn": "滑动窗口最大值",           "title_en": "Sliding Window Maximum", "difficulty": "困难"},
    300:  {"title_cn": "最长上升子序列",          "title_en": "Longest Increasing Subsequence", "difficulty": "中等"},
    309:  {"title_cn": "最佳买卖股票时机含冷冻期", "title_en": "Best Time to Buy and Sell Stock with Cooldown", "difficulty": "中等"},
    322:  {"title_cn": "零钱兑换",               "title_en": "Coin Change", "difficulty": "中等"},
    337:  {"title_cn": "打家劫舍 III",           "title_en": "House Robber III", "difficulty": "中等"},
    347:  {"title_cn": "前 K 个高频元素",         "title_en": "Top K Frequent Elements", "difficulty": "中等"},
    437:  {"title_cn": "路径总和 III",           "title_en": "Path Sum III", "difficulty": "中等"},
    560:  {"title_cn": "和为 K 的子数组",         "title_en": "Subarray Sum Equals K", "difficulty": "中等"},
    1143: {"title_cn": "最长公共子序列",          "title_en": "Longest Common Subsequence", "difficulty": "中等"},
}


def slugify(title: str) -> str:
    parts = re.findall(r'[A-Za-z0-9]+', title)
    return "-".join(p.lower() for p in parts)


def main():
    root = Path(__file__).resolve().parent.parent
    high_dir = root / "high"

    print(f"抓取 {len(PROBLEM_IDS)} 道题目的描述...\n")

    success = 0
    failed = []

    for pid in sorted(PROBLEM_IDS):
        meta = METADATA.get(pid, {})
        title_cn = meta.get("title_cn", "")
        title_en = meta.get("title_en", "")
        difficulty = meta.get("difficulty", "中等")
        folder = high_dir / f"{pid:03d}"

        # 读取现有文件头部信息
        py_file = folder / "solution.py"
        if py_file.exists():
            content = py_file.read_text(encoding="utf-8")
            m = re.search(r"难度:\s*(.+)", content)
            if m:
                difficulty = m.group(1).strip()
            m = re.search(r"英文名:\s*(.+)", content)
            if m:
                title_en = m.group(1).strip()
            m = re.search(r"===\s*\d+\.\s*(.+?)\s*===", content)
            if m:
                title_cn = m.group(1).strip()

        source_url = f"https://leetcode.cn/problems/{slugify(title_en)}/description/"

        # 抓取描述
        raw = fetch_from_azl(pid)
        if raw:
            content = extract_question_content(raw)
        elif pid in BUILTIN_DESCRIPTIONS:
            content = BUILTIN_DESCRIPTIONS[pid]
        else:
            content = ""

        # 写入文件
        py_content = format_for_py(pid, title_cn, title_en, difficulty, content, source_url)
        js_content = format_for_js(pid, title_cn, title_en, difficulty, content, source_url)

        py_file.write_text(py_content, encoding="utf-8")
        (folder / "solution.js").write_text(js_content, encoding="utf-8")

        if content:
            print(f"  [OK] {pid:3d} | {title_cn}")
            success += 1
        else:
            print(f"  [--] {pid:3d} | {title_cn} (未获取到描述)")
            failed.append(pid)

        time.sleep(0.3)  # 避免触发 GitHub 限流

    print(f"\n完成！成功 {success}/{len(PROBLEM_IDS)} 道")
    if failed:
        print(f"未获取到描述的题目: {failed}")


if __name__ == "__main__":
    main()
