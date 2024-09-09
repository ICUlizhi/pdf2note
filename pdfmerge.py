import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_directory(directory, output_filename):
    # 创建一个PdfMerger对象
    merger = PdfMerger()

    # 获取目录中的所有文件
    files = os.listdir(directory)

    # 遍历目录中的所有文件
    for file in files:
        # 检查文件是否为PDF文件
        if file.lower().endswith('.pdf'):
            # 构建文件的完整路径
            file_path = os.path.join(directory, file)
            # 将PDF文件添加到合并器中
            merger.append(file_path)

    # 将合并后的PDF文件保存到输出文件中
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)

    # 关闭合并器
    merger.close()

# 指定当前目录下的一个文件夹和输出文件名
directory = './lectures'
output_filename = 'merged_output.pdf'

# 调用函数合并PDF文件
merge_pdfs_in_directory(directory, output_filename)