import requests

#helpers
def send_request(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return display_system_Erro(resp.status_code)
    return resp

def assembl_url(symbol):
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + symbol + "&f=sl1d1t1c1ohgv&e‌​=.csv"
    return url

#our API Core
def get_stock(symbol):
    if type(symbol) != type('s'):
        display_user_Error()
    else:
        return symbol

def get_stock_info(symbol):
    url = assembl_url(symbol)
    info = str(send_request(url).content)
    return info

def parse_output(string_info):
    output = string_info[2:len(string_info) - 17]
    output = output.replace("\"", '').split(',')
    return output

def display_user_Error(info = ''):
    print("Sorry An Erro occured: Please enter Valid Input: __")
    return

def display_system_Erro(info):
    print("We Apologize for the inconvinece, A System erro occured" + " Status: " + str(info))
    return

def start_program_logic():
    pass

def main():
    start_program_logic()

if __name__ == '__main__':
    main()
