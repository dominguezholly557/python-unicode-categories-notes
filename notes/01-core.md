# Inspect Unicode categories: implementation

## What the example does

Unicode categories distinguish letters, marks, punctuation and symbols. Python iterates code points, not user-perceived grapheme clusters.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"Aé🙂"
```

Expected result:

```json
[
  {
    "character": "A",
    "category": "Lu"
  },
  {
    "character": "é",
    "category": "Ll"
  },
  {
    "character": "🙂",
    "category": "So"
  }
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
