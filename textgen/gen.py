data=open("warpeace_input.txt",'r').read()
chars=list(set(data))
VOCAB_SIZE=len(chars)

ix_to_char={ix:xhar for ix, char in enumerate(chars)}
char_to_ix={char:ix for ix,char in enumerate(chars)}

