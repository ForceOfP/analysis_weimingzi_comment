keyword_extract = {"k", "w", "千", "万", "百", "00"}


def extract():
    f_comment = open("comment.txt", "r", encoding='utf-8')
    f_extracted_comment = open("extracted_comment.txt", "w+", encoding='utf-8')
    lines = f_comment.read().splitlines()
    for line in lines:
        for keyword in keyword_extract:
            if keyword in line:
                f_extracted_comment.write(f'{line}\n')
                break
    f_comment.close()
    f_extracted_comment.close()


if __name__ == "__main__":
    extract()