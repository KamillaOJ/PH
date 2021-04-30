x1 = {"3ml4C01": "KWKSR"}
x2 = {"2x18E00": "KNWRPR",
"1eazA00": "KNWKRR",
"1p6sA00": "KTWRPR",
"1unqA00": "KTWRPR",
"2i5fA00": "KNWKVR",
"1x1gA00": "KNWKVR",
"1x05A00": "KNWKVR",
"1wi1A01": "KRWKKR",
"1fhwA00": "KTWKRR",
"1u29A00": "KTWKRR",
"1fgyA00": "KTWKRR",
"1faoA00": "KTWKTR",
"1v5uA00": "KPWKAR",
"4kvgB02": "KSWKRR",
"4hatB00": "KEWKER",
"5cllB00": "KEWKER",
"3ml4C01": "KKWKSR",
"4gn1C02": "KSWKKR",
"2dkpA01": "KLWKKR",
"3mpxA02": "KNRRPR"}
x3 = {"2x18E00": "KKNWRPR",
"4kvgB02": "KKSWKRR",
"4gn1C02": "KKSWKKR",
"4khbB01": "KEPGKCR"}
x4 = {"1x1gA00": "KRKNWKVR"}
x5 = {"1v89A00": "KMGWLKKQR",
"3voqA00": "KVSMIHRLR",
"4hatB00": "KDAKEWKER",
"1maiA00": "KSSSWRRER"}
x6 = {"1wi1A01": "KNVWKRWKKR",
"5l81B00": "KDHLRIFRPR",
"2ys3A00": "KDHLRIFRPR",
"2dhkA01": "KGPIRGWKSR"}
x7 = {"1v5uA00": "KGAFMKPWKAR",
"4gn1C02": "KDDGKKSWKKR",
"4kvgB02": "KEDGKKSWKRR",
"2crfA01": "KTSQSWVERGR"}
x8 = {"2i5fA00": "KQGHRRKNWKVR",
"1x05A00": "KQGHRRKNWKVR",
"1x1gA00": "KQGHKRKNWKVR",
"1eazA00": "KQGAVMKNWKRR",
"1v5uA00": "KKGAFMKPWKAR",
"1p6sA00": "KRGEYIKTWRPR",
"1unqA00": "KRGEYIKTWRPR",
"3voqA00": "KSFKVSMIHRLR",
"1tqzA01": "KLDQPDWTGRLR"}
x9 = {"2x18E00": "KRGEYIKKNWRPR",
"2dkpA01": "KQDSTGMKLWKKR"}
x11 = {"4l6eA00": "KLYRWDRDVSQWKER",
"4hatB00": "KLFRFDKDAKEWKER",
"1xkeA00": "KLFRFDAEVSQWKER"}
x12 = {"1p3rC00": "KGMAAAGRSQGQHKQR"}
x13 = {"2d9zA01": "KEGWMVHYTSRDNLRKR"}
x14 = {"1p6sA00": "KEGWLHKRGEYIKTWRPR",
"1unqA00": "KEGWLHKRGEYIKTWRPR",
"1eazA00": "KAGYCVKQGAVMKNWKRR",
"2i5fA00": "KQGCLLKQGHRRKNWKVR",
"1x05A00": "KQGCLLKQGHRRKNWKVR",
"2d9wA01": "KQGFLYLQQQQTFGKKWR",
"1x1gA00": "KQGYLAKQGHKRKNWKVR"}
x15 = {"2x18E00": "KEGWVQKRGEYIKKNWRPR",
"4l6eA00": "KERAKLYRWDRDVSQWKER"}
x16 = {"1wi1A01": "KHSGYLWAIGKNVWKRWKKR"}
x19 = {"3tfmA02": "KQGWLHNNGGGSSTLSRRNWKKR"}
x22 = {"1p3rC00": "KMSQDSMMKLKGMAAAGRSQGQHKQR"}
x23 = {"1x05A00": "KEEFRGVIIKQGCLLKQGHRRKNWKVR"}
x31 = {"1tqzA01": "KPDVSVYRIPPRASNRGYRASDWKLDQPDWTGRLR"}

allxmotifs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x11, x12, x13, x14, x15, x16,
            x19, x22, x23, x31]

# pdbs = []
# list_of_motifseqs = []

