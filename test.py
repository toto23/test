import csv

infile="data/Test_file.csv"

print(str(infile))
with open(infile, encoding="windows-1252") as inf:
    reader = csv.DictReader(inf, delimiter=';')
    # for row in reader:
    #     print(row)
    print(str(reader.fieldnames))
inf.close

