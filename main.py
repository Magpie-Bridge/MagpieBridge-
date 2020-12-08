#  还在写嗷
from LiZheng.Preprocessor import Seg_Depart
from LiZheng.QQ_msg import load_msg
from LiZheng import utils


# 加载配置文件
config = utils.readjson("LiZheng/config.json")

# 加载聊天记录
data = load_msg.load_msg_txt(config["msg_path"])

# 分词处理
stopwords = Seg_Depart.create_stopwords_list(config["stopwords_path"])
for i in range(len(data["text"])):
    data["text"][i] = Seg_Depart.seg_depart(data["text"][i], stopwords)

print("done")
