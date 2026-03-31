# 刷题本地管理工具

本地 LeetCode 刷题管理工具，支持 Python / JavaScript 双语言。

## 题库范围

所有题目来自 `高频.md` 与 `codetop.md` 并集（共 45 道），包含以下分类：

- **哈希**：最长连续序列
- **双指针**：盛最多水的容器、三数之和、接雨水
- **滑动窗口**：无重复字符的最长子串
- **子串**：和为 K 的子数组、滑动窗口最大值
- **普通数组**：最大子数组和、合并区间
- **矩阵**：螺旋矩阵
- **链表**：反转链表、回文链表、环形链表、环形链表 II、合并两个有序链表、K 个一组翻转链表、合并K个排序链表
- **二叉树**：二叉树的中序遍历、对称二叉树、二叉树的层序遍历 II、从前序与中序遍历序列构造二叉树、二叉树的最近公共祖先、路径总和 III
- **图论**：岛屿数量
- **回溯**：全排列、组合总和、括号生成、单词搜索、分割回文串
- **堆**：数组中的第K个最大元素、前 K 个高频元素
- **动态规划**：爬楼梯、打家劫舍、打家劫舍 II、打家劫舍 III、最佳买卖股票时机含冷冻期、买卖股票的最佳时机 I/II/III、零钱兑换、单词拆分、最长上升子序列、最长回文子串、最长公共子序列、编辑距离

## 目录结构

```
{项目根目录}/
├── high/                       # 全部题目（45 道）
│   ├── 003/
│   │   ├── solution.py         # Python 题解
│   │   ├── solution.js         # JavaScript 题解
│   │   └── notes/              # 刷题笔记（完成后生成）
│   │       └── 003-xxx.md
│   ├── 005/
│   └── ...
├── scripts/
│   ├── setup.py               # 批量创建所有题目文件夹（离线可用）
│   ├── fetch_descriptions.py  # 批量拉取题目描述（需联网）
│   ├── init_problem.py        # 初始化单个题目（需 leetcode-cli）
│   ├── list_problems.py       # 列出所有题目
│   └── open_problem.py        # 快速打开题目文件夹
├── skill.md                   # AI 笔记生成器说明
└── README.md
```

## 使用流程

### Step 1：安装依赖（首次）

```bash
# Python 依赖
pip install -r requirements.txt

# leetcode-cli（用于获取题目描述）
npm install -g leetcode-cli

# 初始化本地缓存（需联网一次）
leetcode-cli init
```

### Step 2：批量创建所有题目并拉取描述

```bash
python scripts/setup.py          # 创建文件夹骨架（离线可用）
python scripts/fetch_descriptions.py  # 拉取题目描述（需联网）
```

### Step 3：查看题目列表

```bash
python scripts/list_problems.py
```

### Step 4：初始化单个题目（下载完整描述）

```bash
# 单题
python scripts/init_problem.py 1

# 多题
python scripts/init_problem.py 1 2 5 70 72

# 强制覆盖
python scripts/init_problem.py 1 --force
```

### Step 5：快速打开题目

```bash
python scripts/open_problem.py 5
```

### Step 6：编写解答

打开对应文件夹，在 `solution.py` 和 `solution.js` 中自行编写解题代码，题目描述已在文件头部注释中。

### Step 7：生成笔记（AI 辅助）

刷完一道题后，使用 `/skill` 命令触发 AI 笔记生成，生成内容包括：
- 题目描述
- 思路分析
- 复杂度分析
- **测试集**（基础用例 + 边界用例）
- JavaScript / Python 双语言题解
- 本地测试脚本

笔记保存至 `high/{题号}/notes/` 目录。

```bash
# 使用方式：直接对我说 /skill，或 "生成第 70 题的笔记"
```

## 工具脚本说明

### `setup.py`（离线可用）

批量创建所有题目文件夹，使用内置元数据（题号、中文名、英文名、难度）。**不依赖 leetcode-cli**。

### `fetch_descriptions.py`（需联网）

从 GitHub 仓库批量抓取所有题目的题目描述（中文），自动填充到 solution 文件头部注释中。无需 leetcode-cli 登录。

### `init_problem.py`（需 leetcode-cli）

从 `leetcode-cli` 缓存读取完整题目描述，生成包含完整题目正文的 solution 文件。**需要联网下载一次**。

### `list_problems.py`（离线可用）

列出所有题目，显示编号、名称、难度、完成状态。完成判断标准：`solution.py` 或 `solution.js` 中存在非 TODO 的实际代码。

### `open_problem.py`（离线可用）

在 Windows 资源管理器中打开指定题目的文件夹。

## 约束条件

- **不使用** leetcode.com / acm.com 等在线平台
- **不使用** 任何网站的辅助功能（自动补全、提交判题等）
- solution 文件本身不引入任何外部依赖
- 完全离线可用（题目描述嵌入文件头部）

## AI 笔记生成器

使用 `/skill` 或 `/skill {题号}` 触发，会自动：
1. 读取 `high/{题号}/solution.py` 中的代码
2. 读取题目描述
3. 生成含测试集的完整 Markdown 笔记到 `high/{题号}/notes/`
4. 生成 `tests/test_{题号}.py` 本地测试脚本

详见 `skill.md`。
