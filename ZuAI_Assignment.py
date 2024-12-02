from bs4 import BeautifulSoup
import requests

url = "https://nailib.com/ia-sample/ib-math-ai-sl/64a795bb88bfdb4b9172af7b"
response = requests.get(url)

content = response.text

doc=BeautifulSoup(content,'html.parser')
t = doc.find(class_="file_sample__body__container__middle__cover__heading__VG9Sj")
title = t.text.strip()
print(title)

s = doc.find(class_="file_sample__body__container__middle__cover__heading--small__gzm_v")
subject = s.text.strip()[0:17]
print(subject)

time = doc.find_all(class_="file_sample__body__container__middle__cover__stat__item__text__6umeQ")
time_estimate = time[1].text.strip()
print(time_estimate)

w = doc.find_all("strong")
word_count = (w[3].find_parent("div").text)[12:].strip()
print(word_count)

content = doc.find_all("section",class_="file_sample__body__container__middle__section__item__NMSJs")
content_dict={}
heading=""
subheading=""
for c in content:
    try:
        if(c.find(class_="heading_h2__J3Jfh")):
            heading = c.find(class_="heading_h2__J3Jfh").text
        else:
            heading = c.find(class_="heading_h3__RVe48").text
    except:
        continue
    data = c.find(class_="file_sample__body__container__middle__section__item__body__htGIX").text
    content_dict[heading]=data
print(content_dict)

figure = doc.find_all("figure",class_="file_sample__body__container__middle__section__item__NMSJs")
fig_dict={}
for i in figure:
    try:
        f = i.find("img")["src"]
        fc = i.find("figcaption").text
    except:
        continue
    fig_dict[fc]=f
print(fig_dict)

if(doc.find_all("table")):
    tables = doc.find_all("table")
    for table in tables:
        data = []
        headers = []
        for i, row in enumerate(table.find_all('tr')):
            cells = row.find_all(['th', 'td'])
            if i == 0:
                headers = [cell.text.strip() for cell in cells]
            else:
                row_data = [cell.text.strip() for cell in cells]
                data.append(dict(zip(headers, row_data)))
        print(data)