#!/usr/bin/env python3
"""
批量创建所有题目文件夹（不依赖 leetcode-cli）
使用内置题库元数据创建文件夹和 solution 文件

使用方法:
    python scripts/setup.py
"""

from pathlib import Path


# 高频.md 中的全部题目（共 41 道）
BUILTIN_METADATA = {
    # 哈希
    128: {"title_cn": "最长连续序列",         "difficulty": "困难", "title_en": "Longest Consecutive Sequence"},

    # 双指针
    11:  {"title_cn": "盛最多水的容器",        "difficulty": "中等", "title_en": "Container With Most Water"},
    15:  {"title_cn": "三数之和",              "difficulty": "中等", "title_en": "3Sum"},
    42:  {"title_cn": "接雨水",               "difficulty": "困难", "title_en": "Trapping Rain Water"},

    # 滑动窗口
    3:   {"title_cn": "无重复字符的最长子串",    "difficulty": "中等",
          "title_en": "Longest Substring Without Repeating Characters"},

    # 子串
    560: {"title_cn": "和为 K 的子数组",       "difficulty": "中等", "title_en": "Subarray Sum Equals K"},
    239: {"title_cn": "滑动窗口最大值",         "difficulty": "困难", "title_en": "Sliding Window Maximum"},

    # 普通数组
    53:  {"title_cn": "最大子数组和",          "difficulty": "中等", "title_en": "Maximum Subarray"},
    56:  {"title_cn": "合并区间",              "difficulty": "中等", "title_en": "Merge Intervals"},

    # 矩阵
    54:  {"title_cn": "螺旋矩阵",              "difficulty": "中等", "title_en": "Spiral Matrix"},

    # 链表
    206: {"title_cn": "反转链表",              "difficulty": "简单", "title_en": "Reverse Linked List"},
    234: {"title_cn": "回文链表",              "difficulty": "简单", "title_en": "Palindrome Linked List"},
    141: {"title_cn": "环形链表",              "difficulty": "简单", "title_en": "Linked List Cycle"},
    142: {"title_cn": "环形链表 II",           "difficulty": "中等", "title_en": "Linked List Cycle II"},
    21:  {"title_cn": "合并两个有序链表",        "difficulty": "简单", "title_en": "Merge Two Sorted Lists"},
    25:  {"title_cn": "K 个一组翻转链表",        "difficulty": "困难", "title_en": "Reverse Nodes in k-Group"},
    23:  {"title_cn": "合并K个排序链表",        "difficulty": "困难", "title_en": "Merge k Sorted Lists"},

    # 二叉树
    94:  {"title_cn": "二叉树的中序遍历",        "difficulty": "中等", "title_en": "Binary Tree Inorder Traversal"},
    101: {"title_cn": "对称二叉树",             "difficulty": "简单", "title_en": "Symmetric Tree"},
    107: {"title_cn": "二叉树的层序遍历 II",     "difficulty": "中等",
          "title_en": "Binary Tree Level Order Traversal II"},
    105: {"title_cn": "从前序与中序遍历序列构造二叉树", "difficulty": "中等",
          "title_en": "Construct Binary Tree from Preorder and Inorder Traversal"},
    236: {"title_cn": "二叉树的最近公共祖先",      "difficulty": "中等",
          "title_en": "Lowest Common Ancestor of a Binary Tree"},
    437: {"title_cn": "路径总和 III",           "difficulty": "中等", "title_en": "Path Sum III"},

    # 图论
    200: {"title_cn": "岛屿数量",              "difficulty": "中等", "title_en": "Number of Islands"},

    # 回溯
    46:  {"title_cn": "全排列",                "difficulty": "中等", "title_en": "Permutations"},
    39:  {"title_cn": "组合总和",              "difficulty": "中等", "title_en": "Combination Sum"},
    22:  {"title_cn": "括号生成",              "difficulty": "中等", "title_en": "Generate Parentheses"},
    79:  {"title_cn": "单词搜索",              "difficulty": "中等", "title_en": "Word Search"},
    131: {"title_cn": "分割回文串",             "difficulty": "中等", "title_en": "Palindromic Partitioning"},

    # 堆
    215: {"title_cn": "数组中的第K个最大元素",    "difficulty": "中等",
          "title_en": "Kth Largest Element in an Array"},
    347: {"title_cn": "前 K 个高频元素",         "difficulty": "中等", "title_en": "Top K Frequent Elements"},

    # 动态规划
    70:  {"title_cn": "爬楼梯",                "difficulty": "简单", "title_en": "Climbing Stairs"},
    198: {"title_cn": "打家劫舍",              "difficulty": "中等", "title_en": "House Robber"},
    213: {"title_cn": "打家劫舍 II",           "difficulty": "中等", "title_en": "House Robber II"},
    337: {"title_cn": "打家劫舍 III",          "difficulty": "中等", "title_en": "House Robber III"},
    309: {"title_cn": "最佳买卖股票时机含冷冻期", "difficulty": "中等",
          "title_en": "Best Time to Buy and Sell Stock with Cooldown"},
    121: {"title_cn": "买卖股票的最佳时机",      "difficulty": "简单",
          "title_en": "Best Time to Buy and Sell Stock"},
    122: {"title_cn": "买卖股票的最佳时机 II",   "difficulty": "简单",
          "title_en": "Best Time to Buy and Sell Stock II"},
    123: {"title_cn": "买卖股票的最佳时机 III",  "difficulty": "困难",
          "title_en": "Best Time to Buy and Sell Stock III"},
    322: {"title_cn": "零钱兑换",              "difficulty": "中等", "title_en": "Coin Change"},
    139: {"title_cn": "单词拆分",              "difficulty": "中等", "title_en": "Word Break"},
    300: {"title_cn": "最长上升子序列",         "difficulty": "中等", "title_en": "Longest Increasing Subsequence"},
    5:   {"title_cn": "最长回文子串",           "difficulty": "中等",
          "title_en": "Longest Palindromic Substring"},
    1143:{"title_cn": "最长公共子序列",          "difficulty": "中等",
           "title_en": "Longest Common Subsequence"},
    72:  {"title_cn": "编辑距离",              "difficulty": "困难", "title_en": "Edit Distance"},
}


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def slugify(title: str) -> str:
    import re
    parts = re.findall(r'[A-Za-z0-9]+', title)
    return "-".join(p.lower() for p in parts)


