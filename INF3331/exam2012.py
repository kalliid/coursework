import csv

def readcsv(filename):
    with open(filename, 'rb') as infile:
        
        dialect = csv.Sniffer().sniff(infile.read())
        infile.seek(0)
        reader = csv.DictReader(infile, dialect=dialect)        

        data = [d for d in reader]

    return data, reader.fieldnames

def writecsv(namelist, fieldnames, filename):
    with open(filename, 'wb') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        writer = csv.DictWriter(outfile, fieldnames)
        for d in namelist:
            writer.writerow(d)


if __name__ == "__main__":
    namelist, fieldnames = readcsv("input_file.csv")
    writecsv(namelist, fieldnames, 'output_file.csv')

