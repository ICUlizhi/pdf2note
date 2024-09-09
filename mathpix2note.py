import re

def remove_duplicate_titles(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    seen_titles = set()
    output_lines = []
    title_pattern = re.compile(r'^(#+)\s+(.+)$')

    for line in lines:
        match = title_pattern.match(line)
        if match:
            title = match.group(2).strip()
            if title in seen_titles:
                continue  # 跳过重复的标题
            seen_titles.add(title)
        output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

# 示例调用
input_md = 'input.md'  # 你可以替换为其他变量
output_md = 'output.md'
remove_duplicate_titles(input_md, output_md)
