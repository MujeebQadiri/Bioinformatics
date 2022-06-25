with open("/Users/mujeebqadiri/Desktop/geneset/rosalind_gc.txt", 'r') as FASTA_ID:
    data = FASTA_ID.read()
    FASTA_LIST = data.replace('\n', '').split(">Rosalind_")

def findgc(i):
    seq = str(i)
    g = seq.count('G')
    c = seq.count('C')
    a = seq.count('A')
    t = seq.count('T')
    return ((g+c)/(g+c+a+t))

FASTA_LIST.pop(0)
initialgc = 0

for i in FASTA_LIST:
    finalgc = findgc(i)
    if finalgc > initialgc:
        initialgc = finalgc
        sequence = i[0:4]

print(initialgc*100)
print('Rosalind_' + sequence)