## Get CATHid
# for xn_motifs in allxmotifs:
#     for key in xn_motifs:
#         if key not in pdbs:
#             pdbs.append(key)

## Get motif sequence
# for d in allxmotifs:
#     for key in d:
#         list_of_motifseqs.append(d[key])
        
pdbs = ['3ml4C01', '2x18E00', '1eazA00', '1p6sA00', '1unqA00', '2i5fA00',
        '1x1gA00', '1x05A00', '1wi1A01', '1fhwA00', '1u29A00', '1fgyA00',
        '1faoA00', '1v5uA00', '4kvgB02', '4hatB00', '5cllB00', '4gn1C02',
        '2dkpA01', '3mpxA02', '4khbB01', '1v89A00', '3voqA00', '1maiA00',
        '5l81B00', '2ys3A00', '2dhkA01', '2crfA01', '1tqzA01', '4l6eA00',
        '1xkeA00', '1p3rC00', '2d9zA01', '2d9wA01', '3tfmA02']

list_of_motifseqs = ['KWKSR', 'KNWRPR', 'KNWKRR', 'KTWRPR', 'KTWRPR', 'KNWKVR',
                     'KNWKVR', 'KNWKVR', 'KRWKKR', 'KTWKRR', 'KTWKRR', 'KTWKRR',
                     'KTWKTR', 'KPWKAR', 'KSWKRR', 'KEWKER', 'KEWKER', 'KKWKSR',
                     'KSWKKR', 'KLWKKR', 'KNRRPR', 'KKNWRPR', 'KKSWKRR',
                     'KKSWKKR', 'KEPGKCR', 'KRKNWKVR', 'KMGWLKKQR', 'KVSMIHRLR',
                     'KDAKEWKER', 'KSSSWRRER', 'KNVWKRWKKR', 'KDHLRIFRPR',
                     'KDHLRIFRPR', 'KGPIRGWKSR', 'KGAFMKPWKAR', 'KDDGKKSWKKR',
                     'KEDGKKSWKRR', 'KTSQSWVERGR', 'KQGHRRKNWKVR', 'KQGHRRKNWKVR',
                     'KQGHKRKNWKVR', 'KQGAVMKNWKRR', 'KKGAFMKPWKAR', 'KRGEYIKTWRPR',
                     'KRGEYIKTWRPR', 'KSFKVSMIHRLR', 'KLDQPDWTGRLR',
                     'KRGEYIKKNWRPR', 'KQDSTGMKLWKKR', 'KLYRWDRDVSQWKER',
                     'KLFRFDKDAKEWKER', 'KLFRFDAEVSQWKER', 'KGMAAAGRSQGQHKQR',
                     'KEGWMVHYTSRDNLRKR', 'KEGWLHKRGEYIKTWRPR',
                     'KEGWLHKRGEYIKTWRPR', 'KAGYCVKQGAVMKNWKRR',
                     'KQGCLLKQGHRRKNWKVR', 'KQGCLLKQGHRRKNWKVR',
                     'KQGFLYLQQQQTFGKKWR', 'KQGYLAKQGHKRKNWKVR',
                     'KEGWVQKRGEYIKKNWRPR', 'KERAKLYRWDRDVSQWKER',
                     'KHSGYLWAIGKNVWKRWKKR', 'KQGWLHNNGGGSSTLSRRNWKKR',
                     'KMSQDSMMKLKGMAAAGRSQGQHKQR', 'KEEFRGVIIKQGCLLKQGHRRKNWKVR',
                     'KPDVSVYRIPPRASNRGYRASDWKLDQPDWTGRLR']
        
# lpos_min2 = []
# spos_min2 = ""
# for seq in list_of_motifseqs:
#     lpos_min2.append(seq[-2])

# print(lpos_min2)
# spos_min2 = "".join(lpos_min2)
# print(spos_min2)

## 68 motifs in 35 PDBs
spos_min2 = "SPRPPVVVKRRRTAREESKKPPRKCVQLEEKPPSAKRGVVVRAPPLLPKEEEQKPPRVVWVPEKKQVL"


# # print(len(list_of_motifseqs))
# print(spos_min2.count("V"))

