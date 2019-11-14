## PhaSeq: predicting protein liquid-liquid phase separation with structural transfer learning

This repository contains the download link of the code for PhaSeq, a predictor of protein liquid-liquid phase separation.

PhaSeq could be download via [this link](http://db.phasep.pro/static/PhaSeq.zip).

## How to use:

An [Anaconda python environment](https://www.anaconda.com/download) is recommend.
Check the requirments.txt file, but primarily:
- Python >= 3.5
- Cython >= 0.28
- numpy >= 1.10
- pandas >= 0.15
- scikit-learn >= 0.17
- xgboost == 0.90
- torch >= 0.4
- biopython == 1.72
- tqdm >= 4

After entering the file directory of PhaSeq, you can use the following code to install all requirments.

`
pip install -r requirments.txt
`

## Example: prediction of a fasta file.


`
python phaseq.py uniprot.fasta uniprot.txt
`

Input file: uniprot.fasta

Output file: uniprot.txt


## Author:
This software is written by Chunyu Yu.

## Cite us:
If you fell this work useful, please cite:


Yu et.al, PhaSeq: predicting protein liquid-liquid phase separation with structural transfer learning (Submitted work).

