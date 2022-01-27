import random
import time
bai = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
chat_bai = ('BÍCH','CHUỒN','RÔ','CƠ')
name_player = input('nhập tên của bạn:')
print('Chào mừng người chơi '+ name_player,"!")

#chơi với mấy máy.

may = int(input('Bạn muốn chơi với mấy máy( tối đa 3 máy): '))
if may == 1:
    may1 = input('Nhập tên máy 1: ')
elif may == 2:
    may1 = input('Nhập tên cho máy 1: ')
    may2 = input('Nhập tên cho máy 2: ')
elif may == 3:
    may1 = input('Nhập tên máy 1: ')
    may2 = input('Nhập tên máy 2: ')
    may3 = input('Nhập tên máy 3: ')
else:
    print('Nhập sai!!!')

#hàm chia bài cho người chơi
def chiabai_nguoichoi():
    bai_nguoichoi1 = random.choices(bai)
    chatbai_nguoichoi1= random.choices(chat_bai)
    bai_nguoichoi2 = random.choices(bai)
    chatbai_nguoichoi2 = random.choices(chat_bai)
    print('Bài của người chơi:'+ name_player)
    print(str(bai_nguoichoi1) + str(chatbai_nguoichoi1)+ str(bai_nguoichoi2) + str(chatbai_nguoichoi2))

#hàm chia bài cho máy
def chiabai_may1():
    bai_may1_la1 = random.choices(bai)
    chatbai_may1_la1 = random.choices(chat_bai)
    bai_may1_la2 = random.choices(bai)
    chatbai_may1_la2 = random.choices(chat_bai)
    print('Bài máy 1:?????????')
def chiabai_may2():
    bai_may2_la1 = random.choices(bai)
    chatbai_may2_la1 = random.choices(chat_bai)
    bai_may2_la2 = random.choices(bai)
    chatbai_may2_la2 = random.choices(chat_bai)
    print('Bài máy 2:?????????')
def chiabai_may3():
    bai_may3_la1 = random.choices(bai)
    chatbai_may3_la1 = random.choices(chat_bai)
    bai_may3_la2 = random.choices(bai)
    chatbai_may3_la2 = random.choices(chat_bai)
    print('Bài máy 3:?????????')

#chia bài cho nhà cái
def chiabai_nhacai():
    bai_cai_la1 = random.choices(bai)
    chatbai_cai_la1 = random.choices(chat_bai)
    bai_cai_la2 = random.choices(bai)
    chatbai_cai_la2 = random.choices(chat_bai)
    print('Bài nhà cái:????????')

#chia bài
def chiabai1():
    chiabai_nguoichoi()
    chiabai_may1()
    chiabai_nhacai()

def chiabai2():
    chiabai_nguoichoi()
    chiabai_may1()
    chiabai_may2()
    chiabai_nhacai()

def chiabai3():
    chiabai_nguoichoi()
    chiabai_may1()
    chiabai_may2()
    chiabai_may3()
    chiabai_nhacai()
        
tien_nguoichoi = int(input('Nhập sô tiền bạn muốn có trong tài khoản:'))

while True:
    tien_cuoc = int(input('nhập số tiền cược:'))
    if tien_cuoc > tien_nguoichoi:
        print("Tiền cược ko thể lớn hơn số tiền bạn có!")
    else:
        tien_cuoc <= tien_nguoichoi
        print('bạn cược:' + str(tien_cuoc))
    print('bắt đầu chia bài!!')
    time.sleep(3)
    print('.................................')
    if may == 1:
       chiabai1()
    elif may == 2:
        chiabai2()
    elif may == 3:
        chiabai3()
    


    
