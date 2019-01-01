from bs4 import BeautifulSoup

# requests
import requests

bill_list = list()

# 1페이지 -> 100페이지 반복작업 시키기
for i in range(1, 100):
    response = requests.get('http://watch.peoplepower21.org/index.php?mid=Euian&show=1&page={}&title=&rec_num=15&lname=&sangim=&bill_result=#'.format(i))


    html = response.text


    #bs4 + parser는 lxml---> html코드의 body가져오기
    soup = BeautifulSoup(html,"lxml")
    body = soup.body

    # 게시판 첫글 + 해당코드를 확인하기

    # body.find(속성=)함수를 이용해서 <div id=>에 접근하기
    # 찾을 때는 div태그와 무관하게 id속성으로 바로 찾아온다.
    div_ea_list = body.find(id = "ea_list")


    # div id = ea_list 하위구조에서 필요한 것은
    # 해당 table -> tbody -> tr -> td 일 것이다.
    table = div_ea_list.table
    tbody = table.tbody


    # tbody에서는 여러개의 tr을 가지고 있기 때문에,
    # for문을 이용해서 tr들을 모두 찾아 lines에 다 넣어준다.
    lines = tbody.find_all('tr')




    for line in lines:
        td_list = line.find_all('td')
        # 리스트에  리스트형식을 append해주기
        bill_list.append(
            [ td_list[0].text, td_list[1].text, td_list[2].text, td_list[4].text]
        )

    # 2차원 리스트를 이쁘게 보려면, for문으로 print해주자.
    # for bill in bill_list:
    #     print(bill)



    # table -> thead-> th에서 머리말 제목(th들) 가져오기
    thead = table.thead
    # print(thead)
    th_list = thead.find_all('th')
    # print(th_list[0].text)
    # print(th_list[1].text)
    # print(th_list[2].text)
    # print(th_list[4].text)


import pandas as pd
df = pd.DataFrame(bill_list, columns= [th_list[0].text,
                                       th_list[1].text,
                                       th_list[2].text,
                                       th_list[4].text])
df.to_excel('bill.xlsx',  index=False )