# tot 100,01%
# A = 3 = 4,41%
# G = 1 = 1,47%
# E = 8 = 11,77%
# R = 9 = 13,24%
# W = 1 = 1,47%
# Y = 0
# S = 3 = 4,41%
# N = 0
# D = 0
# C = 1 = 1,47%
# Q = 3 = 4,41%
# H = 0
# I = 0
# L = 4 = 5,88%
# K = 10 = 14,71%
# M = 0
# F = 0
# P = 13 = 19,12%
# T = 1 = 1,47%
# V = 11 = 16,18%


lpos_Xn = []
spos_Xn = ""
for seq in list_of_motifseqs:
    lpos_Xn.append(seq[1:-3])
    


spos_Xn = "".join(lpos_Xn)




#spos_Xn = "WNWNWTWTWNWNWNWRWTWTWTWTWPWSWEWEWKWSWLWNRKNWKSWKSWEPGRKNWMGWLKVSMIHDAKEWSSSWRNVWKRWDHLRIFDHLRIFGPIRGWGAFMKPWDDGKKSWEDGKKSWTSQSWVEQGHRRKNWQGHRRKNWQGHKRKNWQGAVMKNWKGAFMKPWRGEYIKTWRGEYIKTWSFKVSMIHLDQPDWTGRGEYIKKNWQDSTGMKLWLYRWDRDVSQWLFRFDKDAKEWLFRFDAEVSQWGMAAAGRSQGQHEGWMVHYTSRDNLEGWLHKRGEYIKTWEGWLHKRGEYIKTWAGYCVKQGAVMKNWQGCLLKQGHRRKNWQGCLLKQGHRRKNWQGFLYLQQQQTFGKQGYLAKQGHKRKNWEGWVQKRGEYIKKNWERAKLYRWDRDVSQWHSGYLWAIGKNVWKRWQGWLHNNGGGSSTLSRRNWMSQDSMMKLKGMAAAGRSQGQHEEFRGVIIKQGCLLKQGHRRKNWPDVSVYRIPPRASNRGYRASDWKLDQPDWTG"
#print(spos_Xn.count("T"))


# tot 516 AA in the X(n) position
# random would be 5% (25,8) of each AA. 
# A = 19 = 3,68%
# G = 51 = 9,88%
# E = 21 = 4,07%
# R = 44 = 8,53%
# W = 69 = 13,37%
# Y = 15 = 2,91%
# S = 30 = 5,81%
# N = 26 = 5,04%
# D = 22 = 2,26%
# C = 4 = 0,88%
# Q = 32 = 6,20%
# H = 18 = 3,49%
# I = 15 = 2,91%
# L = 27 = 5,23%
# K = 54 = 10,47%
# M = 14 = 2,71%
# F = 12 = 2,33%
# P = 10 = 1,94%
# T = 17 = 3,30%
# V = 16 = 3,10%

# Aromatic (W, Y, F, H) = 114 = 22,09%
# Basic (K/R) = 98 = 19,00%

AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]

spos_Xn = "WNWNWTWTWNWNWNWRWTWTWTWTWPWSWEWEWKWSWLWNRKNWKSWKSWEPGRKNWMGWLKVSMIHDAKEWSSSWRNVWKRWDHLRIFDHLRIFGPIRGWGAFMKPWDDGKKSWEDGKKSWTSQSWVEQGHRRKNWQGHRRKNWQGHKRKNWQGAVMKNWKGAFMKPWRGEYIKTWRGEYIKTWSFKVSMIHLDQPDWTGRGEYIKKNWQDSTGMKLWLYRWDRDVSQWLFRFDKDAKEWLFRFDAEVSQWGMAAAGRSQGQHEGWMVHYTSRDNLEGWLHKRGEYIKTWEGWLHKRGEYIKTWAGYCVKQGAVMKNWQGCLLKQGHRRKNWQGCLLKQGHRRKNWQGFLYLQQQQTFGKQGYLAKQGHKRKNWEGWVQKRGEYIKKNWERAKLYRWDRDVSQWHSGYLWAIGKNVWKRWQGWLHNNGGGSSTLSRRNWMSQDSMMKLKGMAAAGRSQGQHEEFRGVIIKQGCLLKQGHRRKNWPDVSVYRIPPRASNRGYRASDWKLDQPDWTG"

totAA = 0.68

hydrophobic = 0
aromatic = 0
positive = 0
negative = 0
non_polar = 0
polar = 0


for AA in AAs:
    AAcount = spos_min2.count(AA)
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
























