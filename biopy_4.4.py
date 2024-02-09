from Bio.Seq import Seq
exon_seq = Seq("ATGCAGTAG")

# A 갯수 구하기
count_a = exon_seq.count("A")
print(count_a)
# 3

# GC_contents 구하는 공식
G_count = exon_seq.count("G")
C_count = exon_seq.count("C")
GC_contents = (G_count + C_count)/len(exon_seq)*100
print(GC_contents)
# 44.44%