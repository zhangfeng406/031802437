import jieba
import jieba.analyse
import os
from sklearn.metrics.pairwise import cosine_similarity


class CosineSimilarity(object):

    def __init__(self, text1, text2):
        self.s1 = text1
        self.s2 = text2

    @staticmethod  # 静态方法
    def extractKeyword(text):
        cut = [i for i in jieba.cut(text, cut_all=True) if i != '']
        keywords = jieba.analyse.extract_tags(",".join(cut), topK=topK, withWeight=False)
        # 提取关键词，按照权重返回前topK个关键词
        return keywords

    @staticmethod
    def oneHotCode(dictionaries, keywords):
        vector = [0] * len(dictionaries)
        #   初始化全0 向量
        for keyword in keywords:
            vector[dictionaries[keyword]] += 1
        return vector

    @staticmethod
    def calculate(s1_code, s2_code):
        sample = [s1_code, s2_code]
        sim = cosine_similarity(sample)
        # 用scikit-learn自带的余弦相似度计算
        # 返回的数组[0][0]为 s1 与 s1 的相似度
        # [0][1]为 s1 与 s2 的相似度
        return sim[0][1]

    def main(self):

        dictionaries = {}
        hash_value = 0
        # 初始化哈希表
        keywords1 = self.extractKeyword(self.s1)
        keywords2 = self.extractKeyword(self.s2)
        #   分别提取文本的关键词
        keywords = set(keywords1).union(set(keywords2))
        #   set去重
        #   关键词取并
        for keyword in keywords:
            dictionaries[keyword] = hash_value
            hash_value += 1
        s1_code = self.oneHotCode(dictionaries, keywords1)
        s2_code = self.oneHotCode(dictionaries, keywords2)
        #   编码
        sim_value = self.calculate(s1_code, s2_code)
        return sim_value


if __name__ == '__main__':

    root = "E:\\python file\\sim_0.8"
    fileName = os.listdir(root)  # 得到当前目录下所有的文件名
    with open(root + '\\' + fileName[0], encoding='UTF-8') as fp:
        orig_text = fp.read()
        seg = [i for i in jieba.cut(orig_text, cut_all=True) if i != '']
    topK = int(len(seg) / 8)
    for i in range(1, 10):
        with open(root + '\\' + fileName[i], encoding='UTF-8') as fp:
            copy_text = fp.read()
            similarity = CosineSimilarity(orig_text, copy_text)
            similarity = similarity.main()
            print(fileName[i] + ' 相似度: %.2f%%' % (similarity * 100))
