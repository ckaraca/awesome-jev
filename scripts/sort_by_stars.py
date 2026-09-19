#!/usr/bin/env python3
"""Sort GitHub entries in each README section by star count and refresh the counts.

Non-GitHub links (docs, sites) keep their order and stay above repo entries.
Uses GITHUB_TOKEN if set, to avoid the unauthenticated rate limit.
"""
import json, os, re, sys, urllib.request

README = os.path.join(os.path.dirname(__file__), "..", "README.md")
ENTRY = re.compile(r"^- \[[^\]]+\]\(https://github\.com/([^/)]+/[^/)#]+)[^)]*\)")
STARS = re.compile(r" ⭐ [\d.]+k?$")


def stars(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    if tok := os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)["stargazers_count"]


def fmt(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def main():
    lines = open(README, encoding="utf-8").read().split("\n")
    out, block = [], []

    def flush():
        entries = []
        for line in block:
            repo = ENTRY.match(line).group(1)
            n = stars(repo)
            entries.append((n, f"{STARS.sub('', line)} ⭐ {fmt(n)}"))
        out.extend(l for _, l in sorted(entries, key=lambda e: -e[0]))
        block.clear()

    for line in lines:
        if ENTRY.match(line):
            block.append(line)
        else:
            flush()
            out.append(line)
    flush()
    open(README, "w", encoding="utf-8").write("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
