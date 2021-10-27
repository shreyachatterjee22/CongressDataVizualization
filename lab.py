#in this doc, I will be making graphs on how many times certain states are mentioned in DoJ press releases 
#for all Congresspeople, I will compare female to male percentages in a pie chart


#importing everything
from json import encoder
import matplotlib.pyplot as plt
import json
import os
import numpy as np


#here i am opening the json data file i downloaded
with open('C:/Users/Shreya/Documents/GitHub/week_07/2017-10-01.json', encoding='utf8') as f:
    text = f.read()
    tweets = json.loads(text)
print('len(tweets)= ',len(tweets))


#i begin by calculating the number of mentions for certain senators
number_california = 0
number_newyork = 0
number_texas = 0
number_dc = 0
number_florida = 0
for i in tweets:
    if 'california' in i['text'] or 'CA' in i['text'] or 'California' in i['text']: 
        number_california += 1
    if 'new york' in i['text'] or 'NY' in i['text'] or 'New York' in i['text']:
        number_newyork += 1
    if 'texas' in i['text'] or 'TX' in i['text'] or 'Texas' in i['text']:
        number_texas += 1
    if 'd.c.' in i['text'] or 'DC' in i['text'] or 'D.C.' in i['text']:
        number_dc += 1
    if 'florida' in i['text'] or 'FL' in i['text'] or 'Florida' in i['text']:
        number_florida += 1
print('number_california = ', number_california)
print('number_newyork = ', number_newyork)
print('number_texas = ', number_texas)
print('number_dc = ', number_dc)
print('number_florida = ', number_florida)


#the lines below organize and create the graph i want to make using the data found above
dict = {'California': number_california, 'New York': number_newyork, 'Texas': number_texas, 'D.C.': number_dc, 'Florida': number_florida}
print('dictionary = ', dict)

xs = sorted(dict.keys())
ys = [dict[key] for key in xs]

print('xs = ', xs)
print('ys = ', ys)

fig, ax = plt.subplots()
ax.bar(xs, ys)
ax.set_xlabel('State Name')
ax.set_ylabel('Number of Mentions')
ax.set_title('State Mentions in Congresspersons Tweets on 10/01/2017')
plt.show()



#opening the other files
with open('C:/Users/Shreya/Documents/GitHub/week_07/role_senate.json', encoding="utf8") as f1:
    text1 = f1.read()
    members_senate = json.loads(text1)
with open('C:/Users/Shreya/Documents/GitHub/week_07/role_hor.json', encoding='utf8') as f2:
    text2 = f2.read()
    members_hor = json.loads(text2)
print('len(members_senate)= ',len(members_senate['objects']))
print('len(members_hor)= ',len(members_hor['objects']))


#calculating number of males and females in each chamber
number_male_senate = 0
for i in members_senate['objects']:
    if i ['person']['gender'] == 'male':
        number_male_senate += 1
number_female_senate = 0
for i in members_senate['objects']:
    if i ['person']['gender'] == 'female':
        number_female_senate += 1
number_male_hor = 0
for i in members_hor['objects']:
    if i ['person']['gender'] == 'male':
        number_male_hor += 1
number_female_hor = 0
for i in members_hor['objects']:
    if i ['person']['gender'] == 'female':
        number_female_hor += 1
print('number_male_senate= ', number_male_senate)
print('number_male_hor= ', number_male_hor)
print('number_female_senate= ', number_female_senate)
print('number_female_hor= ', number_female_hor)


#concanating everything
number_female = number_female_senate + number_female_hor
number_male = number_male_senate + number_male_hor

print('number_female = ', number_female)
print('number_male = ', number_male)

number_congress = number_female + number_male
print('number_congress = ', number_congress)

#getting percentages
percent_female = (number_female/number_congress)*100
percent_male = (number_male/number_congress)*100

print('percent_female = ',percent_female)
print('percent_male = ',percent_male)

#making the pie chart
fig, ax = plt.subplots()
y = np.array([percent_female, percent_male])
mylabels = ["Female (27.14%)", "Male (72.86%)"]
plt.pie(y, labels = mylabels, startangle = 90)
ax.set_title('Percentage of Female vs.Male Congresspersons')
plt.show()
