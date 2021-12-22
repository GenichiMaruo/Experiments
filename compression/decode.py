from tqdm.auto import tqdm
import itertools
class Word:
    def __init__(self, word, create_id):
        self.word = word
        self.create_id = create_id

class Dictionary:
    def __init__(self):
        self.words = []
        self.words_count = 0
    
    def __add_word(self, word):
        word_obj = Word(word, self.words_count)
        self.words.append(word_obj)
        self.words_count += 1
    
    def create_dictionary(self, filearray):
        word = []
        for i in tqdm(range(0,filearray.size,2),bar_format='{l_bar}{bar:50}{r_bar}{bar:-10b}'):
            relative_pos = filearray.array[i]
            if(relative_pos == 0):
                word.append(filearray.array[i+1])
            else:
                word.extend(itertools.chain(self.words[(int)(i/2)-relative_pos].word,[filearray.array[i+1]]))
            self.__add_word(word)
            word = []

    def export_dictionary(self):
        export_array = []
        for i in range(self.words_count):
            export_array.extend(self.words[i].word)
        return export_array

class FileArray:
    def __init__(self, array):
        self.size = len(array)
        self.array = array

def decode(array):
    filearray = FileArray(array)
    dictionary = Dictionary()
    dictionary.create_dictionary(filearray)
    getarray = dictionary.export_dictionary()
    return getarray