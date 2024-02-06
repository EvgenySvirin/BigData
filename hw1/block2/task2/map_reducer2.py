from mrjob.job import MRJob
from mrjob.step import MRStep


class LongestCharacterDialogues(MRJob):
    def get_dialogues(self, _, line):
        records = line.split('" "')
        if len(records) == 3:
            yield records[1], records[2].strip().replace("\"", "")

    def reduce_dialogues(self, character, dialogues):
        max_dialogue = ""
        for dialogue in dialogues:
            if len(max_dialogue) < len(dialogue):
                max_dialogue = dialogue

        yield None, (character, max_dialogue)

    def get_longest(self, _, character_dialogues):
        sorted_dialogues = sorted(character_dialogues, key=lambda x : len(x[1]), reverse=True)
        for ans in sorted_dialogues:
            yield ans

    def steps(self):
        return [
            MRStep(mapper=self.get_dialogues,
                   reducer=self.reduce_dialogues),
            MRStep(reducer=self.get_longest)
        ]


if __name__ == "__main__":
    LongestCharacterDialogues.run()