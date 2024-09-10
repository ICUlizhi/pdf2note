from deep_translator import GoogleTranslator
import re

def translate_to_chinese(input_file, output_file):
    # 使用 'zh-CN' 表示简体中文
    translator = GoogleTranslator(source='en', target='zh-CN')

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []

    for line in lines:
        # 检查是否为公式标记或空行
        if line.strip().startswith('$$') or line.strip() == '':
            translated_lines.append(line)
        else:
            try:
                translated_line = translator.translate(line)
                translated_lines.append(translated_line + '\n')
            except Exception as e:
                print(f"Error translating '{line.strip()}': {e}")
                translated_lines.append(line)  # 失败时保留原文

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)

# 示例调用

# 示例调用
if __name__ == "__main__":
    input_md = 'note.md'
    output_md = 'note(ch).md'
    translate_to_chinese(input_md, output_md)
