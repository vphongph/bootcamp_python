t = (19,42,21)
print(f"The {len(t)} numbers are: {', '.join(str(x) for x in t if isinstance(x, int))}")