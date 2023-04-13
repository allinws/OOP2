from bs4 import BeautifulSoup


html_doc = """
<html>
<head>
    <title>Min första websida</title>
</head>
<body>
    <h1>Välkommen till min websida</h1>
    <p>Detta är en demo-sida för BeautifulSoup.</p>
    <ul>
        <li><a href="https://www.example.com">Exempellänk</a></li>
        <li><a href="https://www.google.com">Google</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Sök efter det första h1-elementet
h1 = soup.find('h1')
print('Första H1', h1, '\n')

# Sök efter alla a-element
links = soup.find_all('a')
print('alla A-taggar', links, '\n')

# Hämta href-attributet från den första a-länken
first_link = links[0]
href = first_link.get('href')
print('HREF på första A-taggen', href, '\n')

# Skriv ut alla länktexter
print('Alla länktexter')
for link in links:
    print(link.text)

# Lägg till en ny p-tag
new_tag = soup.new_tag('p')
new_tag.string = 'Detta är en ny paragraf.'
soup.body.append(new_tag)

# Ta bort den första länken
first_link = links[0]
first_link.extract()

# Skriv ut den modifierade HTML-koden
print('\nNy HTML-kod:')
print(soup.prettify())