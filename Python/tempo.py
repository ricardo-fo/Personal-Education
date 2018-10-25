#https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup
import requests 
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W8vlPu-YXIV")
soup = BeautifulSoup(page.content, 'html5lib')
seven_day = soup.find(id = "seven-day-forecast")

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
#print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#print(short_descs)
print(temps)
#print(descs)

weather = pd.DataFrame({
		"period": periods,
		"short_desc": short_descs,
		"temp": temps,
		#"desc": descs
	})
print(weather)

temp_nums = weather["temp"].str.extract("(?P<temp_nums>\d+)", expand = False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)
print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)
'''
forecast_items = seven_day.find_all(class_ = "tombstone-container")
tonight = forecast_items[0]

period = tonight.find(class_ = "period-name").get_text()
short_desc = tonight.find(class_ = "short-desc").get_text()
temp = tonight.find(class_ = "temp").get_text()
img = tonight.find("img")
desc = img['title']

print(period)
print(short_desc)
print(temp)
#print(desc)
'''
