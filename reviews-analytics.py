import time
import os

def read_file(filename):
	data = []
	reviews_average = 0
	with open (filename, 'r', encoding='utf-8') as f:
		for line in f:
			data.append(line)
			reviews_average += len(line)
			if len(data) % 10000 == 0:
				print(len(data))

	print('字典共有', len(data),'筆資料')
	print('每筆留言均長', reviews_average/len(data))
	return data


def add_to_dictionary(data):
	#將單字加入到字典
	wc = {} # word_count
	numbers_and_symbol = '1234567890!@#$%^&*()_+~`-=[]}{|:;/............?><,1234567890!@#$%^&*()_+~`-=[]}{|:;/............?><,1234567890!@#$%^&*()_+~`-=[]}{|:;/............?><,1234567890!@#$%^&*()_+~`-=[]}{|:;/............?><,'

	start_time = time.time()
	for d in data:
		#將每筆留言以空白為分隔標準進行分割並存成清單
		words = d.split(' ')
		#再將清單中的每個單字逐筆取出
		for word in words:
			

			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	for word in wc:
		for n_a_s in numbers_and_symbol:
			if n_a_s in word:
				word = word.replace(n_a_s, ' ')

	end_time = time.time()
	#建立一個字典的清單
	wc_list = [wc]
	print('executed payed ', end_time - start_time, ' seconds.')
	return wc


def serch_specify_word(wc):
	#建立查詢單字的功能
	while True:
		want_serch = input('What word you want to serch: ')
		if want_serch == 'q' or want_serch == 'Q':
			break
		elif want_serch in wc:
			print('We find out the ',want_serch,'appear: ',wc[want_serch],'times.')
		else:
			print('This word has not exist')
#建立可以顯示某次數以上或以下的單字的功能
# frame the mode [more than] 1
def serch_mode_than(wc):	
	while True:
		print('entered the mode 1')
		want_serch = input('What counts for word you want serch: ')
		if want_serch == 'q' or want_serch == 'Q':
			break
		for word in wc:
			if wc[word] > int(want_serch):
				print(word)

#frame the mode [less than] 2
def serch_mode_less(wc):
	while True:
		print('entered the mode 2')
		want_serch = input('What counts for word you want serch: ')
		if want_serch == 'q' or want_serch == 'Q':
			break
		for word in wc:
			if wc[word] < int(want_serch):
				print(word)

#frame the mode [between] 3
def serch_mode_between(wc):
	while True:
		print('entered the mode 3')
		big = input('max: ')
		mini = input('mini: ')
		if big == 'q' or big == 'Q':
			break
		elif mini == 'q' or mini == 'Q':
			break
		for word in wc:
			if int(big) > wc[word] > int(mini):
				print(word)

#frame the mode to print most count's word top 10
def top10(wc):

	top = []
	top10_word = []
	top1 = 0
	top2 = 0
	top3 = 0
	top4 = 0
	top5 = 0
	top6 = 0
	top7 = 0
	top8 = 0
	top9 = 0
	top10 = 0
	top1_w = None
	top2_w = None
	top3_w = None
	top4_w = None
	top5_w = None
	top6_w = None
	top7_w = None
	top8_w = None
	top9_w = None
	top10_w = None

	for word in wc:
		
		if wc[word] > top1:
			top1 = wc[word]
			top1_w = word
		elif wc[word] > top2:
			top2 = wc[word]
			top2_w = word
		elif wc[word] > top3:
			top3 = wc[word]
			top3_w = word
		elif wc[word] > top4:
			top4 = wc[word]
			top4_w = word
		elif wc[word] > top5:
			top5 = wc[word]
			top5_w = word
		elif wc[word] > top6:
			top6 = wc[word]
			top6_w = word
		elif wc[word] > top7:
			top7 = wc[word]
			top7_w = word
		elif wc[word] > top8:
			top8 = wc[word]
			top8_w = word
		elif wc[word] > top9:
			top9 = wc[word]
			top9_w = word
		elif wc[word] > top10:
			top10 = wc[word]
			top10_w = word


	# for top10 in top:
	#	 print(top10)

	print('top1：', top1_w, '出現次數為：', top1)
	print('top2：', top2_w, '出現次數為：', top2)
	print('top3：', top3_w, '出現次數為：', top3)
	print('top3：', top4_w, '出現次數為：', top4)
	print('top3：', top5_w, '出現次數為：', top5)
	print('top3：', top6_w, '出現次數為：', top6)
	print('top3：', top7_w, '出現次數為：', top7)
	print('top3：', top8_w, '出現次數為：', top8)
	print('top3：', top9_w, '出現次數為：', top9)
	print('top3：', top10_w, '出現次數為：', top10)

	
	return top, top10_word

def main():
	while True:
		user_input = input('請輸入你要查詢的檔案名稱（含副檔名）：')
		if user_input == 'q' or user_input == 'Q':
			break
		else:
			if os.path.isfile(user_input):
				data = read_file(user_input)
				wc = add_to_dictionary(data)
				print('serch mode type')
				print('specify word = 0')
				print('more than = 1')
				print('less than = 2')
				print('between = 3')
				print('print top10 count\'s words = 4')
				print('exit = e')
				serch_mode = input('請選擇查詢模式：')
				if serch_mode == 'E' or serch_mode == 'e':
					break
				elif serch_mode == '0':
					serch_specify_word(wc)
				elif serch_mode == '1':
					serch_mode_than(wc)
				elif serch_mode == '2':
					serch_mode_less(wc)
				elif serch_mode == '3':
					serch_mode_between(wc)
				elif serch_mode == '4':
					top10(wc)
			else:
				print('抱歉，找不到資料＾Ｏ＾')
				break

main()