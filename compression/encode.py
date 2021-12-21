class Word:
    def __init__(self, word, last_word_id, newnum, create_id):
        self.word = word
        self.newnum = newnum
        self.last_word_id = last_word_id
        self.create_id = create_id

class Dictionary:
    def __init__(self):
        self.words = []
        self.word_count = 0

    def __add_word(self, word, last_word_id):
        print(word, last_word_id, word[len(word)-1], self.word_count)
        word_obj = Word(word, last_word_id, word[len(word)-1], self.word_count)
        self.words.append(word_obj)
        self.word_count+=1

    def check_and_add_word(self, word, id):
        pos = next((wd for wd in self.words if wd.word==word), None)
        if pos == None:
            self.__add_word(word, id)
            return 0
        else:
            return pos.create_id

    def create_dictionary(self, filearray):
        word = []
        created_id = 0
        for i in range(filearray.size):
            word.append(filearray.array[i])
            created_id = self.check_and_add_word(word,created_id)
            if created_id == 0:
                word = []

class FileArray:
    def __init__(self, array):
        self.size = len(array)
        self.array = array

def encode(array):
    filearray = FileArray(array)
    dictionary = Dictionary()
    dictionary.create_dictionary(filearray)
    