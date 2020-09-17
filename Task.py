# code for how to generate Password.
# Input the values
F_name = input('Enter your first name :')
L_name = input('Enter the last name :')
P = input('enter the PIN-code :')
N = int(input('enter the Number :'))
smaller=None
greater=None

# comparing the lengths 

	if len(F_name)>len(L_name) :
		greater = F_name
		smaller = L_name
	elif len(F_name)<len(L_name) :
		greater = L_name
		smaller = F_name 
	else :
		p = F_name.sorted()
		q = L_name.sorted()
		if p < q :
			p = smaller
			q = greater
		else : 
			p = greater
			q = smaller
		print(f'smaller one is :{smaller}  greater one is:{greater}')

# generating user id

	ltr = P[N-1]
	T = list(P)
	T.reverse()
	rtl=T[N-1]
id = f'{smaller[-1]}{greater}{ltr}{rtl}'
print(id.swapcase())

        



    