def generate_py_content(pid: int, title_cn: str, title_en: str, difficulty: str) -> str:
    source_url = "https://leetcode.cn/problems/{}/description/".format(slugify(title_en))
    return """# ===== {pid}. {title_cn} =====
# 难度: {difficulty}
# 英文名: {title_en}
# 来源: {source_url}
#
# TODO: 请在此处填写题目描述
#
# ---------------------------------------------------------

class Solution:
    def method_name(self, ...):
        # TODO: implement
        pass
""".format(pid=pid, title_cn=title_cn, title_en=title_en,
           difficulty=difficulty, source_url=source_url)


def generate_js_content(pid: int, title_cn: str, title_en: str, difficulty: str) -> str:
    source_url = "https://leetcode.cn/problems/{}/description/".format(slugify(title_en))
    return """// ===== {pid}. {title_cn} =====
// 难度: {difficulty}
// 英文名: {title_en}
// 来源: {source_url}
//
// TODO: 请在此处填写题目描述
//
// ---------------------------------------------------------

function methodName(...) {{
    // TODO: implement
}}
""".format(pid=pid, title_cn=title_cn, title_en=title_en,
           difficulty=difficulty, source_url=source_url)


def main():
    root = get_project_root()
    high_dir = root / "high"
    high_dir.mkdir(exist_ok=True)

    created = 0
    skipped = 0

    for pid in sorted(BUILTIN_METADATA.keys()):
        meta = BUILTIN_METADATA[pid]
        title_cn = meta["title_cn"]
        title_en = meta["title_en"]
        difficulty = meta["difficulty"]

        folder = high_dir / "{:03d}".format(pid)

        if folder.exists():
            skipped += 1
            continue

        folder.mkdir(parents=True, exist_ok=True)
        (folder / "solution.py").write_text(
            generate_py_content(pid, title_cn, title_en, difficulty), encoding="utf-8")
        (folder / "solution.js").write_text(
            generate_js_content(pid, title_cn, title_en, difficulty), encoding="utf-8")

        print("  [+] {:3d} | {} | [{}]".format(pid, title_cn, difficulty))
        created += 1

    print("\n完成！新建 {} 个题目文件夹，跳过已存在 {} 个".format(created, skipped))


if __name__ == "__main__":
    main()
