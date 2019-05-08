1 st question
a=input("enter word\n")
b=len(a)
int(b)
c=0
for i in range(0,b-1):
	if(a[i]!=a[b-i-1]):
		c=1
		break
if(c==0):
    print("Word is palindrom")
else:
	print("Word is not palindrom")

