from bs4 import BeautifulSoup
import requests
import sqlite3

#Open connection to db
conn = sqlite3.connect('LiquorAppTest.db')
c = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

#For White Rum
for x in range(1,5):
    url = 'https://www.theliquorbarn.com/white-rum/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "White Rum", str(brand)))
        conn.commit()

#For Dark Rum
for x in range(1,13):
    url = 'https://www.theliquorbarn.com/dark-rum/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Dark Rum", str(brand)))
        conn.commit()

#For Spiced Rum
for x in range(1,4):
    url = 'https://www.theliquorbarn.com/spiced-rum/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Spiced Rum", str(brand)))
        conn.commit()

#MUST ADD FLAVOURED OR OTHER RUM

#For Gin
for x in range(1,13):
    url = 'https://www.theliquorbarn.com/gin/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1= soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Gin", str(brand)))
        conn.commit()

#For Blanco Tequila
for x in range(1,12):
    url = 'https://www.theliquorbarn.com/blanco/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Tequila", str(brand)))
        conn.commit()

#For Reposado Tequila
for x in range(1,11):
    url = 'https://www.theliquorbarn.com/reposado/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Tequila", str(brand)))
        conn.commit()


#For Anejo Tequila
for x in range(1,11):
    url = 'https://www.theliquorbarn.com/anejo/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Tequila", str(brand)))
        conn.commit()

#For Mezcal Tequila
for x in range(1,3):
    url = 'https://www.theliquorbarn.com/mezcal/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Tequila", str(brand)))
        conn.commit()


#For Amareto
for x in range(1,2):
    url = 'https://www.theliquorbarn.com/amaretto/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Amareto", str(brand)))
        conn.commit()


#For Irish Cream
for x in range(1,3):
    url = 'https://www.theliquorbarn.com/irish-cream/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Irish Cream", str(brand)))
        conn.commit()

#For Aperitifs
for x in range(1,4):
    url = 'https://www.theliquorbarn.com/aperitifs/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), "Aperitif", str(brand)))
        conn.commit()

#For Vodka
for x in range(1,84):
    url = 'https://www.theliquorbarn.com/vodka/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), str(variety), str(brand)))
        conn.commit()

#For Whiskeys
for x in range(1, 129):
    url = 'https://www.theliquorbarn.com/whisky/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)

        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None


        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), str(variety), str(brand)))
        conn.commit()

#For other Liqeurs
for x in range(1,52):
    url = 'https://www.theliquorbarn.com/other-liqueurs/?sort=featured&page=' + str(x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links1 = soup.find_all('h3')
    for x in links1:
        if "footer" in str(x):
            continue
        links = x.find('a')['href']
        page1 = requests.get (links, headers = headers)   
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        name = soup1.find('h1', class_='single-product-title').text
        name = str(name.strip())
        print(name)
        counter = 0
        checkUPC = soup1.find_all('span', class_='single-product-meta-item-label')
        for x in checkUPC:
            if "Brand" in (str(x.text)):
                brand = soup1.find('div', class_='single-product-brand').text
                brand = brand.strip().replace('Brand:\n','')
                print (brand)
                counter -= 1
            if "UPC:" in (str(x.text)):
                upc = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print (upc)
            if "Varietal" in (str(x.text)):
                variety = soup1.find_all('span', class_='single-product-meta-item-value')[counter].text
                print(variety)
            counter += 1

        #Pull brand
        brand1 = soup1.find('div', class_='single-product-brand')
        if not brand1:
            brand = None

        #Inserts into table
        c.execute("INSERT INTO Ingredient VALUES (?, ?, ?, ?)", (int(upc), str(name), str(variety), str(brand)))
        conn.commit()
c.close()
print("!!!!!!!!!!!!!ALL DONE!!!!!!!!!!!!!!")