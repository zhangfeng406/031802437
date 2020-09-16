import testfunc
import unittest

class MyTest(unittest.TestCase):


    def tearDown(self) -> None:
        print("test over!")

    def test_add(self):
        print("orig_0.8_add.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_add.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_del(self):
        print("orig_0.8_del.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_del.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_1(self):
        print("orig_0.8_dis_1.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_dis_1.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_3(self):
        print("orig_0.8_dis_3.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_dis_3.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_7(self):
        print("orig_0.8_dis_7.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_dis_7.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_10(self):
        print("orig_0.8_dis_10.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_dis_10.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_15(self):
        print("orig_0.8_dis_15.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_dis_15.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_mix(self):
        print("orig_0.8_mix.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_mix.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_rep(self):
        print("orig_0.8_rep.txt 相似度")
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("sim_0.8/orig_0.8_rep.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)


if __name__ == '__main__':

    unittest.main()
