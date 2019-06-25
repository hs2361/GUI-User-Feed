from bs4 import BeautifulSoup as bs
import urllib
q = "http://wisdomquotes.com/quote-of-the-day"
quote_soup = bs(urllib.request.urlopen(q),features="lxml")
quote = quote_soup.select('.quotescollection-quote p')
print("Quote of the Day:")
print(str(quote[0]).replace('<p>','').replace('</p>','') + '\n')
w = "https://www.dictionary.com/e/word-of-the-day"
word_soup = bs(urllib.request.urlopen(w),features="lxml")
word = word_soup.select(".wotd-item__definition h1")
definition = word_soup.select(".wotd-item__definition__text")
print("Word of the Day:")
print(str(word[0]).replace("<h1>",'').replace("</h1>",''))
print(str(definition[0]).replace('<div class="wotd-item__definition__text">','').replace("</div>",''))