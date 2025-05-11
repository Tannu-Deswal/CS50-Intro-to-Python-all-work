import sys
import requests as r
def main():
    if len(sys.argv)!=2:
        print('Missing command-line argument')
        sys.exit(1)
    inp = sys.argv[1]
    try:
        inp = float(inp)
    except ValueError:
        print('Command-line argument is not a number')
        sys.exit(1)
            
    try:
        request = r.get('http://rest.coincap.io/v3/assets/bitcoin?apiKey=63b632fef726d9b977e9600cbdb7d603f418293fcdbb2d7bad370da89ac401e0')
        res = request.json()
        price = res['data']['priceUsd']
        price = float(price)
        total = price*inp
        print(f'${total:,.4f}')
    except r.RequestException:
        print('Error')
        return
    
main()