import testfunc
import unittest
class MyTest(unittest.TestCase):

    def tearDown(self) -> None:
        print("test over!")

    def test_blank(self):
        print("源文本和抄袭文本均为空的情况")
        with open("abnormalTest/orig1.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("abnormalTest/test1.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_same(self):
        print("源文本和抄袭文本内容完全相同的情况")
        with open("abnormalTest/orig2.txt", "r", encoding='UTF-8') as fp:
            orig_text = fp.read()
        with open("abnormalTest/test2.txt", "r", encoding='UTF-8') as fp:
            copy_text = fp.read()
        similarity = testfunc.CosineSimilarity(orig_text, copy_text)
        similarity = round(similarity.main(), 2)
        print(similarity)

if __name__ == '__main__':

    unittest.main()