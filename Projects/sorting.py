def bubble():
	n=int(input("enter the number of element: "))
	arr=[]
	for i in range(n):
		arr.append(int(input("enter element: ")))
	print(arr)
	for i in range(n-1):
		for j in range(n-1):
			if arr[j]>arr[j+1]:
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp
	print(arr)
#bubble()
def selection():
	n=int(input("enter the number of element: "))
	arr=[]
	for i in range(n):
		arr.append(int(input("enter element: ")))
	print(arr)
	for i in range(n):
		for j in range(n-1):
			if arr[i]<arr[j]:
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp
	print(arr)
a=int(input("enter type of sorting\n  enter 1 for bubble\n  and enter 2 for selection:"))
if a==1:
	bubble()
elif a==2:
	selection()
else:
	print("enter correct choice")
