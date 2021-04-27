import sys

with open (sys.argv[1], "r") as cath60:
    cath_S60 = []
    lines = cath60.readlines()
    for line in lines:
        cath_S60.append(line[0:7])

with open (sys.argv[2], "r") as cath35:
    cath_S35 = []
    lines = cath35.readlines()
    for line in lines:
        cath_S35.append(line[0:7])

def find_pdbcode(filename_pdb, filename_txt):
    """"""
    with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as pdb_codes:
        pdb_codes.write(f">{filename_pdb[11:18]}\n")



for file in sys.argv[4:]:
    if str(file[11:18]) in cath_S60 and str(file[11:18]) not in cath_S35:
        find_pdbcode(file, sys.argv[3])



# python find_cluster.py cath_S60.txt cath_S35.txt S60notS35.txt all_PH_raw/*.pdb
