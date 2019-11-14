import pickle
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils.rnn import PackedSequence
import torch.utils.data
from src.alphabets import Uniprot21,loadmod
import warnings
from tqdm import tqdm
from Bio import SeqIO
import sys
args=sys.argv[1:]


warnings.filterwarnings('ignore')

loaded_model = pickle.load(open("./src/phaseq.dat", "rb"))
locmodel='./src/epoch100.sav'
encoder = torch.load(locmodel)
encoder.eval()
encoder = encoder.embedding
lm_embed = encoder.embed
lstm_stack = loadmod.unstack_lstm(encoder.rnn)
proj = encoder.proj
alphabet = Uniprot21()
embs=[]
ids=[]
seq_records=[seq_record for seq_record in SeqIO.parse(args[0], "fasta")]

for seq_record in tqdm(seq_records):
    x=str.encode(str(seq_record.seq))
    x0 = alphabet.encode(x)
    x1 = torch.from_numpy(x0).long().unsqueeze(0)

    z_x = loadmod.featurize(x1, lm_embed, lstm_stack, proj, include_lm=True, lm_only=False)
    z_x = z_x.squeeze(0).cpu()
    embs.append(z_x.mean(0).detach().numpy())
    ids.append(seq_record.id)
    
pd.DataFrame(loaded_model.predict_proba(embs)[:,1],ids).to_csv(args[1])