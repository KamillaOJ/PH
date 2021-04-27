import sys

with open (sys.argv[1], "r") as cath:
    cath_S = []
    lines = cath.readlines()
    for line in lines:
        cath_S.append(line[0:7])

def find_template(filename_pdb, filename_txt):
    """Get the AA sequence from a PDB file and save it in a text file"""
    with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as temp_file:
        temp_file.write(f">{filename_pdb[11:18]}  _P_ {filename_pdb[11:16]}\n")


for file in sys.argv[3:]:
    if str(file[11:18]) in cath_S:
        find_template(file, sys.argv[2])




###what i wrote in the command line for S35:
###data kamilla$ python FS_all_PH_templist.py cath_S35.txt PH_temp_S35.txt all_PH_raw/*.pdb
