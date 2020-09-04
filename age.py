drive = input('請問你有開過車嗎？ ')
if drive == '有' or drive == '沒有' :
	age = input('請輸入年齡：')
	age = int(age)
	if drive == '有' :		
		if age >= 18 :
			print('通過驗證')
		else :
			print('嘖嘖嘖，偷開車')
	elif drive == '沒有' :
		if age >= 18:
			print('你可以去考駕照喔')
		else :
			print('很好，再過幾年就可以考駕照了')
else :
	print('只能輸入有或沒有喔')
