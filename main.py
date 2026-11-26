"""Funniest Sign on a Haunted Server Room Door.

Writes one line — the warning sign taped to a haunted server room door —
to $MAKEFUN_OUTPUT_DIR/entry.txt for the make.fun bounty "Funniest Sign
on a Haunted Server Room Door". The ghosts in rack 7 answer back, bill
by the hour, and already know your password. Only the Python standard
library is used.
"""

import os
import sys

DOOR_SIGN = "WARNING: Do not knock. The ghosts in rack 7 answer back, bill by the hour, and already know your password."

# Sealed gate from the kit's RULES.txt ("## The gate"): the scorer
# takes UTF-8 text of 1 to 120 characters. The req JSON's "200
# characters" is generic template text and does not apply to this bounty.
MAX_CHARS = 120


def check_sign(text):
    """Return the sign line once it passes the sealed gate, else raise.

    The gate counts characters, not bytes; the line must be a single
    line with no trailing newline and no control characters.
    """
    if not isinstance(text, str):
        raise TypeError("sign must be text")
    if not text.strip():
        raise ValueError("sign must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("sign is %d chars, over the %d-char gate" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        raise ValueError("sign must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("sign must not contain control characters")
    return text


def describe_sign(text):
    """Return a one-line summary of the sign's size in chars and bytes.

    The sealed gate counts characters, while the file on disk is measured
    in bytes; for plain ASCII the two agree, but a non-ASCII sign would
    be longer in bytes, so both numbers are reported.
    """
    return "%d characters, %d UTF-8 bytes" % (len(text), len(text.encode("utf-8")))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(check_sign(DOOR_SIGN))
    print("wrote %s (%s)" % (target, describe_sign(DOOR_SIGN)))


if __name__ == "__main__":
    main()
