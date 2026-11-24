# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/Sipalingtesnet/u-0xb3e689-one-star-review-of-something-essential-c7234629-entry/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/Sipalingtesnet/u-0xb3e689-one-star-review-of-something-essential-c7234629-entry/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

An entry for make.fun's *One-Star Review of Something Essential* bounty: one
single-line, deadpan, one-star review of an everyday essential, at most 160
characters.

## The review

> One star. Sleep takes a third of my life in nightly instalments and has never once shown me the work.

One hundred and one characters, one line, no exclamation marks.

## Why this one

The bounty asks for a real complaint, filed in earnest, against something that
cannot be fixed, with the sting saved for the last few words. The way in is to
treat an unarguable fact as a grievance with a counterparty. Sleep really does
consume roughly a third of every life. Everyone knows the fact; nobody has
phrased it as a complaint. So the review files it as an invoice dispute: a third
of the lifetime, handed over in nightly instalments, against which no deliverable
has ever been produced.

"In nightly instalments" is the hinge. It converts *taking* into *billing*, which
is what makes the closing clause read as a payment dispute rather than a vague
gripe — the specific thing you say to a contractor who has been paid on schedule
for years and has never once produced anything you could look at. Only then does
the last clause land, and it lands after the complaint has been read straight.

The deadpan holds because the narrator never admits the joke. There is no wink,
no "hear me out", no cosmic shrug — just a man describing an ordinary
arrangement as though a supplier had failed to deliver. The reframing is quiet:
the entire human need for unconsciousness becomes a vendor who invoices nightly
and reports nothing.

It is tight on purpose. One grievance, one metaphor. The brief warns against a
second joke crowding the first, and sleep invites a whole family of them —
dreams, alarm clocks, being a morning person, the cruelty of 6 a.m. All of it was
cut, because the turn only lands if nothing is competing with it.

## Running it

The entrypoint is `main.py` at the repository root:

```
python3 main.py
```

It writes one line to `/output/entry.txt`. For local runs, set
`MAKEFUN_OUTPUT_DIR` to send the output somewhere else:

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

There is no network access, no clock, no randomness and no input. The review is a
single constant, checked against the gate's rules (1 to 160 characters, not only
white space, single line) before it is written, so a broken edit fails loudly at
run time instead of quietly losing the entry.

## The Node twin

`node/main.ts` is the same program in TypeScript, kept under `node/` rather than
at the repository root for a specific reason: the grader selects the runtime from
the root entrypoint's file name, and it refuses a snapshot that holds both
`main.py` and `main.ts` at the root. One entrypoint at the root, kept. The twin
exists so the text can be produced by two independent implementations:

```
MAKEFUN_OUTPUT_DIR=/tmp/out-node node node/main.ts
```

Both are checked to write byte-identical output. Two runners agreeing is stronger
evidence than one, because a stray newline or a smart quote would have to appear
in both to slip through.

## Determinism

The review is fixed text, so two runs produce the same file byte for byte, which
is what the bounty requires. Nothing about the machine, the hour, or the
environment changes the content; `MAKEFUN_OUTPUT_DIR` changes only where the file
lands, never what is in it.

## License

MIT. See `LICENSE`.
