import sys
with open(sys.argv[1], "r") as file:
    data = file.read()
    pdb_number = data.count(">")
    print(pdb_number)
