import urllib2, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument("amount", help="amount to calculate in USD", type=float)
args = parser.parse_args()

price_url = "http://api.coindesk.com/v1/bpi/currentprice.json"
bpi_data = json.load(urllib2.urlopen(price_url))
input_amt = args.amount
satoshi_amt = input_amt / float((bpi_data.get("bpi").get("USD").get("rate"))) * 100000000

print "${0:.2f} is equal to {1:,} satoshi".format(input_amt, int(satoshi_amt))
