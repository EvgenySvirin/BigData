from mrjob.job import MRJob
from mrjob.step import MRStep
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk


class BigramFrequencies(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper_init=self.mapper_init,
                mapper=self.get_bigram_ones,
                reducer=self.reduce_ones,
            ),
            MRStep(reducer=self.get_sorted_freqs)
        ]

    def mapper_init(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def get_bigram_ones(self, _, line):
        split_lines = line.strip().split('" "')
        if len(split_lines) != 3:
            return
        line = split_lines[2]
        line = line.lower().replace("(", '').replace(")", '').replace(",", '')
        sentences = nltk.sent_tokenize(line)
        stop_words = set(stopwords.words('english'))
        tokenizer = RegexpTokenizer(r'\w+')
        for sentence in sentences:
            word_tokens = tokenizer.tokenize(sentence)
            word_tokens = [w for w in word_tokens if not w in stop_words]
            for bigram in ngrams(word_tokens, 2):
                yield " ".join(bigram), 1

    def reduce_ones(self, bigram, ones):
        yield None, (bigram, sum(ones))

    def get_sorted_freqs(self, _, bigram_frequencies):
        sorted_frequencies = sorted(bigram_frequencies, key=lambda x: x[1], reverse=True)[:20]
        for ans in sorted_frequencies:
            yield ans


if __name__ == "__main__":
    BigramFrequencies.run()
