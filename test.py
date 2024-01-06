from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

for child in bs.find('table', {'id':'gift'}).children:
    print(child)



from IPython.display import Image
Image(filename = 'D:\\file\\PythonFiles\\python_spyder_guid\\png\\re1.png', width=320, height=240)
Image(filename = 'D:\\file\\PythonFiles\\python_spyder_guid\\png\\re2.png', width=320, height=240)