import jieba


def create_stopwords_list(stopwords_path):
    stopwords = [line.strip() for line in open(
        stopwords_path, encoding='UTF-8').readlines()]
    return stopwords


def seg_depart(sentence, stopwords):
    sentence_depart = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
