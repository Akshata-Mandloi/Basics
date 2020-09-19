# creating a class
class Difft:
# 	method m1 for taking integers in first array
	def m1(self): 
		for i in range(NoOfEle):
			i=int(input('enter elements'))
			list1.append(i)
			print(list1)
			
# 	method m2 for taking integers in second array
	def m2(self):
		for j in range(NoOfEle):
			j=int(input('enter elements'))
			list2.append(j)
			print(list2)
			
# 	chomparing the array is same or not
	def sorting(self):
		list1.sort()
		list2.sort()
		if list1==list2:
			print("All emements are same")
		else:
			print("not all elements are same")


# calling the method via object created for class difft

list1=[]
list2=[]
NoOfEle=int(input("enter the no of elements you want to enter"))
d=Difft()
d.m1()
d.m2()
d.sorting()




	
