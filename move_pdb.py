#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:04:49 2021

@author: kamilla
"""
import os
import shutil


motifCA = ['3ml4C01', '2x18E00', '1eazA00', '1p6sA00', '1unqA00', '2i5fA00',
        '1x1gA00', '1x05A00', '1wi1A01', '1fhwA00', '1u29A00', '1fgyA00',
        '1faoA00', '1v5uA00', '4kvgB02', '4hatB00', '5cllB00', '4gn1C02',
        '2dkpA01', '3mpxA02', '4khbB01', '2pz1A03', '1w1hD00', '1v89A00',
        '3voqA00', '1maiA00', '5l81B00', '2ys3A00', '2dhkA01', '5d3xB00',
        '2crfA01', '1tqzA01', '4chjA00', '2yf0A01', '3au4A04',
        '1xkeA00', '1p3rC00', '2d9zA01', '2d9vA01', '2i1jA03', '4yl8A03',
        '2d9wA01', '4l6eA00', '3hk0B02', '1kz7C02', '2cofA00', '1foeC02',
        '3syxA00', '3tfmA02', '2vrwB02', '2lulA00', '2dhiA00', '2kcjA00',
        '1mkeA00', '3f0wA00', '3zvrA03']

motifNCA = ["4f7hA00", "5l81B00", "2ys3A00", "4bbkA00", "1egxA00", "1qc6A00", 
      "2p0hA00", "3pp2A00", "1upqA00", "2yryA00", "2d9yA00", "2dkpA01", 
      "1eazA00", "3aj4A00", "3tfmA02", "2dhiA00", "2d9vA01", "1wgqA00", 
      "2rloA00", "2dn6A00", "1v89A00", "1v5uA00", "1droA00", "3f5rA00", 
      "1wjmA00", "1x1gA00", "2i5fA00", "1x05A00", "1x1fA00", "2cy5A00", 
      "3tfmA01", "1wi1A01", "2d9wA01", "3zvrA03", "1dynA00", "2ys1A00", 
      "4kvgB02", "4gn1C02", "1fgyA00", "1fhwA00", "1u29A00", "1p6sA00", 
      "2x18E00", "1unqA00", "2dhkA01", "2q13A02", "4wsfA00", "3hk0B02", 
      "4k81A02", "4k2pD01", "3a8pB01", "2p8vA00", "2codA01", "3qbvB02", 
      "4hatB00", "5cllB00", "3oanA00", "1faoA00", "2vszB02", "3ml4C01"]

def motifpdbs():
    os.mkdir("NCAmotif_pdbs_raw")

    for pdb in motifNCA:
        shutil.copy(f"/Users/Kamilla/documents/data/all_PH_raw/{pdb}.pdb", f"NCAmotif_pdbs_raw/{pdb}.pdb")

motifpdbs()
