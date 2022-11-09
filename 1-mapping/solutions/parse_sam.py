from simplesam import Reader
from dataclasses import dataclass
from typing import List
import argparse

parser = argparse.ArgumentParser(
    prog='Mapping assignment',
    description='Creates an \"output.txt\" file where it stores the total number of mappings, the start '
                'position/positions of the mapping to the reference and the average quality of the mapping for each '
                'read_id that is in the input .sam file. Skips the reads that are not mapped.')
parser.add_argument("alignment", help="Input file path containing alignment, must be in sam format")
args = parser.parse_args()

if not args.alignment.endswith('.sam'):
    raise ValueError('File should be in sam format')


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
        return "{} {} {} {}\n".format(self.id, self.alignments, self.positions, self.avg_quality())


reads = dict()
in_file = open(args.alignment, 'r')
in_sam = Reader(in_file)
for read in in_sam:
    if read.mapped:
        if read.qname in reads.keys():
            reads[read.qname].add_alignment(read.pos, read.mapq)
        else:
            reads[read.qname] = Read(read.qname, read.pos, read.mapq)

with open('output.txt', 'w') as f:
    f.write('%-35s %6s %-40s %2s\n' % ("Read ID", "mappings", "Start positions", "Avg quality"))
    for read_id, read in reads.items():
        f.write(read.print())
f.close()
