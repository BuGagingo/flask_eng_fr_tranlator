import unittest
from translator import englishToFrench, frenchToEnglish

print(frenchToEnglish(text="bonjour"))


class Test(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(englishToFrench(text="hello"), "bonjour")
        self.assertNotEqual(englishToFrench(text="I"), "vous")
        self.assertNotEqual(englishToFrench(text="you"), "I")
        self.assertEqual(englishToFrench(text="apple"), "pomme")
        self.assertEqual(englishToFrench(text="water"), "eau")

    def test_fr_to_en(self):
        self.assertEqual(frenchToEnglish(text="bonjour"), "hello")
        self.assertNotEqual(frenchToEnglish(text="vous"), "I")
        self.assertNotEqual(frenchToEnglish(text="I"), "you")
        self.assertEqual(frenchToEnglish(text="pomme"), "apple")
        self.assertEqual(frenchToEnglish(text="eau"), "water")
        print("Test complete")

if __name__ == '__main__':
    unittest.main()
