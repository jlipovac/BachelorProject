## Intro

In this task, you will get familiar with the problem of mapping a set of reads to a reference. The reference and reads are in FASTA format. The objective of mapping task is to align the reads to reference in such way that the best match between the read sequence and part of the reference sequence is found. This way, we can extract the information about the region in the reference a read belongs to.

## Tools

The tool you would use is available here: https://github.com/lh3/minimap2. minimap2 is a commonly used mapper that outputs mapping information.

## Task

You will receive data (fastq files) containing ONT reads of Vibrio harveyi virus. 

* The obtained reads must be mapped to the reference (fasta file). The reference is the chromosome 1 of Vibrio harveyi virus. We do mapping to find out which read belongs to which part of the genome.

We want the output of minimap2 to be in .sam format - use the instructions on the Github page to get the desired output.

The .sam file format specifications can be found here: https://samtools.github.io/hts-specs/SAMv1.pdf

* The second task is to write a python script to parse the .sam file. In an output txt file, it is necessary to print for each read_id that is in the .sam file the total number of mappings, the initial position/positions of the mapping to the reference and the average quality of the mapping.  Skip the reads that are not mapped ( * in the third column of the sam file).

Example of two lines of output file:

fdf34b2b-93de-4aa7-a4eb-9d09d9569be8	1	2346	45
8e14d498-c647-4434-b5fe-ee055f4fb09e	2	45565, 235676	46.5

The first column contains the read_id. The second contains the number of occurrences in the .sam file, more precisely the number of mappings of that read. In the third column is the starting mapping position, if there are more than one, they must be separated by a comma. In the fourth, the average quality of mapping. Columns are separated by a tab delimiter.
