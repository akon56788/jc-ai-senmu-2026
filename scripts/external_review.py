#!/usr/bin/env python3
"""Generate semi-automatic external review requests for Codex PMO."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEWS_DIR = ROOT / "reviews"


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return f"(git command failed: {' '.join(args)}\n{result.stderr.strip()})"
    return result.stdout.strip()


def read_target(path: str) -> str:
    target = (ROOT / path).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        raise SystemExit(f"Target is outside repository: {path}")

    if not target.is_file():
        raise SystemExit(f"Target file not found: {path}")

    text = target.read_text(encoding="utf-8")
    limit = 12000
    if len(text) > limit:
        return text[:limit] + "\n\n...[truncated for review prompt]..."
    return text


def build_prompt(args: argparse.Namespace) -> str:
    today = dt.date.today().isoformat()
    targets = "\n".join(f"- `{target}`" for target in args.target)
    target_contents = "\n\n".join(
        f"## Target: {target}\n\n```text\n{read_target(target)}\n```"
        for target in args.target
    )
    diff_stat = run_git(["diff", "--stat", args.base, "--"])
    diff_text = run_git(["diff", args.base, "--", *args.target])
    if len(diff_text) > 16000:
        diff_text = diff_text[:16000] + "\n\n...[diff truncated for review prompt]..."

    return f"""# External Review Request

**Date**: {today}
**Requester**: Codex PMO
**Reviewer**: {args.reviewer}
**Mode**: Semi-automatic

## Objective

{args.objective}

## Review Questions

{args.question}

## Target Files

{targets}

## Reviewer Stance

Please review objectively and critically. Focus on:

- unclear ownership or role definitions
- SSOT / GitHub / Drive / Notion operational risk
- missing handoff or PMO steps
- automation risks, security concerns, and maintenance burden
- wording that could confuse Code, Cowork, Chat, Codex, ChatGPT, or Gemini

Do not rewrite the full document. Give concise findings.

## Required Output Format

```markdown
## External Review Result

**Overall**: Blocker / Risk / Suggestion / No issue

### Findings
- [Blocker/Risk/Suggestion] ...

### Missing Context
- ...

### Recommended Next Action
- ...
```

## Git Diff Stat

```text
{diff_stat or "(no diff against base)"}
```

## Git Diff

```diff
{diff_text or "(no diff against base)"}
```

## Current Target Content

{target_contents}
"""


def write_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def run_gemini(prompt: str, output_path: Path, gemini_command: str) -> None:
    executable = shutil.which(gemini_command)
    if executable is None:
        raise SystemExit(
            f"Gemini CLI not found: {gemini_command}\n"
            "Review request was generated. Install Gemini CLI or paste the request manually."
        )

    result = subprocess.run(
        [executable],
        cwd=ROOT,
        input=prompt,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    output = result.stdout.strip()
    if result.stderr.strip():
        output += "\n\n---\n\n## Gemini CLI stderr\n\n```text\n" + result.stderr.strip() + "\n```"
    if result.returncode != 0:
        output += f"\n\nGemini CLI exited with code {result.returncode}."
    write_file(output_path, output + "\n")
    if result.returncode != 0:
        raise SystemExit(f"Gemini CLI failed. Result saved: {output_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", action="append", required=True, help="Target file path. Repeatable.")
    parser.add_argument("--question", required=True, help="Specific review question.")
    parser.add_argument(
        "--objective",
        default="Review the proposed PMO / SSOT / tool-collaboration change before final reflection.",
        help="Review objective.",
    )
    parser.add_argument("--reviewer", default="Gemini or ChatGPT", help="Reviewer label.")
    parser.add_argument("--base", default="HEAD", help="Git base for diff generation.")
    parser.add_argument("--run-gemini", action="store_true", help="Run Gemini CLI after generating request.")
    parser.add_argument("--gemini-command", default="gemini", help="Gemini CLI command name or path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    today = dt.date.today().isoformat()
    prompt = build_prompt(args)
    request_path = REVIEWS_DIR / f"{today}_external_review_request.md"
    result_path = REVIEWS_DIR / f"{today}_external_review_gemini_result.md"
    write_file(request_path, prompt)
    print(f"Review request written: {request_path}")

    if args.run_gemini:
        run_gemini(prompt, result_path, args.gemini_command)
        print(f"Gemini review written: {result_path}")
    else:
        print("Gemini was not run. Paste the request into ChatGPT/Gemini or rerun with --run-gemini.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
