#!/usr/bin/env python3
"""
Text → Regex (offline)
Usage:
  python main.py --input "emails ending with .edu"
"""
import argparse, requests, os, sys, re

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 60

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(desc):
    return (
        "Return ONLY a single regular expression (no delimiters, no explanation) that matches the description below.\n"
        f"Description: {desc}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
