print('study while')


my_money = 10000    # 만원있는데,
egg_price = 300     # 계란은 개당 300원
my_eggs = 0         # 지금 나는 계란이 0개


print('계란 보유 : {}, 남은 돈 : {}원' .format(my_eggs, my_money))

#계란을 살수 있는 한 다 살 것이므로, 조건문의 조건을 아래와 같이
while my_money > egg_price:
    # 계란을 하나 사는 식은  내돈 - 계란1개 가격  -> 그만큼 내 계란 + 1개 증가
    my_money = my_money - egg_price
    my_eggs = my_eggs + 1
    print('계란 보유 : {}, 남은 돈 : {}원' .format(my_eggs, my_money))



