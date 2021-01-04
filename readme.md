## PhaSeq: predicting protein liquid-liquid phase separation with structural transfer learning

This repository contains the download link of the code for PhaSeq, a predictor of protein liquid-liquid phase separation.

PhaSeq could be download via [Google Drive (faster)](https://drive.google.com/file/d/1uIX3q92wLCSlmVgAGJJkWh29ER76JbkA/view?usp=sharing) or [our local server (slower)](http://db.phasep.pro/static/PhaSeqV2.zip).

## How to use:

An [Anaconda python environment](https://www.anaconda.com/download) is recommend.
Check the requirments.txt file, but primarily:
- Cython>=0.28
- numpy>=1.10
- pandas>=0.15
- scikit-learn>=0.17
- xgboost==1.1.0
- torch==0.4.1
- biopython==1.78
- tqdm>=4

After entering the file directory of PhaSeq, you can use the following code to install all requirments.

`
pip install -r requirments.txt
`
If users failed to install torch==0.4.1, please try
`
conda install pytorch=0.4.1 -c pytorch
`

## Example: prediction of a fasta file.

`
python phaseq.py uniprot.fasta uniprot.txt
`

Input file: uniprot.fasta

Output file: uniprot.txt


## Author:
This software is written by Chunyu Yu.

