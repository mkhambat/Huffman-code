import collections
import string
import re
import io
import Queue

class Node(object):
    def __init__(self,char):
    	self.char=char
        self.left=None
        self.right=None
        # self.freq=freq
       


allow=list(string.ascii_lowercase)
spl_char = [" ",".",",","!","?","'"]
allow = allow + spl_char
#print allow

#with open("plain_text.txt") as file :
f =io.open("plain_text.txt",mode="r", encoding="utf-8") 
text=f.read()
text=text.strip()
text=text.lower()
#print(len(text))

filtered_text = re.sub(r"[^a-z\+.,!? ']","",text)
dict_freq = collections.Counter(filtered_text)
# print ((dict_freq.keys()[9]))

def huffman(freq):
	no_of_char=len(dict_freq)-1
	q=Queue.PriorityQueue()
	l=[]
	for k in dict_freq.keys():
		l.append(dict_freq[k])
		l.append(Node(k))
		t=tuple(l)
		l=[]
		q.put(t)
		 
	# for i in range(len(dict_freq)):
	# 	print q.get()
	for i in range(no_of_char-1):
		z=Node(None)
		x=q.get()
		y=q.get()
		z.left=x
		z.right=y
		q.put(z)
	return q.get()


huffman(dict_freq)
