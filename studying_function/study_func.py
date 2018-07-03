def add_something(x):
    return x + 8

a = add_something(6)







#인자가 2개인 함수
def plus_two_times(a, b):
    return a + b + b

c = plus_two_times(3, 4)
print(c)







#문자열을 인자로 받는 함수
def hello_someone(someone):
    return 'Hello ~ ' + someone

print(hello_someone('조재성'))