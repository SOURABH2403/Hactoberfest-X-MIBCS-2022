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
bubble()
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
