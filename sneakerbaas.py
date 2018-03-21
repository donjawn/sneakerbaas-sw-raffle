import requests
from random import getrandbits
url = 'https://mailchi.mp/sneakerbaas/sean-wotherspoon-raffle'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit+1):
        num = getrandbits(40)
        firstname = 'firstname{}'.format(num) # put your name here, don't remove the {}
        lastname = 'lastname{}'.format(num) # put your name here, don't remove the {}
        addy1 = 'address 1' # enter address line 1 here
        addy2 = 'address 2' # enter address line 2 here, if none leave blank
        city = 'your city' # enter city
        state = 'your state' # enter state, spelled out. NO INITIALS!
        zipcode ='your zip' # enter your zip code
        twitterHandle = 'your twitter' #enter twitter handle with @ ie. @StrikeShoesHQ
        email = 'your_email+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'u': 'ca1123cd14fc268217c3cfcc4',
            'id': '00cac2e1f0',
            'EMAIL': email,
            'FNAME': firstname,
            'LNAME': lastname,
            'ADDRESS[addr1]': addy1,
            'ADDRESS[addr2]': addy2,
            'ADDRESS[city]': city,
            'ADDRESS[state]': state,
            'ADDRESS[zip]': zipcode,
            'ADDRESS[country]': '164', # leave as if for US residents
            'MMERGE7': twitterHandle,
            'MMERGE5': 'EU 42 | UK 7.5 | US 8.5', # change all 3 sizes to desired conversions if need be
            'MMERGE6': '1987', # leave as if
            'b_ca1123cd14fc268217c3cfcc4_714245': '', 
            'c': 'dojo_request_script_callbacks.dojo_request_script2'
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    x = int(raw_input("How many entries do you want: "))
    main(x)

# ALL CREDIT GOES TO github user yousefissa
# THIS SCRIPT IS MODIFICATION TO HIS PREEXISTING SCRIPTS
