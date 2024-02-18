files = ['Furina.txt', 'Firefly.txt', 'Sparkle.txt', 'User.txt']
total_lines = 0

for file in files:
    with open(f'Lists/{file}', 'r') as f:
        lines = f.readlines()
        total_lines += len(lines)

print(f'Total line count: {total_lines}')