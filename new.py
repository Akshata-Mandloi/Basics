# cresting a class
class Difft:

	def m1(self): 
		for i in range(NoOfEle):
			i=int(input('enter elements'))
			list1.append(i)
			print(list1)
	
	def m2(self):
		for j in range(NoOfEle):
			j=int(input('enter elements'))
			list2.append(j)
			print(list2)
	
	def sorting(self):
		list1.sort()
		list2.sort()
		if list1==list2:
			print("equal")
		else:
			print("not equal")




list1=[]
list2=[]
NoOfEle=int(input("enter the no of elements you want to enter"))
d=Difft()
d.m1()
d.m2()
d.sorting()




	