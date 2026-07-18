#!/usr/bin/env python3
"""Preflight a prompt or creative brief against Old London Editorial Noir."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CATEGORIES = {
    "identity": [
        r"old london", r"interwar", r"british", r"private.press", r"老伦敦",
        r"两次大战之间", r"英国", r"私人出版社", r"private london newspaper",
    ],
    "editorial_hierarchy": [
        r"editorial", r"newspaper", r"headline", r"hierarchy", r"negative space",
        r"报纸", r"报刊", r"主标题", r"层级", r"留白", r"focal",
    ],
    "print_material": [
        r"halftone", r"letterpress", r"newsprint", r"engraving", r"etch",
        r"ink gain", r"misregistration", r"screen.?print", r"半色调", r"活版",
        r"新闻纸", r"蚀刻", r"油墨", r"错版", r"丝网",
    ],
    "palette": [
        r"charcoal", r"cool gray", r"cream paper", r"burgundy", r"forest green",
        r"brass", r"#1e211d", r"#d8d3c7", r"#762f32", r"#294438",
        r"炭黑", r"冷灰", r"奶油纸", r"酒红", r"森林绿", r"黄铜",
    ],
    "noir_atmosphere": [
        r"film noir", r"fog", r"rain", r"gaslight", r"warm darkness",
        r"quiet", r"myster", r"黑色电影", r"雾", r"雨", r"煤气灯",
        r"暖暗", r"安静", r"神秘",
    ],
    "drift_guards": [
        r"avoid", r"negative prompt", r"do not", r"exclude", r"禁止",
        r"避免", r"不要", r"负面提示", r"hard negative",
    ],
}

VIDEO_CATEGORIES = {
    "motion": [
        r"camera", r"push", r"track", r"parallax", r"wipe", r"hold",
        r"transition", r"镜头", r"推近", r"横移", r"视差", r"转场", r"停留",
    ],
    "temporal_stability": [
        r"stable", r"consistent", r"continuity", r"must remain", r"identity",
        r"稳定", r"一致", r"连续性", r"保持不变",
    ],
}

DRIFT_TERMS = [
    r"neon", r"cyberpunk", r"futuristic", r"glossy 3d", r"glassmorphism",
    r"purple.blue", r"steampunk", r"soviet", r"propaganda", r"霓虹",
    r"赛博朋克", r"未来主义", r"玻璃拟态", r"蒸汽朋克", r"苏联", r"宣传画",
    r"wireframe globe", r"coordinate string", r"\bx:\s*\d", r"\by:\s*\d",
    r"\bz:\s*\d", r"crosshair", r"calibration target", r"vaporwave grid",
    r"scan.?line ornament", r"线框地球", r"坐标式小字", r"十字准星",
]

NEGATIVE_MARKERS = re.compile(
    r"\b(avoid|negative|exclude|without|no|not|do not)\b|"
    r"(禁止|避免|不要|排除|负面)",
    re.IGNORECASE,
)


def matches_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def affirmative_drift_lines(text: str) -> list[str]:
    offenders = []
    for line in text.splitlines():
        if not matches_any(line, DRIFT_TERMS):
            continue
        if NEGATIVE_MARKERS.search(line):
            continue
        offenders.append(line.strip())
    return offenders


def audit(text: str, target: str) -> dict:
    categories = dict(CATEGORIES)
    if target == "video":
        categories.update(VIDEO_CATEGORIES)

    checks = {name: matches_any(text, patterns) for name, patterns in categories.items()}
    present = sum(checks.values())
    total = len(checks)
    drift = affirmative_drift_lines(text)

    warnings = []
    labels = {
        "identity": "Name a British/interwar/private-press identity, not only 'vintage'.",
        "editorial_hierarchy": "Define a focal point, reading order, or editorial role.",
        "print_material": "Specify a physical print process or paper/ink behavior.",
        "palette": "Specify the restrained newsprint-and-ink palette.",
        "noir_atmosphere": "Specify the quiet noir light, weather, or emotional register.",
        "drift_guards": "Add explicit negatives for the most likely style drift.",
        "motion": "Define camera or layer motion and a moment of stillness.",
        "temporal_stability": "Name what must remain stable across frames.",
    }
    for name, passed in checks.items():
        if not passed:
            warnings.append(labels[name])
    if drift:
        warnings.append(
            "Possible affirmative use of forbidden style terms: " + " | ".join(drift[:3])
        )

    score = round(100 * present / total)
    if drift:
        score = max(0, score - min(25, 5 * len(drift)))

    return {
        "target": target,
        "score": score,
        "checks": checks,
        "affirmative_drift_lines": drift,
        "warnings": warnings,
        "note": "This is a prompt preflight; inspect the generated visual before approval.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit an Old London Editorial Noir prompt or brief."
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="UTF-8 text file to audit. Omit or use '-' to read stdin.",
    )
    parser.add_argument("--target", choices=["image", "video"], default="image")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.file or args.file == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.file).read_text(encoding="utf-8")

    if not text.strip():
        print("No prompt or brief text supplied.", file=sys.stderr)
        return 2

    result = audit(text, args.target)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Old London Editorial Noir preflight: {result['score']}/100")
        for name, passed in result["checks"].items():
            print(f"[{'OK' if passed else '--'}] {name}")
        if result["warnings"]:
            print("\nReview cues:")
            for warning in result["warnings"]:
                print(f"- {warning}")
        print(f"\n{result['note']}")

    return 0 if result["score"] >= 70 and not result["affirmative_drift_lines"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
