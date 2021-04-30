#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:21:10 2021

@author: kamilla
"""

from Bio import AlignIO

AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]

AATYPE3 = {
    "LEU": "Hydrophobic,H-non-aromatic",
    "ILE": "Hydrophobic,H-non-aromatic",
    "CYS": "Hydrophobic,H-non-aromatic",
    "MET": "Hydrophobic,H-non-aromatic",
    "TYR": "Hydrophobic,H-aromatic",
    "TRP": "Hydrophobic,H-aromatic",
    "PHE": "Hydrophobic,H-aromatic",
    "HIS": "Positive",
    "LYS": "Positive",
    "ARG": "Positive",
    "ASP": "Negative",
    "GLU": "Negative",
    "VAL": "Non-polar",
    "ALA": "Non-polar",
    "SER": "Polar",
    "ASN": "Polar",
    "GLY": "Non-polar",
    "PRO": "Non-polar",
    "GLN": "Polar",
    "THR": "Polar",
    "UNK": "none"
}

AATYPE1 = {
    "L": "Hydrophobic,H-non-aromatic",
    "I": "Hydrophobic,H-non-aromatic",
    "C": "Hydrophobic,H-non-aromatic",
    "M": "Hydrophobic,H-non-aromatic",
    "Y": "Hydrophobic,H-aromatic",
    "W": "Hydrophobic,H-aromatic",
    "F": "Hydrophobic,H-aromatic",
    "H": "Positive",
    "K": "Positive",
    "R": "Positive",
    "D": "Negative",
    "E": "Negative",
    "V": "Non-polar",
    "A": "Non-polar",
    "S": "Polar",
    "N": "Polar",
    "G": "Non-polar",
    "P": "Non-polar",
    "Q": "Polar",
    "T": "Polar",
    "X": "none"
}

alignmentfile = "/Users/Kamilla/documents/data/Anathasois/S60/all_PHS60_min8_clustal.aln"
alignment = AlignIO.read(alignmentfile, "clustal")

loop1_range = [200, 286]
loop2_range = [334, 445]

seqresults_loop1 = {}
lenresults_loop1 = {}
lseqloop1 = []
sseqloop1 = ""

seqresults_loop2 = {}
lenresults_loop2 = {}
lseqloop2 = []
sseqloop2 = ""

for record in alignment:
    seqid = record.id[:7]
    seq = record.seq
   
    #Loop 1
    loop_stripped1 = seq[loop1_range[0]:loop1_range[1]]
    loop_ungapped1 = loop_stripped1.ungap()
    sequence1 = str(loop_ungapped1)
    loop_len1 = len(loop_ungapped1)

    seqresults_loop1[seqid] = loop_ungapped1
    lenresults_loop1[seqid] = loop_len1

    lseqloop1.append(sequence1)
    sseqloop1 = "".join(lseqloop1)

    # Loop 2
    loop_stripped2 = seq[loop2_range[0]:loop2_range[1]]
    loop_ungapped2 = loop_stripped2.ungap()
    sequence2 = str(loop_ungapped2)
    loop_len2 = len(loop_ungapped2)


    seqresults_loop2[seqid] = loop_ungapped2
    lenresults_loop2[seqid] = loop_len2

    lseqloop2.append(sequence2)
    sseqloop2 = "".join(lseqloop2)
    
#print(len(sseqloop1)/150)
#print(len(sseqloop2))

# for AA in AAs:
#     AAcount = sseqloop1.count(AA)
#     percentage = AAcount/11.67
    

#     print(f"{AA} = {AAcount} = {percentage:.2f}%")

totAA = 12.06

hydrophobic = 0
aromatic = 0
positive = 0
negative = 0
non_polar = 0
polar = 0


for AA in AAs:
    AAcount = sseqloop2.count(AA)
    if AA == "L":
        hydrophobic = hydrophobic + AAcount
    elif AA == "I":
        hydrophobic = hydrophobic + AAcount
    elif AA == "C":
        hydrophobic = hydrophobic + AAcount
    elif AA == "M":
        hydrophobic = hydrophobic + AAcount
    elif AA == "W":
        hydrophobic = hydrophobic + AAcount 
        aromatic = aromatic + AAcount
    elif AA == "Y":
        hydrophobic = hydrophobic + AAcount
        aromatic = aromatic + AAcount
    elif AA == "F":
        hydrophobic = hydrophobic + AAcount
        aromatic = aromatic + AAcount
    elif AA == "D":
        negative = negative + AAcount
    elif AA == "E":
        negative = negative + AAcount
    elif AA == "V":
        non_polar = non_polar + AAcount
    elif AA == "A":
        non_polar = non_polar + AAcount
    elif AA == "G":
        non_polar = non_polar + AAcount
    elif AA == "P":
        non_polar = non_polar + AAcount
    elif AA == "S":
        polar = polar + AAcount
    elif AA == "N":
        polar = polar + AAcount
    elif AA == "Q":
        polar = polar + AAcount
    elif AA == "T":
        polar = polar + AAcount
    elif AA == "H":
        positive = positive + AAcount
    elif AA == "K":
        positive = positive + AAcount        
    elif AA == "R":
        positive = positive + AAcount
        
        
hp = hydrophobic/totAA           
ap = aromatic/totAA 
ppos = positive/totAA
np = negative/totAA       
npp = non_polar/totAA 
ppol = polar/totAA       
        
    

print(f"Hydrophobic AAs = {hydrophobic} = {hp:.2f}%")
print(f"Aromatic AAs = {aromatic} = {ap:.2f}%")
print(f"Positive AAs = {positive} = {ppos:.2f}%")
print(f"Negative AAs = {negative} = {np:.2f}%")
print(f"Non polar AAs = {non_polar} = {npp:.2f}%")
print(f"Polar AAs = {polar} = {ppol:.2f}%")



hydrophobic1 = 0
armotaic1 = 0
positive1 = 0
negative1 = 0
non_polar1 = 0
polar1 = 0


















        
