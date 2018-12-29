from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>조재성의 HTML 웹스크래핑 연습</title>
    <link rel="stylesheet" href="https://bootswatch.com/4/darkly/bootstrap.css" media="screen">
    <link rel="stylesheet" href="https://bootswatch.com/_assets/css/custom.min.css">

</head>
<body>
<h1> (h1) Web Scrapping practice </h1>
<h2> (h2) 한글 웹 스크래핑 </h2>
<p> (p)안녕하세요? 웹 스크래핑 연습용 페이지 입니다.</p>

<table class="table table-striped">
    <thead>
        <tr>
            <th> (th)는 한칸인데 굵은글씨</th>
            <th> 다음칸 목록</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>조재성 : (td)는 (table-tr한줄)안에 한칸을 의미합니다</td>
            <td> | 다음칸1</td>
        </tr>
        <tr>
            <td>김석영 : (td)는 (table-tr한줄)안에 한칸을 의미하네요. </td>
            <td> | 다음칸2</td>
        </tr>
    </tbody>

</table>

</body>
</html>
'''


# 서버에서 받은 html코드를 이용하여 BeautifulSoup객체를 만드는데,
# 받아올 때 필요한 양식이 "lxml"이며, 인스톨이 필요하다

soup = BeautifulSoup(html, "lxml")
body = soup.body
h1 = body.h1
h1_text = body.h1.text

table = body.table

tr_list = table.tbody.find_all('tr')

for tr in tr_list:
    print(tr.find_all('td')[0].text)


