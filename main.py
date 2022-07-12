import pyshorteners
long_url = input("\nEnter the URL to shorten:\n")
 
shortener = pyshorteners.Shortener()

short_url = shortener.chilpit.short(long_url)


print("\nThe Shortened URL is:\n " + short_url)