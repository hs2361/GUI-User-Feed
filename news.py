import requests,json
url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=a4cb616ced6244cd90bfb688f97bc758'
print('Which categories of news are you interested in receiving?')
print('1.Business')
print('2.Entertainment')
print('3.General')
print('4.Health')
print('5.Science')
print('6.Sports')
print('7.Technology')
print("News Feed powered by NewsAPI")
pref = input("Enter your preferences separated by commas")
print("\n")
cat_list = []
cat_dict = {1:'business',2:"entertainment",3:"general",4:"health",5:"science",6:"sports",7:"technology"}
data = []

for cat in pref.split(","):
    cat_list.append(cat_dict[int(cat)])

for i in cat_list:
    data.append(requests.get(url + f"&category={i}").json())


for i in data:
    c = 1
    while c < 4:
        print(i['articles'][c]['title'])
        if not i['articles'][c]['description'] is None:
            print(i['articles'][c]['description'] + '\n')
        else:
            print("\n")
        c += 1