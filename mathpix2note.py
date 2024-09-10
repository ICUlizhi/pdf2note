import re
import heads.md as md

def remove_duplicate_titles(input_md):
    titles = input_md.get_tags('title')
    seen_titles = dict()
    input_md.extract_line_numbers(titles).save_to_file('titles.csv', 'csv')
    would_delete = []
    for line_number in titles:
        #print("-----")
        #print(f"line_number: {line_number}")
        title_content = input_md.df.at[line_number, 'content']
        title_level = input_md.df.at[line_number, 'tag_level']
        title_text = title_content.strip('#')
        #print(f"title_text: {title_text}, title_level: {title_level}")
        #print(f"seen_titles: {seen_titles}")
        if title_text in seen_titles :
            #print(title_level, seen_titles[title_text][0])
            if title_level >= seen_titles[title_text][0]:
                would_delete.append(line_number)
                #print(f'detected duplicate title: {title_text}{line_number} because of {seen_titles[title_text][1]}')               
            else:
                would_delete.append(seen_titles[title_text][1])
                #print(f'detected duplicate title: {title_text}{seen_titles[title_text][1]} because of {line_number}')
                seen_titles[title_text] = title_level, line_number
        else:
            seen_titles[title_text] = title_level, line_number
    for line_number in would_delete:
        input_md.df = input_md.df.drop(line_number)

    return input_md


if __name__ == "__main__":
    input_md = 'outputs/courses.md'
    output_md = 'note2.md'
    input = md.Md(file_path=input_md)
    output = remove_duplicate_titles(input)
    output.save_to_file(file_path = output_md,file_type='md')