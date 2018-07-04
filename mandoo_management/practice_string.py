message = '내 이름은 조재성이고, 파이썬을 좋아합니다.'

#split -> list로 반환
word_list = message.split(' ')
print( type(word_list) )

for w in word_list:
    print(w)


#join
joined_string = ' '.join(word_list)
print(joined_string)

#replace
print('----replace----')
print(message.replace('이','2'))

#upper, lower
print('----upper & lower ----')
eng_string = 'My name is Jaeseong. I\'am happy'
print(eng_string.upper())
print(eng_string.lower())

#starstwith
print('---- startswith ----')
print(eng_string.startswith('I\'am'))
print(eng_string.startswith('My name'))
print('---- endswith ----')
print(eng_string.endswith('happy'))