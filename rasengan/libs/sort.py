with open('source.txt') as f:
    lines = f.readlines()
lines.sort()
with open('source.txt', 'w') as f:
    map(f.write, lines)
