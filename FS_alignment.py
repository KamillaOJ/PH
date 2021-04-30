#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:21:10 2021

@author: kamilla
"""

from Bio import AlignIO

AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]

alignmentfile = "/Users/Kamilla/documents/data/Anathasois/S60/all_PHS60_min8_clustal.aln"
alignment = AlignIO.read(alignmentfile, "clustal")

loop1_range = [197, 291]
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

for AA in AAs:
    AAcount = sseqloop2.count(AA)
    percentage = AAcount/12.06
    print(f"{AA} = {AAcount} = {percentage:.2f}%")


