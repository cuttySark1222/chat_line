# 读取档案
def read_file(file_name):
    new_chat_list = []
    with open(file_name, 'r', encoding="utf-8-sig") as f:
        for line in f:
            new_chat_list.append(line.strip())
    return new_chat_list


# 转换档案
def convert(new_chat_list):
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_photo_count = 0
    viki_photo_count = 0

    for line in new_chat_list:
        s = line.split(' ')
        if s[1] == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_photo_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif s[1] == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_photo_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
        else:
            for m in s[2:]:
                allen_word_count += len(m)

    print('在此对话记录中,')
    print(f'Allen打了 {allen_word_count} 个字，传了 {allen_sticker_count} 个贴图，{allen_photo_count} 张图片。')
    print(f'Viki打了 {viki_word_count} 个字，传了 {viki_sticker_count} 个贴图，{viki_photo_count} 张图片。')




# main
def main():
    new_chat_list = read_file('LINE-Viki.txt')
    convert(new_chat_list)
    

if __name__ == '__main__':
    main()