with open('/Users/mujeebqadiri/Desktop/rosalind_prot-2.txt', 'r') as file:
    data = file.read().replace('\n', '')

a = ''

mydict = {
    'UUU' : 'F', 'UUC' : 'F',
    'UUA' : 'L', 'UUG' : 'L',
    'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S',
    'UAU' : 'Y', 'UAC' : 'Y',
    'UAA' : 'Stop', 'UAG' : 'Stop', 'UGA' : 'Stop',
    'UGU' : 'C', 'UGC' : 'C',
    'UGG' : 'W',
    'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
    'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
    'CAU' : 'H', 'CAC' : 'H',
    'CAA' : 'Q', 'CAG' : 'Q',
    'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',
    'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I',
    'AUG' : 'M',
    'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
    'AAU' : 'N', 'AAC' : 'N',
    'AAA' : 'K', 'AAG' : 'K',
    'AGU' : 'S', 'AGC' : 'S',
    'AGA' : 'R', 'AGG' : 'R',
    'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
    'GCU' : 'A', 'GCC' : 'A', 'GCA': 'A','GCG' : 'A',
    'GAU' : 'D', 'GAC' : 'D',
    'GAA' : 'E', 'GAG' : 'E',
    'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G',
}

def search(codon):
    for key, value in mydict.items():
        if codon == key:
            return value

for i in range(0, len(data), 3):
    codon = data[i: i + 3]
    key = search(codon)
    a = a + key

print(a)