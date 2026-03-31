#!/usr/bin/env python3
"""
快速打开题目脚本
根据题目编号打开对应题目的文件夹（Windows 资源管理器）

使用方法:
    python open_problem.py 1
"""

import os
import sys
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def find_problem_folder(problem_id: int) -> Path | None:
    root = get_project_root()
    folder = root / "high" / f"{problem_id:03d}"
    if folder.exists():
        return folder
    return None


def main():
    if len(sys.argv) < 2:
        print("用法: python open_problem.py <题目编号>")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print(f"无效的题目编号: {sys.argv[1]}")
        sys.exit(1)

    folder = find_problem_folder(pid)
    if folder is None:
        print(f"题目 {pid} 的文件夹不存在，请先运行:")
        print(f"  python scripts/init_problem.py {pid}")
        sys.exit(1)

    # Windows 资源管理器打开文件夹
    os.startfile(folder)


if __name__ == "__main__":
    main()
