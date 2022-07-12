import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
shortener = pyshorteners.Shortener()

short_url = shortener.chilpit.short(long_url)


print("The Shortened URL is: " + short_url)