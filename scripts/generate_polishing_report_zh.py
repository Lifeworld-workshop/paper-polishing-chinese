#!/usr/bin/env python3
"""
Generate a concise narrative polishing note for Chinese academic writing.

Usage:
    python3 generate_polishing_report_zh.py --input-json data.json --output report.md

Supported input keys:
- overall_note: str
- key_changes: list[str]
- flagged: list[str]
- polished_text: str
- paragraphs: list[{
    original: str,
    polished: str,
    changes: list[{original, revised, reason}],
    flagged: list[str],
    section: str
  }]
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Any, Dict, List


def _normalize_paragraphs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    if isinstance(data.get("paragraphs"), list):
        return data["paragraphs"]
    return [data]


def _collect_key_changes(data: Dict[str, Any], paragraphs: List[Dict[str, Any]], limit: int = 8) -> List[str]:
    custom = data.get("key_changes")
    if isinstance(custom, list) and custom:
        return [str(item).strip() for item in custom if str(item).strip()][:limit]

    notes: List[str] = []
    for idx, para in enumerate(paragraphs, start=1):
        for change in para.get("changes", []) or []:
            original = str(change.get("original", "")).strip()
            revised = str(change.get("revised", "")).strip()
            reason = str(change.get("reason", "")).strip()
            if original and revised:
                line = f"第 {idx} 段：将“{original}”调整为“{revised}”。"
            elif revised:
                line = f"第 {idx} 段：补充“{revised}”。"
            else:
                continue
            if reason:
                line += f" 理由：{reason}"
            notes.append(line)
            if len(notes) >= limit:
                return notes
    return notes


def _collect_flagged(data: Dict[str, Any], paragraphs: List[Dict[str, Any]]) -> List[str]:
    flagged: List[str] = []
    if isinstance(data.get("flagged"), list):
        flagged.extend(str(item).strip() for item in data["flagged"] if str(item).strip())
    for para in paragraphs:
        for item in para.get("flagged", []) or []:
            text = str(item).strip()
            if text:
                flagged.append(text)
    return flagged


def _build_polished_text(data: Dict[str, Any], paragraphs: List[Dict[str, Any]]) -> str:
    if isinstance(data.get("polished_text"), str) and data["polished_text"].strip():
        return data["polished_text"].strip()

    chunks: List[str] = []
    for idx, para in enumerate(paragraphs, start=1):
        section = str(para.get("section", "")).strip()
        heading = f"### 第 {idx} 段"
        if section:
            heading += f"（{section}）"
        chunks.append(heading)
        text = str(para.get("polished") or para.get("original") or "").strip()
        chunks.append(text)
        chunks.append("")
    return "\n".join(chunks).strip()


def generate_report(data: Dict[str, Any]) -> str:
    paragraphs = _normalize_paragraphs(data)
    key_changes = _collect_key_changes(data, paragraphs)
    flagged = _collect_flagged(data, paragraphs)
    polished_text = _build_polished_text(data, paragraphs)
    overall_note = str(data.get("overall_note", "")).strip()
    if not overall_note:
        overall_note = "本次润色以提升论证连贯性、表达精确性与学术叙事自然度为目标。"

    lines: List[str] = []
    lines.append("# 中文学术论文润色说明")
    lines.append("")
    lines.append(f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("**任务类型**：中文学术论文语言润色")
    lines.append("")

    lines.append("## 一、整体说明")
    lines.append("")
    lines.append(overall_note)
    lines.append("")

    lines.append("## 二、润色后文本")
    lines.append("")
    lines.append(polished_text if polished_text else "（未提供文本）")
    lines.append("")

    lines.append("## 三、关键修改摘要（可选）")
    lines.append("")
    if key_changes:
        for item in key_changes:
            lines.append(f"- {item}")
    else:
        lines.append("- （无）")
    lines.append("")

    lines.append("## 四、待确认事项（可选）")
    lines.append("")
    if flagged:
        for idx, item in enumerate(flagged, start=1):
            lines.append(f"{idx}. {item}")
    else:
        lines.append("1. （无）")
    lines.append("")

    lines.append("## 五、参考标准")
    lines.append("")
    lines.append("- GB/T 15834-2011《标点符号用法》")
    lines.append("- GB/T 15835-2011《出版物上数字用法》")
    lines.append("- GB/T 7713.1-2006《学位论文编写规则》")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate concise Chinese polishing note")
    parser.add_argument("--input-json", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Output Markdown file path")
    args = parser.parse_args()

    try:
        with open(args.input_json, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    report = generate_report(data)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"润色说明已生成：{args.output}")


if __name__ == "__main__":
    main()
