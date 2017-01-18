import requests

#helpers
def send_request(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return display_system_Erro(resp.status_code)
    return resp

def assembl_url(symbol):
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + str(symbol) + "&f=sl1d1t1c1ohgv&e‌​=.csv"
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

def get_user_input(info = ''):
    if info == '':
        print("Please Enter A company Symbol to get Share Price:")
    else:
        print("Press y or Type yes to continue: Press Any other key to quit")
    user_in = input(" ")
    while(user_in == ''):
        user_in = input(" ")

    return user_in

def display_Results_to_user(user_output, demo = None):
    print('.....................................................................')
    print("%s |   %s   |   %s   |   %s  " %("Symbol", "Price", "Date","Time" ))
    print("  " + user_output[0] +"      " + user_output[1] + "        " + user_output[2]+"      " + user_output[3])
    print()
    print('.....................................................................')
    if(demo == True or user_output.__contains__("N/A")):
        print("Hello Esteemed user for more accurate result USE symbols only: E.g FaceBook -> FB")
    return

def start_program_logic():
    demo = True
    while(True):
        #get user Input
        user_in = get_user_input()

        #give symbole for validation
        symbol = get_stock(user_in)

        #get stock info
        info = get_stock_info(symbol)

        #parse info
        user_output = parse_output(info)

        #Display out parse_output
        display_Results_to_user(user_output, demo)

        #Ask if they want to quit
        user_in = get_user_input('end')
        if user_in == 'y' or user_in == 'yes':
            demo = False
        else:
            break

def main():
    start_program_logic()

if __name__ == '__main__':
    main()
