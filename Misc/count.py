import os

def count_lines_in_file(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for line in f)

def count_lines_in_dir(dir_path):
    total_lines = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    total_lines += count_lines_in_file(file_path)
                except UnicodeDecodeError:
                    print(f"Skipping binary file: {file_path}")
    return total_lines

print(f"Total: {count_lines_in_dir('.')}")