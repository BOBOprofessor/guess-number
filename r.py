import random 
r = random.randint(1, 100)
i = 6
while True :
	num = input('猜猜數字多少?')
	num = int(num)
	if num == r :
		print('你答對了!')
		break
	elif num != r :
		i = i - 1
		if i == 0 :
			print('你失敗了')
			break

		elif num > r :
			print ('猜小一點試試看你還剩', i, '次機會')
		
		elif num < r :
			print ('猜大一點試試看你還剩', i, '次機會')
				
			
			


	
		
		
		
	
		
		
		


