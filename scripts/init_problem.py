#!/usr/bin/env python3
"""
题目初始化脚本
根据题目编号创建题目文件夹及 solution 文件

使用方法:
    python init_problem.py 1
    python init_problem.py 1 2 15 20
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

# leetcode-cli 缓存在 Windows 上的路径
CACHE_DIR = Path(os.path.expandvars(r"%APPDATA%\leetcode-cli"))
DATA_DIR = CACHE_DIR / "data"


DIFFICULTY_MAP = {"1": "简单", "2": "中等", "3": "困难"}


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def find_cache_file(problem_id: int) -> Path | None:
    """在 leetcode-cli 缓存目录中查找题目 JSON 文件"""
    if not DATA_DIR.exists():
        return None
    for f in DATA_DIR.iterdir():
        if f.suffix == ".json" and f.stem.lstrip("0") == str(problem_id):
            return f
        try:
            data = __import__("json").loads(f.read_text(encoding="utf-8"))
            if str(data.get("frontendQuestionId", "")) == str(problem_id):
                return f
        except Exception:
            pass
    return None


def load_problem_data(problem_id: int) -> dict:
    """加载题目数据，支持从缓存读取或通过 leetcode-cli 下载"""
    import json

    cache_file = find_cache_file(problem_id)
    if cache_file:
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        if data:
            return data

    # 尝试下载
    print(f"  缓存未命中，尝试下载题目 {problem_id} ...")
    import subprocess

    result = subprocess.run(
        ["leetcode", "download", str(problem_id)],
        capture_output=True, text=True,
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
    )
    if result.returncode != 0:
        return {}

    cache_file = find_cache_file(problem_id)
    if cache_file:
        return json.loads(cache_file.read_text(encoding="utf-8"))
    return {}


def html_to_text(html: str) -> str:
    """将 HTML 内容转换为纯文本"""
    import html as html_module

    text = html or ""
    text = html_module.unescape(text)
    # 移除 HTML 标签
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECCASE)
    text = re.sub(r"<p[^>]*>", "\n", text)
    text = re.sub(r"</p>", "", text)
    text = re.sub(r"<li[^>]*>", "- ", text)
    text = re.sub(r"</li>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    # 清理多余空行
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def slugify(title: str) -> str:
    """将标题转为文件夹名格式（用下划线分隔小写英文和拼音）"""
    # 如果是纯中文，先转为拼音（或直接用原始中文简化）
    import re

    # 提取英文单词和中文
    parts = re.findall(r"[\u4e00-\u9fff]+|[A-Za-z0-9]+", title)
    slug = "_".join(p.lower() for p in parts if p)
    if not slug:
        slug = str(title)
    return slug[:50]


def build_description_comment(data: dict, problem_id: int) -> tuple[str, str, str, str]:
    """从题目数据构建注释头部的各个字段"""
    title_en = data.get("title", "")
    title_cn = data.get("titleCn") or data.get("title_cn") or title_en
    difficulty_raw = str(data.get("difficulty", ""))
    difficulty = DIFFICULTY_MAP.get(difficulty_raw, difficulty_raw or "未知")
    content_html = data.get("content", "")
    content = html_to_text(content_html)

    # 示例
    examples = []
    for key in ["exampleTestCases", "exampleExampleTestCases", "sampleTestCase"]:
        ex = data.get(key) or data.get("sampleTestCase", "")
        if ex:
            examples.append(ex)
            break

    # 来源链接
    frontend_id = data.get("frontendQuestionId", problem_id)
    source_url = f"https://leetcode.cn/problems/{data.get('titleSlug', '')}/description/"

    return title_cn, title_en, difficulty, content, source_url


def generate_py_content(problem_id: int, title_cn: str, title_en: str,
                        difficulty: str, content: str, source_url: str) -> str:
    header = f'''# ===== {problem_id}. {title_cn} =====
# 难度: {difficulty}
# 英文名: {title_en}
# 来源: {source_url}
#
{content}
#
# ---------------------------------------------------------
'''
    return header + '''
class Solution:
    def method_name(self, ...):
        # TODO: implement
        pass
'''


def generate_js_content(problem_id: int, title_cn: str, title_en: str,
                        difficulty: str, content: str, source_url: str) -> str:
    header = f'''// ===== {problem_id}. {title_cn} =====
// 难度: {difficulty}
// 英文名: {title_en}
// 来源: {source_url}
//
{content}
//
// ---------------------------------------------------------
'''
    return header + '''
function methodName(...) {
    // TODO: implement
}
'''


def init_single_problem(problem_id: int, force: bool = False) -> bool:
    """初始化单个题目，返回是否成功"""
    root = get_project_root()
    folder_name = f"{problem_id:03d}"
    folder = root / "high" / folder_name

    # 如果文件夹已存在
    if folder.exists() and not force:
        resp = input(f"  题目 {problem_id} 的文件夹已存在，是否覆盖？[y/N] ").strip().lower()
        if resp != "y":
            print(f"  跳过 {problem_id}")
            return False

    folder.mkdir(parents=True, exist_ok=True)

    # 加载题目数据
    data = load_problem_data(problem_id)
    if not data:
        print(f"  [!] 题目 {problem_id} 未找到，请检查 leetcode-cli 缓存或网络连接")
        return False

    title_cn, title_en, difficulty, content, source_url = build_description_comment(
        data, problem_id)

    # 生成文件
    py_file = folder / "solution.py"
    js_file = folder / "solution.js"

    py_file.write_text(generate_py_content(
        problem_id, title_cn, title_en, difficulty, content, source_url),
        encoding="utf-8")
    js_file.write_text(generate_js_content(
        problem_id, title_cn, title_en, difficulty, content, source_url),
        encoding="utf-8")

    print(f"  [OK] {problem_id:3d} | {title_cn} | [{difficulty}] -> high/{folder_name}/")
    return True


def main():
    parser = argparse.ArgumentParser(description="初始化 LeetCode 题目")
    parser.add_argument("ids", nargs="+", type=int, help="题目编号，支持多个")
    parser.add_argument("--force", "-f", action="store_true", help="强制覆盖已有文件夹")
    args = parser.parse_args()

    root = get_project_root()
    # 确保目录存在
    (root / "high").mkdir(exist_ok=True)

    print(f"\n项目根目录: {root}")
    print(f"leetcode-cli 缓存目录: {DATA_DIR}")
    print(f"初始化 {len(args.ids)} 道题目...\n")

    success = 0
    for pid in args.ids:
        if init_single_problem(pid, args.force):
            success += 1

    print(f"\n完成！成功 {success}/{len(args.ids)} 道")


if __name__ == "__main__":
    main()
