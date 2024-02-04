from mrjob.job import MRJob
from mrjob.step import MRStep


class CountCharacterDialogues(MRJob):
    def get_ones(self, _, line):
        records = line.split('" "')
        if len(records) == 3:
            yield records[1], 1

    def reduce_ones(self, character, ones):
        yield None, (character, sum(ones))

    def get_most_frequent(self, _, character_counts):
        sorted_frequencies = sorted(character_counts, key=lambda x: x[1], reverse=True)
        for character_count in sorted_frequencies[:20]:
            yield character_count

    def steps(self):
        return [
            MRStep(mapper=self.get_ones,
                   reducer=self.reduce_ones),
            MRStep(reducer=self.get_most_frequent)
        ]


if __name__ == "__main__":
    CountCharacterDialogues.run()
