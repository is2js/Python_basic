from bs4 import BeautifulSoup

# requests
import requests
# 셀레니움 패키지의 webdriver 클래스 이용
from selenium import webdriver
# 셀레니움 webdriver패키지 안에 특정속성출현을 기다려줄 수 있는 클래스 3가지
from selenium.webdriver.support.ui import WebDriverWait # 1)
from selenium.webdriver.support import expected_conditions as EC # 2)
from selenium.webdriver.common.by import By #3)


# web driver 중 크롬드라이버 이용
browser = webdriver.Chrome('chromedriver')

bill_list = list()

# 1페이지 -> 100페이지 반복작업 시키기
# TODO 크롤링을 위해서 (1, 2)로 수정 나중에 고치기
for i in range(1, 10):
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


        # TODO 게시판의 각 줄을 의미하는 line안의   각 칸<td> 중 제목칸인 td_list[1]를 보자.
        # TODO .text제외시키고  제목칸 <td>태그 안에는 링크 주소태그 <a> 태그가 있다.


        href = "http://watch.peoplepower21.org" + td_list[1].a.get('href')



        browser.get(href) # 1. response 받기 - repsonse = requests.get(url)에 대응

        # Selenium은 기본적으로 웹 자원들이 모두 로드될때까지 기다려주지만, 암묵적으로 모든 자원이 로드될때 까지 기다리게 하는 시간을 직접 implicitly_wait을 통해 지정할 수 있다
        browser.implicitly_wait(3)  # 3. 필요한 html코드를 받기 전에 암묵적으로 기다려준 뒤, html코드 받기
        # 3가지클래스를 이용해 특정속성출현을 확실히 기다려줌
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.ID, 'collapseTwo')
            )
        )


        html = browser.page_source # 2. url에서 html코드 가져오기 - html = response.text에 대응
        soup = BeautifulSoup(html, "lxml")
        body = soup.body

        proposer = body.find(id='collapseTwo').text.replace(' ','') # 7. 빈칸이 너무 많다. replace(' ','')



        # 4. 리스트에  리스트형식을 append해주기 -> 타고간 페이지의 정보를 받은 뒷자리로 코드 이동
        bill_list.append(
            # 5. 발의자목록 text도 추가로 append -> # 6.로 가서 칼럼명도 추가
            [ td_list[0].text, td_list[1].text, td_list[2].text, td_list[4].text, proposer]
        )







    # 2차원 리스트를 이쁘게 보려면, for문으로 print해주자.
    # for bill in bill_list:
    #     print(bill)





    # table -> thead-> th에서 머리말 제목(th들) 가져오기
    thead = table.thead
    # print(thead)
    th_list = thead.find_all('th')


import pandas as pd
df = pd.DataFrame(bill_list, columns= [th_list[0].text,
                                       th_list[1].text,
                                       th_list[2].text,
                                       th_list[4].text, # 6. 추가된 정보-> 발의자 칼럼 추가
                                       "발의자"])
df.to_excel('bill.xlsx',  index=False )

browser.quit()