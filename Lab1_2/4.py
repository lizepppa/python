import re


class Proc:
    def __init__(self, text):
        self.word = 0
        self.characters = 0
        self.sentences = 0
        self.text = text
        self.lines = 0

    def Count(self):
        self.word = self.text.count(' ') + len(re.findall("\n", self.text)) + 1
        self.characters = self.text.count('') - 1
        self.lines = len(re.findall("\n", self.text)) + 1
        self.sentences = self.text.count('.') + self.text.count("...") * (-2) + self.text.count(";") + self.text.count('?') + self.text.count('!')
        print("num of words=", self.word)
        print("num of characters=", self.characters)
        print("num of sentences=", self.sentences)
        print("num of lines=", self.lines)


f = open("text.txt")
a = Proc(f.read())
f.close()
a.Count()


text.txt
Create a class that describes a Product of online store...
As a Product fields you can use a price, description and product' dimensions.
