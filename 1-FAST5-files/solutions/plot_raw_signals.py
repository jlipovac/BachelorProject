from ont_fast5_api.fast5_interface import get_fast5_file
import matplotlib.pyplot as plt
import os, glob

def plot_all_raw_data():
    path = '../raw_signals'
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

def main():
    plot_all_raw_data()

if __name__ == "__main__":
    main()