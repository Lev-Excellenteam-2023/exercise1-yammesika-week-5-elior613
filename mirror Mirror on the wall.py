

encryption_key = {
    'T': '1', 'F': '6', 'W': 'c', 'Y': 'h', 'B': 'k',
    'P': '~', 'H': 'q', 'S': 's', 'E': 'w', 'Q': '@',
    'U': '$', 'M': 'i', 'I': 'l', 'N': 'o', 'J': 'y',
    'Z': 'z', 'G': '!', 'L': '#', 'A': '&', 'O': '+',
    'D': ',', 'R': '-', 'C': ':', 'V': '?', 'X': '^', 
    'K': '|',
}
decryption_key={}
for i in encryption_key:
    decryption_key[encryption_key[i]]=i;

SONG = """
l1's ih #l6w
l1's o+c +- ow?w-
l &lo'1 !+oo& #l?w 6+-w?w-
l y$s1 c&o1 1+ #l?w cql#w l'i &#l?w
(l1's ih #l6w)
ih qw&-1 ls #l|w &o +~wo ql!qc&h
#l|w 6-&o|lw s&l,
l ,l, l1 ih c&h
l y$s1 c&o1 1+ #l?w cql#w l'i &#l?w
l1's ih #l6w
"""

tmp=''
for i in SONG:
    tmp+=decryption_key.get(i,i);
SONG=tmp;
print(SONG)