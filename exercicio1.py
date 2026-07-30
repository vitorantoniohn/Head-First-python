import urllib.request
import time

price = 99.99

while price > 4.47:  
    time.sleep(1000)  # Wait for 60 seconds before checking the price again
    page = urllib.request.urlopen("https://www.youtube.com/")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price : end_of_price])
print("Buy!") 