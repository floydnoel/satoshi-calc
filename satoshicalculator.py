import urllib2, json, sys

if(len(sys.argv) != 2):
	print "Usage: dollars2satoshis.py [USD_amount]"
	sys.exit(1)

price_url = "http://api.coindesk.com/v1/bpi/currentprice.json"
bpi_data = json.load(urllib2.urlopen(price_url))
input_amt = sys.argv[1]
satoshi_amt = int((float(input_amt)) / float((bpi_data.get("bpi").get("USD").get("rate"))) * 100000000)

print "${0} is equal to {1:,} satoshi".format(input_amt, satoshi_amt)