import requests
def get_tesla():
    url = "https://yahoo-finance97.p.rapidapi.com/stock-info"

    payload = "symbol=TSLA"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "7dc596c1fcmsh9cc541252b15086p180685jsnda63fba9b114",
        "X-RapidAPI-Host": "yahoo-finance97.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    ask_value = response.text[177:189] 

    print(f'TESLA Price : {ask_value}')
def get_apple():
    url = "https://yahoo-finance97.p.rapidapi.com/stock-info"

    payload = "symbol=AAPL"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "7dc596c1fcmsh9cc541252b15086p180685jsnda63fba9b114",
        "X-RapidAPI-Host": "yahoo-finance97.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    ask_value = response.text[179:191] 

    print(f'APPLE Price : {ask_value}')

get_tesla()
get_apple()
#display= dict.fromkeys(response, "TSLA")

#print(display)