import pandas as pd

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

scrapper = pd.read_html("https://fr.wikipedia.org/wiki/Linux")

print(scrapper)

for index, table in enumerate(scrapper):
    print("*************************************************************")
    print(index)
    print(table)
    

print(scrapper[3])