#!/usr/bin/env python3
"""
题目列表脚本
列出所有已创建的题目（编号、名称、难度、完成状态）

使用方法:
    python list_problems.py
"""

import re
from pathlib import Path

HIGH_PRIORITY = {5, 70, 72, 121, 122, 123, 139, 198, 213, 300, 322, 1143, 337, 309}


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def parse_problem_header(file_path: Path) -> dict:
    """从 solution 文件头部解析题目基本信息"""
    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return {}

    result = {"title_cn": "", "difficulty": ""}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            stripped = line.lstrip("#").lstrip("/").lstrip()
            if stripped.startswith("==="):
                m = re.match(r"===+\s*(\d+)\.\s*(.+?)\s*===+", stripped)
                if m:
                    result["id"] = int(m.group(1))
                    result["title_cn"] = m.group(2).strip()
            elif stripped.startswith("难度:"):
                result["difficulty"] = stripped.split(":", 1)[1].strip()
        else:
            break
    return result


def is_completed(file_path: Path) -> bool:
    """判断 solution 文件是否已完成。标准：有实际实现（非 placeholder）。"""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    # 去掉头部注释
    in_header = True
    code_lines = []
    for line in content.splitlines():
        stripped = line.strip()
        if in_header:
            if stripped.startswith("class ") or stripped.startswith("function "):
                in_header = False
                code_lines.append(stripped)
        else:
            code_lines.append(stripped)

    # 过滤掉头部行（class / function 定义本身）
    body_lines = [l for l in code_lines if not (l.startswith("class ") or l.startswith("function ") or l.startswith("def ") or l.startswith("async def "))]
    # 过滤掉空行和纯注释
    meaningful = [l for l in body_lines if l.strip() and not l.strip().startswith("//") and not l.strip().startswith("#")]

    # 如果没有任何实质性代码行，则未完成
    if not meaningful:
        return False

    # 过滤掉空行、纯注释、纯括号
    clean = [l for l in meaningful if l not in ("}", "]", ")")]
    if not clean:
        return False

    # 如果只有 placeholder，则未完成
    placeholders = ("raise NotImplementedError", 'throw new Error("TODO', "pass", "return None", "return []")
    if all(any(p in l for p in placeholders) for l in clean):
        return False

    return True


def scan_directory(base_dir: Path, section: str) -> list[dict]:
    """扫描一个目录下的所有题目文件夹"""
    problems = []
    if not base_dir.exists():
        return problems

    for folder in sorted(base_dir.iterdir()):
        if not folder.is_dir():
            continue
        # 匹配数字开头的文件夹（可能有 !、todo 等后缀）
        if not re.match(r"^\d+", folder.name):
            continue

        num_match = re.match(r"^(\d+)", folder.name)
        pid = int(num_match.group(1))
        info = parse_problem_header(folder / "solution.py")
        info["id"] = pid
        info["folder"] = folder.name
        info["section"] = section

        py_done = is_completed(folder / "solution.py")
        js_done = is_completed(folder / "solution.js")
        info["completed"] = py_done or js_done

        problems.append(info)

    return problems


def main():
    root = get_project_root()
    high_dir = root / "high"

    codetop_dir = root / "codetop"

    all_problems = []
    all_problems += scan_directory(high_dir, "high")
    all_problems += scan_directory(codetop_dir, "codetop")

    if not all_problems:
        print("尚未创建任何题目，请先运行:")
        print(f"  python scripts/init_problem.py 1")
        print("或批量初始化:")
        print(f"  python scripts/init_problem.py 1 2 3 5 70 72")
        return

    # 输出
    total = len(all_problems)
    completed = sum(1 for p in all_problems if p["completed"])

    diff_map = {"简单": 0, "中等": 1, "困难": 2}
    all_problems.sort(key=lambda p: (diff_map.get(p.get("difficulty", ""), 1), p["id"]))

    print()
    print(f"{'编号':<5} {'题目名称':<30} {'难度':<6} {'状态':<10} {'分类'}")
    print("-" * 65)

    for p in all_problems:
        pid = f"{p['id']:>3}"
        title = (p.get("title_cn") or "未知").ljust(30)
        diff = (p.get("difficulty") or "未知").ljust(6)
        status = "[OK]" if p["completed"] else "[--]"
        section = p.get("section", "")
        print(f"{pid:<5} {title:<30} {diff:<6} {status:<10} {section}")

    print("-" * 65)
    print(f"已完成: {completed} / {total}")


if __name__ == "__main__":
    main()
