class Word:
    def __init__(self,word):
        self.word = word
        self.count = 1    
class Dictionary:
    words = []

    def __add_word(self, word):
        word_obj = Word(word)
        self.words.append(word_obj)

    def check_and_add_word(self, word):
        pos = next((wd for wd in self.words if wd.word==word), None)
        if pos == None:
            self.__add_word(word)
        else:
            self.words[pos].count+=1

def encode(array):
    size = len(array)
    dictionary = Dictionary()
    for i in range(size-1):
        word = [array[i],array[i+1]]
        dictionary.check_and_add_word(word)

