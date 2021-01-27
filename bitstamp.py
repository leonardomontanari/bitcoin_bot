import ssl
import json

import websocket


def ao_abrir(ws):
    print("Abriu a conexão")
    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """
    ws.send(json_subscribe)


def ao_fechar(ws):
    print("Fechou a conexão")


def erro(ws, erro):
    print("Deu erro")
    print(erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    if mensagem['data'] and mensagem['data']['price']:
        price = mensagem['data']['price']
        print("$ {}".format(price))


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.", on_open=ao_abrir, on_close=ao_fechar,
                                on_message=ao_receber_mensagem, on_error=erro)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
