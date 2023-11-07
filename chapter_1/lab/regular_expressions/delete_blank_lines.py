import re

with open('my.txt', 'r') as file:
    lines = file.readlines()

new_lines = []

for line in lines:
    # Используйте регулярное выражение для удаления \n после точек
    if line.strip():
        new_line = re.sub(r'\n([:.**])|\*\*', r'\1', line)
        new_lines.append(new_line)

with open('my_modified.txt', 'w') as output:
    output.writelines(new_lines)