# finding max in an array.
# left and right side of element of the peak will be smaller.
import time
start_time = time.time()
b = [ 21, 22, 23, 24, 22, 21, 20, 19, 17, 15, 14]

def fun(a):
	if len(a) > 2:
		
		if a[round(len(a)/2)] < a[round(len(a)/2)-1]:
			b = a[0:round(len(a)/2)-1]
			print('b is',b)
			a = fun(b)
		elif a[round(len(a)/2)] < a[round((len(a)/2))+1]:
			b = a[round(len(a)/2)+1:len(a)]
			a = fun(b)
		else:
			a = a[round(len(a)/2)]

	elif len(a)==2:
		return a[0] if a[0]>a[1] else a[1]

	else:
		return a

	return a

print(fun(b))
print(b[0])
print(time.time()-start_time)