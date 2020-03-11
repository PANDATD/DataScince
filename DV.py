import matplotlib.pyplot as plt
print('*'*50)
print('which graph you want:')
print('1: hist-plot ' )
print('2: bar-plot ' )
print('3: pie-plot ' )
print('*'*50)
yaxis = []
ch=int(input('>>> Enter choice'))
if ch==1:
	tit = input('>>> enter title of plot hear :')
	plt.title(tit)
	ylab = input('>>> enter y label name :')
	plt.ylabel(ylab)
	xlab = input('>>> enter x label name :')
	plt.xlabel(xlab)
	n = int(input('enter the no you want to add the graph elements :'))	
	for i in range(0,n):
		ele = int(input('>>>'))
		yaxis.append(ele)
		
	plt.hist(yaxis)

elif ch==2:
	tit = input('>>> enter title of plot hear :')
	plt.title(tit)
	ylab = input('>>> enter y label name :')
	plt.ylabel(ylab)
	xlab = input('>>> enter x label name :')
	plt.xlabel(xlab)
	n = int(input('enter the no you want to add the graph elements :'))	
	for i in range(0,n):
		ele = int(input('>>>'))
		yaxis.append(ele)
		
	plt.plot(yaxis)


elif ch==3:
	tit = input('>>> enter title of plot hear :')
	plt.title(tit)
	ylab = input('>>> enter y label name :')
	plt.ylabel(ylab)
	xlab = input('>>> enter x label name :')
	plt.xlabel(xlab)
	n = int(input('enter the no you want to add the graph elements :'))	
	for i in range(0,n):
		ele = int(input('>>>'))
		yaxis.append(ele)
		
	plt.pie(yaxis)

else :
	print('Something Went Wrong')

plt.show()
