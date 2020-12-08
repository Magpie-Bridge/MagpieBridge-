
def load_msg_txt(file_path, skip_lines=8):
    data = {
        "date": [],
        "time": [],
        "name": [],
        "text": []
    }
    f = open(file_path, 'r', encoding="utf-8")
    line = f.readline()  # 读取第一行
    for i in range(skip_lines):
        line = f.readline()
    while line:
        try:
            count_date = line.index(" ")
            date = line[0:count_date]
            count_time = line[count_date + 1:].index(" ") + count_date
            time = line[count_date+1:count_time+1]
            name = line[count_time+2:-1]
            # 开始读取聊天内容
            line = f.readline()  # 读取下一行
            text = ""
            if line == "\n":
                line = f.readline()  # 读取下一行
                pass
            else:
                while line and line != "\n":
                    text += line
                    line = f.readline()  # 读取下一行
            data["date"].append(date)
            data["time"].append(time)
            data["name"].append(name)
            data["text"].append(text)
            line = f.readline()  # 读取下一行
        except:
            line = f.readline()  # 读取下一行, 跳过奇怪的东西
    return data


if __name__ == "__main__":
    data = load_msg_txt("LiZheng/QQ_msg/txt/test.txt")
