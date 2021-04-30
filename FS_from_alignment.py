#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:25:28 2021

@author: kamilla
"""


import sys
from Bio import AlignIO


# alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/56motif.fa"
# alignment = AlignIO.read(alignmentfile, "fasta")

# b1loop1b2_range = [50,130]

# seqresults_b1loop1b2 = {}
# lenresults_b1loop1b2 = {}

# for record in alignment:
#     seqid = record.id[:7]
#     seq = record.seq
#     loop_stripped = seq[b1loop1b2_range[0]:b1loop1b2_range[1]]
#     loop_ungapped = loop_stripped.ungap()
#     loop_len = len(loop_ungapped)

#     seqresults_b1loop1b2[seqid] = loop_ungapped
#     lenresults_b1loop1b2[seqid] = loop_len

# def findloopseq(filename_txt):
#     with open(filename_txt, "a") as seq_file:
#         alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/56motif.fa"
#         alignment = AlignIO.read(alignmentfile, "fasta")

#         #b1loop1b2_range = [50,130]
#         loop_range = [80, 100]

#         # seqresults_b1loop1b2 = {}
#         # lenresults_b1loop1b2 = {}
#         seqresults_loop = {}
#         lenresults_loop = {}

#         for record in alignment:
#             seqid = record.id[:7]
#             seq = record.seq
#             loop_stripped = seq[loop_range[0]:loop_range[1]]
#             loop_ungapped = loop_stripped.ungap()
#             sequence = str(loop_ungapped)
#             loop_len = len(loop_ungapped)

#             seqresults_loop[seqid] = loop_ungapped
#             lenresults_loop[seqid] = loop_len

#             # seq_file.write(f">{seqid}\n")
#             # seq_file.write(sequence)
#             # seq_file.write("\n")

#         # print(seqresults_b1loop1b2)
#         # print(lenresults_b1loop1b2)


# findloopseq(sys.argv[1])

alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/56motif.fa"
alignment = AlignIO.read(alignmentfile, "fasta")

loop_range = [80, 100]

seqresults_loop = {}
lenresults_loop = {}
lseqloop = []
for record in alignment:
    seqid = record.id[:7]
    seq = record.seq
    loop_stripped = seq[loop_range[0]:loop_range[1]]
    loop_ungapped = loop_stripped.ungap()
    sequence = str(loop_ungapped)
    loop_len = len(loop_ungapped)

    seqresults_loop[seqid] = loop_ungapped
    lenresults_loop[seqid] = loop_len

    lseqloop.append(sequence)
    sseqloop = "".join(lseqloop)

#print(sseqloop)
sseqloop = "RPRKLTLKGRPRKLTLKGGGGSSTLSRRNWSTILKRWSSILRRWGSGLSSVTSRDNLRGEYIKTWGEYIKKNWGEYIKTWGGKGPIRGWGGLVKTWGHRRKNWGHRRKNWGHKRKNWGAVMKNWKDNPQRSYVNSQWRSIVKNWGAFMKPWQQQTFGKKWDKTSQSWELGKKSWEDGKKSWDDGKKSWDSTGMKLWGGRVKTWGGRVKTWGGGRVKTWNIGIMSDGKKWSQQKKKTSPTNYLTGWGKNRDVESKEWDAEVSQWDRDVSQWDKDAKEWGKNVWKRWSKTSVIWLNPPESRGMHVCEDDVPDARGDKMSQDSMMKLKSAGNITQPQAKSKSSSWRSKEAFDNWECKEGGFPRFTKGLFATDHKELARRNKKNKNKKGPPRASNRGSVERRSK"

    
# #print(lenresults_loop)
# #print(seqloop)

# #range loop [0, 20]
# llenloop = []

    
# for key in seqresults_loop:
#     seqloop.append(seqresults_loop[key])
    
# # for d in lenresults_loop:
# #     for key in d:
# #         print([key])

# #the avergave loop length is 7,14 AAs. 
# #print(sum(llenloop)/len(llenloop))

# #print(seqresults_loop)

#print(len(sseqloop))
AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]

for AA in AAs:
    AAcount = sseqloop.count(AA)
    percentage = AAcount/4
    print(F"{AA} = {AAcount} = {percentage}%")


#sseqloop = "RPRKLTLKGRPRKLTLKGGGGSSTLSRRNWSTILKRWSSILRRWGSGLSSVTSRDNLRGEYIKTWGEYIKKNWGEYIKTWGGKGPIRGWGGLVKTWGHRRKNWGHRRKNWGHKRKNWGAVMKNWKDNPQRSYVNSQWRSIVKNWGAFMKPWQQQTFGKKWDKTSQSWELGKKSWEDGKKSWDDGKKSWDSTGMKLWGGRVKTWGGRVKTWGGGRVKTWNIGIMSDGKKWSQQKKKTSPTNYLTGWGKNRDVESKEWDAEVSQWDRDVSQWDKDAKEWGKNVWKRWSKTSVIWLNPPESRGMHVCEDDVPDARGDKMSQDSMMKLKSAGNITQPQAKSKSSSWRSKEAFDNWECKEGGFPRFTKGLFATDHKELARRNKKNKNKKGPPRASNRGSVERRSK"    
    
# A = 11 = 2,75%
# G = 46 = 11,5%
# E = 16 = 4%
# R = 35 = 8,75%
# W = 35 = 8,75%
# Y = 5 = 1,25%
# S = 39 = 9,75%
# N = 21 = 5,25%
# D = 21 = 5,25%
# C = 2 = 0,5%
# Q = 13 = 3,25%
# H = 5 = 1,25%
# I = 11 = 2.75%
# L = 17 = 4.25%
# K = 59 = 14.75%
# M = 8 = 2.0%
# F = 6 = 1.5%
# P = 13 = 3.25%
# T = 21 = 5.25%
# V = 16 = 4.0%



    
    
    
    
    
    
    
    
    