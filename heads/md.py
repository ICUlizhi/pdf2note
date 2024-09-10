import pandas as pd

class Md:
    # 提供两种初始化方式,一种是直接传参content,另一种传入md文件路径
    def __init__(self, content=None, file_path=None):
        # 初始化DataFrame，包含行号, 文本, 标签, 标签等级
        self.df = pd.DataFrame(columns=['line_number', 'tag', 'tag_level', 'content'])
        
        # 依据传入参数处理内容
        if content is not None:
            self.parse_content(content)
        elif file_path is not None:
            self.load_from_file(file_path)
        
        # 为每行初始化标签
        for line_number in range(len(self.df)):
            self.init_tag(line_number)
    
    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.parse_content(content)
        except FileNotFoundError:
            print(f"错误: 文件 {file_path} 未找到。")
        except Exception as e:
            print(f"发生错误: {e}")
    
    def parse_content(self, content):
        lines = content.splitlines()
        data = {
            'line_number': range(len(lines)),
            'tag': [None] * len(lines),
            'tag_level': [None] * len(lines),
            'content': lines
        }
        self.df = pd.DataFrame(data)
    
    # 初始化标签和标签等级
    def init_tag(self, line_number):
        content = self.df.at[line_number, 'content']
        
        if content.startswith('#'):
            self.df.at[line_number, 'tag'] = 'title'
            self.df.at[line_number, 'tag_level'] = content.count('#')
        elif content.startswith('$$'):
            self.df.at[line_number, 'tag'] = 'formula'
        elif content.startswith('-') or content.startswith('*'):
            self.df.at[line_number, 'tag'] = 'list'
        elif content.startswith('```'):
            self.df.at[line_number, 'tag'] = 'code'
        elif content.startswith('>'):
            self.df.at[line_number, 'tag'] = 'quote'
        elif content.startswith('|'):
            self.df.at[line_number, 'tag'] = 'table'
        elif content.startswith('---') or content.startswith('***') or content.startswith('___'):
            self.df.at[line_number, 'tag'] = 'hr'
        elif content.startswith('![') or content.startswith('http'):
            self.df.at[line_number, 'tag'] = 'image'
        elif content.startswith('['):
            self.df.at[line_number, 'tag'] = 'link'
        else:
            self.df.at[line_number, 'tag'] = 'text'

    # 获取指定标签的行号
    def get_tags(self, tag, tag_level=None):
        if tag_level is None:
            return self.df[self.df['tag'] == tag]['line_number']
        else:
            return self.df[(self.df['tag'] == tag) & (self.df['tag_level'] == tag_level)]['line_number']
        
    # 还原为文本
    def get_content(self):
        return '\n'.join(self.df['content'])
    
    # 保存到文件,csv或md
    def save_to_file(self, file_path, file_type='md'):
        if file_type == 'md':
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.get_content())
            except Exception as e:
                print(f"保存为markdown文件时发生错误: {e}")
        elif file_type == 'csv':
            try:
                self.df.to_csv(file_path, index=False, encoding='utf-8')    
            except Exception as e:
                print(f"保存为csv文件时发生错误: {e}")
        else:
            print("不支持的文件类型。")
    
    # 提取多行为新的md对象
    def extract_lines(self, start, end=None):
        if end is None:
            end = start
        if start < 0 or start >= len(self.df) or end < 0 or end >= len(self.df) or start > end:
            raise IndexError("行号超出范围。")
        new_md = Md()
        new_md.df = self.df.iloc[start:end+1].reset_index(drop=True)
        return new_md
    
    # 提取行号列表为新的md对象
    def extract_line_numbers(self, line_numbers):
        new_md = Md()
        new_md.df = self.df[self.df['line_number'].isin(line_numbers)].reset_index(drop=True)
        return new_md    

    # 打印全部或者前n行
    def print(self, n=None):
        if n is None:
            print(self.df)
        else:
            print(self.df.head(n))
    
    # 插入多行(支持md对象,panads.DataFrame,或者list)
    def insert(self, line_number, new_md):
        if isinstance(new_md, Md):
            new_md = new_md.df
        elif isinstance(new_md, pd.DataFrame):
            new_md = new_md
        elif isinstance(new_md, list):
            new_md = pd.DataFrame({'content': new_md})
        else:
            raise TypeError("不支持的类型。")
        
        # 找到对应 line_number 的索引
        index = self.df[self.df['line_number'] == line_number].index
        if len(index) == 0:
            raise IndexError("行号超出范围。")
        
        # 插入新行
        self.df = pd.concat([self.df.iloc[:index[0]], new_md, self.df.iloc[index[0]:]])


    # 删除多行
    def delete(self, start, end=None):
        if end is None:
            end = start

        if start < 0 or start >= len(self.df) or end < 0 or end >= len(self.df) or start > end:
            raise IndexError("行号超出范围。")
        
        # 找到 start 和 end 对应的索引
        start_index = self.df[self.df['line_number'] == start].index
        end_index = self.df[self.df['line_number'] == end].index
        
        if len(start_index) == 0 or len(end_index) == 0:
            raise IndexError("行号超出范围。")
        
        # 删除指定范围的行
        self.df = pd.concat([self.df.iloc[:start_index[0]], self.df.iloc[end_index[0]+1:]])
    

    # 更新行号
    def refresh(self):
        self.df['line_number'] = range(len(self.df))
        for line_number in range(len(self.df)):
            self.init_tag(line_number)

    # 替换多行
    def replace(self, new_md, start, end=None):
        if end is None:
            end = start
        self.delete(start, end)
        self.insert(start, new_md)
