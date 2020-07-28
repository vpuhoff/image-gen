app_id = '5084739164692335824'
app_secret = '8aa08a7315cbf385a4f3572264f868e8d220625c928bd0e6c428be69b2c05e4d'
#get token http://jako.tech/pinterest/access_token_oauth.php
app_token = 'Arp3JS3p3frmRIM138uwoigN38XNFfZuPCg_Ko5GkJ9UhwDM0As4QDAAARM9RpCovdrA0ngAAAAA'

import pinterest

api = pinterest.Pinterest(token=app_token)

limits = api.me()['ratelimit']['remaining']

if limits >0:
    pins = api.board("vpuhoff92/hard-metal-machine").pins()['data']
    for pin in pins:
        id = pin['id']
        pin_info=api.pin(id).fetch()
        print(pin_info)
else:
    print('limit exceed...')