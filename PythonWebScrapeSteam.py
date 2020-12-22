import requests
res = requests.get("https://store.steampowered.com//")

import bs4
soup = bs4.BeautifulSoup(res.text, "lxml")

#get the topseller games
topsellers = soup.select("#tab_topsellers_content a.tab_item")

#create csv file
f = open("SteamTopGamesPy.csv", "w")

#header row of the csv file
f.write("Rank, Title, Price, Tags\n")

#iteration of topseller game details
Rank = 0
for container in topsellers:
    Rank += 1
    Title = container.select(".tab_item_name")[0].text
    FinalPrice = container.select(".discount_final_price")[0].text
    #OrigPrice = container.select(".discount_original_price")[0].text
    Tags = container.select(".tab_item_top_tags")[0].text
    
    f.write(str(Rank)+","+Title+","+FinalPrice.replace(",",".")+","+Tags.replace(",",".")+"\n")

#close the csv file
f.close()