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


spos_Xn = "WNWNWTWTWNWNWNWRWTWTWTWTWPWSWEWEWKWSWLWNRKNWKSWKSWEPGRKNWMGWLKVSMIHDAKEWSSSWRNVWKRWDHLRIFDHLRIFGPIRGWGAFMKPWDDGKKSWEDGKKSWTSQSWVEQGHRRKNWQGHRRKNWQGHKRKNWQGAVMKNWKGAFMKPWRGEYIKTWRGEYIKTWSFKVSMIHLDQPDWTGRGEYIKKNWQDSTGMKLWLYRWDRDVSQWLFRFDKDAKEWLFRFDAEVSQWGMAAAGRSQGQHEGWMVHYTSRDNLEGWLHKRGEYIKTWEGWLHKRGEYIKTWAGYCVKQGAVMKNWQGCLLKQGHRRKNWQGCLLKQGHRRKNWQGFLYLQQQQTFGKQGYLAKQGHKRKNWEGWVQKRGEYIKKNWERAKLYRWDRDVSQWHSGYLWAIGKNVWKRWQGWLHNNGGGSSTLSRRNWMSQDSMMKLKGMAAAGRSQGQHEEFRGVIIKQGCLLKQGHRRKNWPDVSVYRIPPRASNRGYRASDWKLDQPDWTG"
print(spos_Xn.count("T"))


# tot 516 AA in the X(n) position
# A = 19
# G = 51
# E = 21
# R = 44
# W = 69
# Y = 15
# S = 30
# N = 26
# D = 22
# C = 4
# Q = 32
# H = 18
# I = 15
# L = 27
# K = 54
# M = 14
# F = 12
# P = 10
# T = 
# V = 16


























