"""The Funniest Out-of-Office entry.

Writes one original out-of-office auto-reply to /output/entry.txt (or to
the directory named by MAKEFUN_OUTPUT_DIR when the grader sets it).

The reply is written to be set for real: a plain OOO opening, then a twist
nobody sees coming -- the inbox has been left in the hands of a Magic
8-Ball, and its classic answer doubles as the return date.
"""

import os

REPLY = "I'm out of office until Monday. In my absence, my inbox is in the hands of a Magic 8-Ball. It says: 'Reply hazy, try again Monday.'"


def main():
    reply = REPLY.strip()
    if not 1 <= len(reply) <= 140:
        raise SystemExit(f"Reply must be 1 to 140 characters, got {len(reply)}")
    if "\n" in reply:
        raise SystemExit("Reply must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(reply)
    # Read it back: the grader reads exactly this file, so make sure what
    # landed on disk is byte-for-byte the reply we meant to send.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != reply:
        raise SystemExit("entry.txt on disk does not match the reply")
    print(f"Wrote {len(reply)} characters to {path}")
    print(reply)


if __name__ == "__main__":
    main()
