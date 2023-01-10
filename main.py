import time, os
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print(" ____  __   __  ____  _   _  ____   _____  ____   _____     _     ____    ____  _   _ ")
print("|  _ \ \ \ / / / ___|| | | || __ ) | ____|/ ___| | ____|   / \   |  _ \  / ___|| | | |")
print("| |_) | \ V / | |    | | | ||  _ \ |  _|  \___ \ |  _|    / _ \  | |_) || |    | |_| |")
print("|  __/   | |  | |___ | |_| || |_) || |___  ___) || |___  / ___ \ |  _ < | |___ |  _  |")
print("|_|      |_|   \____| \___/ |____/ |_____||____/ |_____|/_/   \_\|_| \_\ \____||_| |_|")

print("                                                                       made by Argk")
anzahl = 16
product = input("What product are you looking for?")
f = open([YOUR PATH HERE], "a")
f.write(f"Results for {product}:\n")
f.close()
counter = 0
def shop(name, ShopSearchUrl, ErrorMessage):
    global ctx
    fullurl = ShopSearchUrl + product
    html = urlopen(fullurl, context=ctx).read().decode("utf-8")
    if f"{ErrorMessage}" in html:
        f = open([YOUR PATH HERE], "a")
        f.write(f"{name}: Not Found \n")
        f.close()
        
    else:
        f = open([YOUR PATH HERE], "a")
        f.write(f"{name}: Found {fullurl}\n")
        f.close()
        
shop("euro-cubes.com", "https://euro-cubes.com/search?options%5Bprefix%5D=last&q=", "Keine Ergebnisse gefunden")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")


shop("speedcubeshop.com", "https://speedcubeshop.com/search?type=product&q=", "did not return any results. Please try again.")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("thecubicle.com", "https://www.thecubicle.com/search?q=", ">No results found</h1>")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("ziicube.com", "https://www.ziicube.com/index.php?route=product%2Fsearch&keyword=", "did not match any products.")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("knobelbox.com", "https://www.knobelbox.com/search?sSearch=", "Leider wurden zu Ihrer Suchanfrage keine Artikel gefunden ")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("speedcube.com.au", "https://www.speedcube.com.au/search?type=product&options%5Bprefix%5D=last&q=", "No results could be found for")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("cubingoutloud.com", "https://www.cubingoutloud.com/search?q=", "Try checking your spelling or using different words.")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("dailypuzzles.com", "https://www.dailypuzzles.com.au/a/search?type=article%2Cpage%2Cproduct&q=", "no-results-title")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("cubelelo.com", "https://www.cubelelo.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=last&q=", "No results could be found for")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("cubewerkz.com", "https://www.cubewerkz.com/search?q=", "did not yield any results")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("kewbz.co.uk", "https://kewbz.co.uk/search?type=product&q=", "No results could be found for")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("speedcube.co.nz", "https://www.speedcube.co.nz/search?q=", "0 matches for")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("cubikon.de", "https://cubikon.de/search?sSearch=", "Leider wurden zu deiner Suchanfrage keine Artikel gefunden ")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("puzzle-corner.de","http://www.puzzle-corner.de/epages/82949342.sf/de_DE/?ObjectID=11529501&ViewAction=FacetedSearchProducts&SearchString=", "Ihre Suchanfrage ergab keine Treffer.")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("cubediction.com", "https://www.cubediction.com/de/?s=", "Die angefragte Seite konnte nicht gefunden werden. Verfeinern Sie ")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

shop("cubeshop.ch", "https://cubeshop.ch/de/suche?controller=search&s=", "Entschuldigen Sie die Unannehmlichkeiten")
os.system("CLS")
counter = counter + 1
print(f"{counter} out of {anzahl} shops checked")

