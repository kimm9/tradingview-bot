import ccxt
import config

ftx = ccxt.ftx({
    'apiKey': config.API_KEY,
    'secret': config.SECRET_KEY,
})

def get_quote(request):
    symbol = request.args.get('symbol')

    try:
        quote = ftx.fetch_ticker(symbol)
    except Exception as e:
        return {
            "code": "error",
            "message": str(e)
        }

    return quote

def trade_crypto(request):
    data = request.get_json()

    order = ftx.create_market_buy_order(data['symbol'], data['quantity'])
    

    return order