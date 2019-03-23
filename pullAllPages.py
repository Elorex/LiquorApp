from bs4 import BeautifulSoup
import requests
import re
import sqlite3
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
f=open("testurls.txt", "a+")
counter = 0

#Open connection to db
conn = sqlite3.connect('LiquorAppTest.db')
c = conn.cursor()

for x in range(1,216):
    url = 'https://tipsybartender.com/drinks/page/' + str(x) + '/'
    page = requests.get (url, headers = headers)    
    soup = BeautifulSoup(page.content, 'html.parser')
    for a in (soup.find_all('a', href=re.compile("https://tipsybartender.com/recipe/"))):
        counter = counter + 1
        if counter%2 == 0:
            continue
        link_text= a['href']
        if "pinterest" in link_text:
            continue
        if "twitter" in link_text:
            continue
        if "facebook" in link_text:
            continue
        indPage = requests.get (link_text, headers = headers)
        indSoup = BeautifulSoup(indPage.content, 'html.parser')

        # Grabs nice list of proportions of ingredients, and prep
        description = indSoup.find_all('div', class_ = 'rich-text')
        for x in description:
            proportions = x.find_all('p')[1].text
            preparations = x.find_all('p')[2].text

            print (preparations)

        # Grab Drink Name
        drinkName = indSoup.find('h1', itemprop='name').text
        print(drinkName)

        #Removes drink name from proportions
        drinkNameString = str(drinkName).upper() + " "
        proportions= proportions.replace(str(drinkNameString), '')
        print (proportions)

        #Inserts into table
        c.execute("INSERT INTO Recipe VALUES (?, ?, ?)", (str(drinkName), str(preparations), str(proportions)))
        conn.commit()

        #Grab list of alcohols in drink
        alcohols = indSoup.find_all('a', itemprop = 'recipeIngredient')
        for x in alcohols:
            if str(x).find("alcohol") != -1:
                print(x.text)
                ingredient = x.text
                c.execute("INSERT INTO RecipeIngredient VALUES (?, ?)", (str(drinkName), str(ingredient)))

print("done!!!!")