from urllib.request import urlopen
from datetime import date

def test_display():
    link = "http://127.0.0.1:5000/"
    f = urlopen(link)
    myfile = f.read()
    content = myfile.decode("utf-8")
    current_date = str(date.today())
    assert current_date in content
