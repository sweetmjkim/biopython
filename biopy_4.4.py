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

tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
print(tatabox_seq.upper())
# TATAAAGGCAATATGCAGTAG         대문자로 변환
print(tatabox_seq.lower())
# tataaaggcaatatgcagtag         소문자로 변환

dna = Seq("ATGCAGTAG")          # dna 정보
mrna = dna.transcribe()         # mrna로 전사
ptn = dna.translate()           # 번역      ptn : protein
print(mrna)
# AUGCAGUAG
print(ptn)
# MQ*

mRNA = Seq("AUGAACUAAGUUUAGAAU")
ptn = mRNA.translate()
print(ptn)
# MN*V*N

mRNA = Seq("AUGAACUAAGUUUAGAAU")
ptn = mRNA.translate(to_stop=True)
print(ptn)
# MN            # 첫번째 종결코돈에서 끝나게 하기

mrna = Seq("AUGAACUAAGUUUAGAAU")
ptn = mrna.translate()
print(ptn)
# MN*V*N
for seq in ptn.split("*"):          # split 메서드로 종결코든 문자(*)를 기준으로 나눈다.
    print(seq)
# MN
# V
# N

seq = Seq("TATAAAGGCAATATGCAGTAG")
comp_dic = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
comp_seq = ''
for s in seq:
    comp_seq += comp_dic[s]
revcomp_seq = comp_seq[::-1]
print(comp_seq)
# ATATTTCCGTTATACGTCATC
print(revcomp_seq)
# CTACTGCATATTGCCTTTATA

comp_seq = seq.complement()
rev_comp_seq = seq.reverse_complement()
print(comp_seq)
print(rev_comp_seq)