import argparse

def ends_with(filename, extensions):
    for ext in extensions:
        if filename.endswith(ext):
            return True
    return False


def add_reference_and_reads(parser):
    parser.add_argument("reference", help="Input file path containing the reference sequence, must be in fasta format")
    parser.add_argument("reads", help="Input file path containing the reads, must be in fasta format")
    args = parser.parse_args()
    extensions = ['.fasta', '.fna', '.ffn', '.faa', '.frn', '.fa']

    if not ends_with(args.reference, extensions):
        raise ValueError('File should be in fasta format')
    if not ends_with(args.reads, extensions):
        raise ValueError('File should be in fasta format')
    return args

def add_reads(parser):
    parser.add_argument("reads", help="Input file path containing the reads, must be in fasta format")
    args = parser.parse_args()
    extensions = ['.fasta', '.fna', '.ffn', '.faa', '.frn', '.fa']

    if not ends_with(args.reads, extensions):
        raise ValueError('File should be in fasta format')
    return args
