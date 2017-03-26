def split_sentence(sentence):
	alist=[]
	asentence=''
	bsentence=''
	alist=sentence.split()
	asentence=''.join(alist)
	bsentence=''.join(sentence).split()
	#alist=sentence.split('',1)
	return alist, asentence, bsentence
	

my_sentence='Boston is a nice city'

print split_sentence(my_sentence)