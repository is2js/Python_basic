def gugudan(x):
    for i in range(1,10):
        print( '{} * {} = {}'.format(x, i, x * i) )

a = input('구구단 몇단을 하고싶으세요? : ')

#input으로 받은 문자열 숫자를 --> 정수형으로 변형
int_a = int(a)

gugudan( int_a )


