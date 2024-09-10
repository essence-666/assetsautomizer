from google_sheets_sender import fill_cell
from dotenv import dotenv_values
import requests

config = dotenv_values()

def update_table() -> None:
    try:
        request = requests.get(config["RUBREQUEST"])
        rub_value = request.json()['data']['RUB']['value']
        headers = {
            "X-CoinAPI-Key": config['CRYPTO_API_KEY'] 
        }
        ton_value = requests.get(config['CRYPTO_URL'], headers=headers).json()['rate']
        print(ton_value)
        fill_cell(ton_value, config['TONCELL'])
        fill_cell(rub_value, config['RUBCELL'])
        fill_cell("", "I1")
    except:
        fill_cell("some api is reached their limits", "I1")
        print("some api is reached their limits")

