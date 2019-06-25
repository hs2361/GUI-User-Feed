from bs4 import BeautifulSoup as bs
import urllib,re,random
page = random.randint(1,34)
j = f"http://www.laughfactory.com/jokes/clean-jokes/{page}"
joke_soup = bs(urllib.request.urlopen(j))
joke = joke_soup.select(".joke-text p")
print(re.split('"joke_[0-9][0-9][0-9][0-9][0-9]">\r\n',str(random.choice(joke)))[1].replace("</p>",'').replace("<br/>",'\n').strip())