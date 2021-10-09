import json
import urllib.request as ur
import urllib.parse as up

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    param = dict()
    param['sensor'] = 'false'
    param['address'] = address
    param['key'] = api_key
    url = serviceurl + up.urlencode(param)


    print ('Retrieving ',url)
    url_handle = ur.urlopen(url)
    data = url_handle.read()

    print ('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    #lat = js['results'][0]['geometry']['location']['lat']
    #lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)

    #location = js['results'][0]['formatted_address']
    #print(location)

    print ('Place id',js['results'][0]['place_id'])
    
    
#Sample output
#Enter location: UIUC
#Retrieving  http://py4e-data.dr-chuck.net/json?sensor=false&address=UIUC&key=42
#Retrieved 1654 characters
#Place id ChIJ6VUmqSTXDIgR-iZoBCUFPKU
#Enter location:
