class Word:
    def __init__(self, word, create_id):
        self.word = word
        self.count = 1
        self.create_id = create_id

class Dictionary:
    def __init__(self):
        self.words = []
        self.sorted_words = []
        self.word_count = 0

    def __add_word(self, word):
        word_obj = Word(word, self.word_count)
        self.words.append(word_obj)
        self.word_count+=1

    def check_and_add_word(self, word):
        pos = next((wd for wd in self.words if wd.word==word), None)
        if pos == None:
            self.__add_word(word)
        else:
            self.words[pos.create_id].count += 1

    def sort_words(self):
        self.sorted_words = sorted(self.words, key=lambda w: w.count, reverse=True)

class FileArray:
    def __init__(self, array):
        self.size = len(array)
        self.array = array
        self.unused_num = []
        self.unused_num_count = 0

    def regist_unused_num(self):
        for i in range(256):
            if (i in self.array) == False:
                self.unused_num.append(i)
        self.unused_num_count = len(self.unused_num)

def encode(array):
    filearray = FileArray(array)
    filearray.regist_unused_num()
    print(filearray.unused_num_count)
    dictionary = Dictionary()
    for i in range(filearray.size-1):
        word = [filearray.array[i],filearray.array[i+1]]
        dictionary.check_and_add_word(word)
    dictionary.sort_words()
    for i in range(dictionary.word_count):
        if dictionary.sorted_words[i].count > 1:
            print(dictionary.sorted_words[i].word,dictionary.sorted_words[i].count)
