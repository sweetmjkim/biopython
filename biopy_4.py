from Bio.Seq import Seq
tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
print(tatabox_seq)
# tataaaggcAATATGCAGTAG
print(type(tatabox_seq))
# <class 'Bio.Seq.Seq'>
print(dir(Seq))
print(help(Seq))