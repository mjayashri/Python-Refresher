from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html>
<body>
<h1>This is title</h1>
<p class="subtitle">This is paragraph with class name</p>
<p>This is paragraph</p>
<ul>
    <li>Jayashri</li>
    <li>Charlie</li>
    <li>Jose</li>
    <li>Tiger</li>
</ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('h1').string)


def find_listitems():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)


find_listitems()


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [e for e in paragraphs if 'subtitle' not in e.attrs.get('class', [])]
    print(other_paragraph[0])


find_subtitle()
