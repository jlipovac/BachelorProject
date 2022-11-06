from simplesam import Reader, Writer
from dataclasses import dataclass
from typing import List

@dataclass
class Read:
    id: str
    positions: List[int]
    qualities: List[float]
    alignments: int = 1

    def __init__(self, id: str, positions: int, qualities: float = 0, alignments: int = 1):
        self.id = id
        self.positions = list()
        self.positions.append(positions)
        self.qualities = list()
        self.qualities.append(qualities)
        self.alignments = alignments
    def avg_quality(self) -> float:
        return sum(self.qualities) / self.alignments
    def add_alignment(self, position, quality):
        self.positions.append(position)
        self.qualities.append(quality)
        self.alignments += 1
        return
    def print(self):
        return "{} {} {} {}\n".format(self.id.ljust(10), self.alignments, self.positions, self.avg_quality())

def main():
    reads = dict()
    in_file = open('alignment.sam', 'r')
    in_sam = Reader(in_file)
    for read in in_sam:
        if read.mapped:
            if read.qname in reads.keys():
                reads[read.qname].add_alignment(read.pos, read.mapq)
            else:
                reads[read.qname] = Read(read.qname, read.pos, read.mapq)

    with open("output.txt", "w") as f:
        f.write('%-35s %6s %-40s %2s\n' % ("Read ID", "mappings", "Start positions", "Avg quality"))
        for read_id, read in reads.items():
            f.write(read.print())
    f.close()

if __name__ == "__main__":
    main()
