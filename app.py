import requests

def get_bitcoin_price():
       url = 'https://api.coingecko.com/api/v3/simple/price'
       params = {
              'ids': 'bitcoin',
              'vs_currencies': 'usd,eur,irr,cad'
       }

       try:
              response = requests.get(url, params=params)
              data = response.json()
              
              if 'bitcoin' in data:
                     bitcoin_data = data['bitcoin']
                     usd_price = bitcoin_data.get('usd')
                     eur_price = bitcoin_data.get('eur')
                     irr_price = bitcoin_data.get('irr')
                     cad_price = bitcoin_data.get('cad')

                     return usd_price, eur_price, irr_price, cad_price
              else:
                     print('Error: Unable to retrieve Bitcoin price data.')
                     return None

       except Exception as e:
              print(f'Error: {e}')
              return None

if __name__ == "__main__":
       prices = get_bitcoin_price()

       if prices is not None:
              usd_price, eur_price, irr_price, cad_price = prices
              print(f"Current Bitcoin Price:")
              print(f"USD: ${usd_price}")
              print(f"Euro: €{eur_price}")
              print(f"Iranian Rial: {irr_price} IRR")
              print(f"Canadian Dollar: ${cad_price}")
