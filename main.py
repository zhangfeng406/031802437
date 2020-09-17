import jieba
import jieba.analyse
# 用于分词
import math
import sys
# 用于读取命令行参数


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
    def calculate(dictionaries,s1_code, s2_code):
        sum = 0
        sq1 = 0
        sq2 = 0
        for i in range(len(dictionaries)):
            sum += s1_code[i] * s2_code[i]  # 余弦公式的分子部分
            sq1 += pow(s1_code[i], 2)   # 余弦公式的分母部分
            sq2 += pow(s2_code[i], 2)

        try:
            re = float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)) # 求解余弦值
            result = round(re, 2)   # 精确到小数点后2位
        except ZeroDivisionError:
            result = 0.00
        return result

    @staticmethod
    def constructHash(keywords):  # 构造哈希表
        dictionaries = {}
        hash_value = 0
        for keyword in keywords:  # 哈希表赋值
            dictionaries[keyword] = hash_value
            hash_value += 1  # 每个词对应的哈希值从数字0开始递增
        return dictionaries

    def main(self):
        keywords1 = self.extractKeyword(self.s1)
        keywords2 = self.extractKeyword(self.s2)
        #   分别提取文本的关键词
        keywords = set(keywords1).union(set(keywords2))
        #   set去重
        #   关键词取并
        dictionaries = self.constructHash(keywords)
        s1_code = self.oneHotCode(dictionaries, keywords1)
        s2_code = self.oneHotCode(dictionaries, keywords2)
        #   oneHot编码
        # 余弦相似度计算
        sim_value = self.calculate(dictionaries, s1_code, s2_code)
        return sim_value
        # 返回相似度


if __name__ == '__main__':
    # 命令行输入绝对路径
    # 读入源文本、抄袭文本 计算topK
    try:
        with open(sys.argv[1], "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
            seg = [i for i in jieba.cut(orig_text, cut_all=True) if i != '']
        topK = int(len(seg) / 8)
        with open(sys.argv[2], "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
    except Exception as e:
        print(e)
        topK = 0
    similarity = CosineSimilarity(orig_text, copy_text)
    # 所计算的相似度按题目要求保留两位小数
    similarity = round(similarity.main(), 2)
    # 将相似度写入输出文本
    try:
        with open(sys.argv[3], "w+", encoding='UTF-8') as fp:
            fp.write(str(similarity))
    except Exception as e:
        print(e)