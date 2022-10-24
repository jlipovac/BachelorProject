## FAST5 Task

In this part of the project you should get familiar with another format data, fast5. fast5 is a Nanopore data format that stores information on raw signals obtained through ONT Nanopore sequencing process. A gente introduction to the fast5 format is available [here](https://medium.com/@shiansu/a-look-at-the-nanopore-fast5-format-f711999e2ff6). To understand the format you should complete several tasks.

Data:
  * Folder **raw_signals** contains a small subset of 10 signals in fast5 format. These signals are not basecalled (basecalling = a process of converting raw ONT signal to nucleotides).
  * Folder **basecalled_signals** contains the same subset of signals but with basecalling information.


Tasks:
  * Parse signals from folder raw_signals, plot each signal separately, find the length of the signal and calculate the mean value of the signal.
  * Parse signals from folder basecalled_signals and detect which additional information regarding the signal you get from basecalling. 
  * Download and install guppy basecaller (as instructed [here](https://ontpipeline2.readthedocs.io/en/latest/GetStarted.html)). Use guppy to basecall signals in raw_signals folder and compare them to already basecalled signals. Identify differences in basecalls for pairs of signals.

Python library [ont-fast5-api](https://pypi.org/project/ont-fast5-api/0.4.1/) should be quite useful for this task. You can also inspect the content of fast5 file with [hdfview](https://support.hdfgroup.org/products/java/hdfview/). Finally, the instruction on how to use guppy for basecalling can be found [here](https://timkahlke.github.io/LongRead_tutorials/BS_G.html).

