import unicodedata

def solve(value):
    return [{"character": c, "category": unicodedata.category(c)} for c in value]
