from ont_fast5_api.fast5_interface import get_fast5_file
import matplotlib.pyplot as plt
import os, glob
import argparse

parser = argparse.ArgumentParser(
    prog='FAST5 1',
    description='Parses and plots signals from the input folder which should contain one or more fast5 signals files.',
    epilog='some text')
parser.add_argument("input_directory", help="Input directory path containing files in fast5 format")
args = parser.parse_args()

path = args.input_directory
for filename in glob.glob(os.path.join(path, '*.fast5')):
    with get_fast5_file(os.path.join(os.getcwd(), filename), mode="r") as f5:
        for read in f5.get_reads():
            raw_data = read.get_raw_data()
            print(read.read_id, raw_data)
            print("Length of signal: ", len(raw_data))
            print("Mean value of the signal: ", sum(raw_data) / len(raw_data))

            xs = [x for x in range(len(raw_data))]
            plt.plot(xs, raw_data)
            plt.show()
            plt.close()
