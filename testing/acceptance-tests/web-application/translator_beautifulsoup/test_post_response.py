from bs4 import BeautifulSoup

html_content = '''
<!DOCTYPE HTML>
<html>
<head>
    <title>Translation Application</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    <h2>
        <p>Translate: cat into Katze</p>
    </h2>
    <p/>
    <a href="index.html"> back</a>
</body>
</html>
'''

soup = BeautifulSoup(html_content, 'html.parser')


def test_title():
    title = soup.title.string.strip()
    assert title == "Translation Application"


def test_translate_paragraph():
    paragraph = soup.find('p').string.strip()
    assert paragraph == "Translate: cat into Katze"


def test_back_link():
    link = soup.find('a')
    assert link.get('href') == 'index.html'
    assert link.text.strip() == 'back'
