# %%file is an Ipython magic function that saves the code cell as a file

from mrjob.job import MRJob # import the mrjob library

class MRSongCount(MRJob):
    #В маппер приходят отдельные строки
    #Например, one, two, three
    #Например, one, two, five
    #Например, two, three, four
    def mapper(self, _, line):
        words = line.lower().replace("(", '').replace(")", '').replace("!", '').replace(".", '').replace(",", '').split()

        word_map = {}
        for word in words:
            if word in word_map:
                word_map[word] = word_map[word] + 1
            else:
                word_map[word] = 1

        for word,size in word_map.items():
            yield (word, size)
    #На выходе у нас пары: (key, value)
    # (one, 1)
    # (two, 1)
    # (three, 1)
    # и так далее

    
    #На выходе у нас пары: (key, спислк всех значений, которые мы получили на предыдущей стадии)
    # (one, [1,1])
    # (two, [1,1, 1])
    # (three, [1,1])
    # (four, [1])
    # и так далее
    def reducer(self, word, values):
        yield (word, sum(values))
        
if __name__ == "__main__":
    MRSongCount.run()
