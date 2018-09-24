InputFile = ['suspect1.txt', 'suspect2.txt', 'suspect3.txt']
sample = ['GTA', 'GGG', 'CAC']


def read_dna(dna_file):
    with open(dna_file, 'r') as f:
        content = f.read()
        return content


def dna_codons(dna):
    length = len(dna)

    return [dna[i:i + 3] for i in range(0, length, 3) if i <= 299]


def match_dna(dna):
    matches = [i for i in dna if i in sample]
    return len(matches)


for file in InputFile:
    content = read_dna(file)
    codons = dna_codons(content)
    matches = match_dna(codons)
    print(matches)
