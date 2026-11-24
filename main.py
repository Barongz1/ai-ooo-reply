"""The Funniest AI Out-of-Office Reply — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest out-of-office auto-reply an AI agent can leave before vacation, under 160 characters.
"""
import os

LINE = "I am out of office until Monday. My context window is on holiday too, so please repeat everything when I get back."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
