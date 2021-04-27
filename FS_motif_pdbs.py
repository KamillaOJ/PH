import sys

def find_sequence(filename_pdb, filename_txt):
    """Get the AA sequence from a PDB file and save it in a text file"""
    with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as seq_file:
        ca_lines = []
        sequence = ""
        lines = pdb_file.readlines()

        amino_acids = {"ALA": "A", "GLY": "G", "GLU": "E", "ARG": "R",
                "TRP": "W", "TYR": "Y", "SER": "S", "ASN": "N",
                "ASP": "D", "CYS": "C", "GLN": "Q", "HIS": "H",
                "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M",
                "PHE": "F", "PRO": "P", "THR": "T", "VAL": "V"}

        for line in lines:
            if line[12:16].strip() == "CA":
                ca_lines.append(line)
                sequence = sequence + amino_acids[line[17:20]]

        new_sequence = ""
        for aa in sequence:
            new_sequence += aa
            if len(new_sequence.replace("\n", "")) % 70 == 0:
                new_sequence += "\n"


        seq_file.write(f">{filename_pdb[15:22]}\n")
        seq_file.write(new_sequence)
        seq_file.write("\n")

for file in sys.argv[2:]:
        find_sequence(file, sys.argv[1])

# python FS_motif_pdbs.py PH_motif_seqs.fasta motif_pdbs_raw/*.pdb
