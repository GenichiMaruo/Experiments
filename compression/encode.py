class Word:
    def __init__(self, word, last_word_relative_pos, create_id):
        self.word = word
        self.newnum = word[len(word)-1]
        self.last_word_relative_pos = last_word_relative_pos
        self.create_id = create_id

class Dictionary:
    size = 255

    def __init__(self):
        self.words = []
        self.search_words = []
        self.words_count = 0

    def __add_word(self, word, last_word_relative_pos):
        word_obj = Word(word, last_word_relative_pos, self.words_count)
        self.search_words.insert(0, word_obj)
        if self.words_count >= self.size:
            del self.search_words[self.size]
        self.words.append(word_obj)
        self.words_count += 1

    def check_and_add_word(self, word, id):
        pos = next((wd for wd in self.search_words if wd.word==word), None)
        if pos == None:
            self.__add_word(word, id)
            return 0
        else:
            return self.words_count - pos.create_id

    def create_dictionary(self, filearray):
        word = []
        created_id = 0
        for i in range(filearray.size):
            word.append(filearray.array[i])
            created_id = self.check_and_add_word(word, created_id)
            if created_id == 0:
                word = []

    def export_dictionary(self):
        export_array = []
        for i in range(self.words_count):
            export_array.extend([self.words[i].last_word_relative_pos,self.words[i].newnum])
        return export_array

class FileArray:
    def __init__(self, array):
        self.size = len(array)
        self.array = array

def encode(array):
    filearray = FileArray(array)
    dictionary = Dictionary()
    dictionary.create_dictionary(filearray)
    presarray = dictionary.export_dictionary()
    print(len(array),'->',len(presarray))
    return presarray
    