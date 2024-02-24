import requests
import pandas as pd 
import json
# import pandas as pd
#21, 14 [{'Name': 'Saskia Jurriaans', 'Role': 'Treasurer', 'uuid': '3e20cfe7-20f1-ec11-bb3c-000d3ad1769c'}, {'Name': 'Michelle Dyer', 'Role': 'Committee Member', 'uuid': '8517be32-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Stephanie Nitschke', 'Role': 'Secretary', 'uuid': '9b17be32-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Catheline Froehlich', 'Role': 'Committee Member', 'uuid': 'd05eb638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Graeme Cumming', 'Role': 'Vice-president', 'uuid': '605fb638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Kate Quigley', 'Role': 'Committee Member', 'uuid': 'c45fb638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Tessa Hill', 'Role': 'Committee Member', 'uuid': '2960b638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Anna Scott', 'Role': 'Committee Member', 'uuid': 'd160b638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Sarah Hamylton', 'Role': 'Other', 'uuid': '3761b638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Katie Sambrook', 'Role': 'Committee Member', 'uuid': '5961b638-0628-ed11-9db1-000d3ad21577'}, {'Name': 'David Suggett', 'Role': 'President', 'uuid': 'c6a6ae3e-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Kennedy Wolfe', 'Role': 'Committee Member', 'uuid': '80a7ae3e-0628-ed11-9db1-000d3ad21577'}, {'Name': 'Jodie Rummer', 'Role': 'Committee Member', 'uuid': 'bca7ae3e-0628-ed11-9db1-000d3ad21577'}, {'Name': 'samantha Goyen', 'Role': 'Committee Member', 'uuid': '6ba8ae3e-0628-ed11-9db1-000d3ad21577'}]
#0,"[{'Name': 'Collin Visaggio', 'Role': 'Treasurer', 'uuid': 'd379dd1e-c2d5-ec11-a7b5-002248944339'}, {'Name': 'Giovanni Minutillo', 'Role': 'President', 'uuid': '95ce9ab8-07f2-ec11-bb3e-002248116f6b'}, {'Name': 'Nicola Visaggio', 'Role': 'Secretary', 'uuid': 'ccce9ab8-07f2-ec11-bb3e-002248116f6b'}, {'Name': 'Nunzio Pisani', 'Role': 'Vice-president', 'uuid': 'eece9ab8-07f2-ec11-bb3e-002248116f6b'}, {'Name': 'Antonietta Massara', 'Role': 'Committee Member', 'uuid': '2148d356-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Marisa Pisani', 'Role': 'Committee Member', 'uuid': '4648d356-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Sonia La Macchia', 'Role': 'Committee Member', 'uuid': '5d48d356-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Nicola Trolio', 'Role': 'Committee Member', 'uuid': '9148d356-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Antonina Graziano', 'Role': 'Committee Member', 'uuid': 'cb48d356-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Rita Onoforo', 'Role': 'Committee Member', 'uuid': 'adf2cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Joseph Onoforo', 'Role': 'Committee Member', 'uuid': 'e0f2cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Anna Minutillo', 'Role': 'Committee Member', 'uuid': '0df3cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Antonio Monterosso', 'Role': 'Committee Member', 'uuid': '34f3cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Domenic Morolla', 'Role': 'Committee Member', 'uuid': '53f3cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Fedele Arangio', 'Role': 'Committee Member', 'uuid': '89f3cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Girolamo Alberti', 'Role': 'Committee Member', 'uuid': 'a1b73643-1bbc-e811-a961-000d3ad24282'}, {'Name': 'Salvatore Galati', 'Role': 'Committee Member', 'uuid': 'd5f3cd5c-e1f9-ec11-82e6-00224811654f'}, {'Name': 'Marcus Gangemi', 'Role': 'Board Member', 'uuid': '54b62e42-a6cf-ed11-a7c7-00224893bc23'}, {'Name': 'Carlo Tomeo', 'Role': 'Board Member', 'uuid': '6eb62e42-a6cf-ed11-a7c7-00224893bc23'}]",FISHING FLEET FESTIVAL ASSOCIATION,19
# 63371328019
Number=pd.read_csv(r"1000 ABN.csv")
# print(Number)
list=[]
list1=[]
list2=[]
cookies = {
    '_ga': 'GA1.1.1105843403.1705250234',
    'ak_bmsc': '10AA5146B8AFEC30C79C55A273F75811~000000000000000000000000000000~YAAQh5YRYF5v0AiNAQAAu4ZZCRawy5fH47EUIpZN+IBwmJ7kZNJsE7K/1tABh7KNpkA6HsaCsZO2/McpBRCu7wxQl5DkhEAY/Zs5BEKo59ONy8b3m+R1wzzZ03GFguGk9a9kSGaUCmpwraXjPiOK4dPQesjudpjPspK7fA/ixHgMSVE/03HCXOzh5aJSVN3q2w+IM8mHbGgQcanDGfrs1PK5zNTAahLHGZPEAt49a/CvecfYjI6kt0wcpBxco/6Y8dnKmTIdkedu2tAfPAZA50G8MRjHpqB+3OHNiLmwtDuGXQ93ZqX8COB98/3IAioNxMNdtbIt1APJI62L5Fnk+villhe3zcD/7hv/x4X1GR3TwiSVrYrwK8vw17uE29rAL6m3zSDqqU5Fu5eu3AROxN2dhw7RgA122Dn4oqGX6eljYpZf4eAMR7niUezK8XB/I4uTefkmQOb3GfplZJVyRI0/6B7xcl8on3lRFFJSZrrRnnFz/YI4am2Xj3ze+Z0=',
    '_ga_WCGKJ5Z7LL': 'GS1.1.1705258879.3.0.1705258879.60.0.0',
    'bm_sv': '2F51842D5E21DACCDD26F93A11BA78D7~YAAQh5YRYJtv0AiNAQAA5rdZCRYnLO/MYw/KqKuzxLT0a07qTAriSbTHvpxm5oHgPrseY+reGjjP+j73sw/U7xUAf6BuvopsR90VT+aevvxCou7G0x9d2ll40fAMGccFy+2hVPQiVIsEC1Ryf5EEwphZpFBJS1f9l3/IBeGeCxo6juVpVqf5yzFXSDw6AaXAdVZCtdVE1tOAQlkgB2cjbnYSoIxf8vEOu4xhbkRhgAXDuWw96WYmU5lXtn5juKO+OA==~1',
}

headers = {
    'Host': 'www.acnc.gov.au',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.acnc.gov.au/charity/charities',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=1, i',
    # 'Cookie': '_ga=GA1.1.1105843403.1705250234; ak_bmsc=10AA5146B8AFEC30C79C55A273F75811~000000000000000000000000000000~YAAQh5YRYF5v0AiNAQAAu4ZZCRawy5fH47EUIpZN+IBwmJ7kZNJsE7K/1tABh7KNpkA6HsaCsZO2/McpBRCu7wxQl5DkhEAY/Zs5BEKo59ONy8b3m+R1wzzZ03GFguGk9a9kSGaUCmpwraXjPiOK4dPQesjudpjPspK7fA/ixHgMSVE/03HCXOzh5aJSVN3q2w+IM8mHbGgQcanDGfrs1PK5zNTAahLHGZPEAt49a/CvecfYjI6kt0wcpBxco/6Y8dnKmTIdkedu2tAfPAZA50G8MRjHpqB+3OHNiLmwtDuGXQ93ZqX8COB98/3IAioNxMNdtbIt1APJI62L5Fnk+villhe3zcD/7hv/x4X1GR3TwiSVrYrwK8vw17uE29rAL6m3zSDqqU5Fu5eu3AROxN2dhw7RgA122Dn4oqGX6eljYpZf4eAMR7niUezK8XB/I4uTefkmQOb3GfplZJVyRI0/6B7xcl8on3lRFFJSZrrRnnFz/YI4am2Xj3ze+Z0=; _ga_WCGKJ5Z7LL=GS1.1.1705258879.3.0.1705258879.60.0.0; bm_sv=2F51842D5E21DACCDD26F93A11BA78D7~YAAQh5YRYJtv0AiNAQAA5rdZCRYnLO/MYw/KqKuzxLT0a07qTAriSbTHvpxm5oHgPrseY+reGjjP+j73sw/U7xUAf6BuvopsR90VT+aevvxCou7G0x9d2ll40fAMGccFy+2hVPQiVIsEC1Ryf5EEwphZpFBJS1f9l3/IBeGeCxo6juVpVqf5yzFXSDw6AaXAdVZCtdVE1tOAQlkgB2cjbnYSoIxf8vEOu4xhbkRhgAXDuWw96WYmU5lXtn5juKO+OA==~1',
}
# for i in Number["ABN"]:
for index, row in enumerate(Number["ABN"], start=1):
    proxy_options={
    "proxy" :{
        "http": "",
    }
}
    if 800 <= index <=1000 :# 100-150, 1 5,10-20,30-50 200-250 450-500,500-650
        i=row
        print(i)
        params = {
            'search': f'{i}',
        }

        response = requests.get(
            'https://www.acnc.gov.au/api/dynamics/search/charity',
            params=params,
            cookies=cookies,
            headers=headers,
            proxies=proxy_options,
            verify=False,
        )
        # print(response.json())
        print(response.json)
        result = response.json()
        # print(result["results"][0]["uuid"])
        # print(result["results"][0]["data"]["Name"])
        # print(result["results"][0]["uuid"])
        # for i in result["results"]:
        #     print(i["uuid"])
        user_Name=result["results"][0]["data"]["Name"]
        uuid=result["results"][0]["uuid"]
        print(user_Name)
        list2.append(user_Name)
        cookies = {
            '_ga': 'GA1.1.1105843403.1705250234',
            'ak_bmsc': '10AA5146B8AFEC30C79C55A273F75811~000000000000000000000000000000~YAAQh5YRYF5v0AiNAQAAu4ZZCRawy5fH47EUIpZN+IBwmJ7kZNJsE7K/1tABh7KNpkA6HsaCsZO2/McpBRCu7wxQl5DkhEAY/Zs5BEKo59ONy8b3m+R1wzzZ03GFguGk9a9kSGaUCmpwraXjPiOK4dPQesjudpjPspK7fA/ixHgMSVE/03HCXOzh5aJSVN3q2w+IM8mHbGgQcanDGfrs1PK5zNTAahLHGZPEAt49a/CvecfYjI6kt0wcpBxco/6Y8dnKmTIdkedu2tAfPAZA50G8MRjHpqB+3OHNiLmwtDuGXQ93ZqX8COB98/3IAioNxMNdtbIt1APJI62L5Fnk+villhe3zcD/7hv/x4X1GR3TwiSVrYrwK8vw17uE29rAL6m3zSDqqU5Fu5eu3AROxN2dhw7RgA122Dn4oqGX6eljYpZf4eAMR7niUezK8XB/I4uTefkmQOb3GfplZJVyRI0/6B7xcl8on3lRFFJSZrrRnnFz/YI4am2Xj3ze+Z0=',
            '_ga_WCGKJ5Z7LL': 'GS1.1.1705258879.3.1.1705259417.44.0.0',
            'bm_sv': '2F51842D5E21DACCDD26F93A11BA78D7~YAAQHNYLFwqpzO2MAQAASsBhCRZzV0ORBoIpw0vwxre/RYTis2iSM1WKy+Ie13Tm+FeTxadv4QytB2EMg8H8oHotmcMfSCRrCx9jy1oedxJXvd30lrUNNchDn/Wk2mQqaj40dveRr9a8IeM2gaEZUd4HmQcewoTQN19UN1+zS41kr8nJHgaQUhkwhymatd5vEiNxr/Gx05sX1Sl9rfInTBeFB2YzQqeOXV23B7O9j1ZsI8F0ZFdMatj7d5UETlRc+3Q=~1',
        }

        headers = {
        'Host': 'www.acnc.gov.au',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.acnc.gov.au/charity/charities?search=63371328019',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        # 'Cookie': '_ga=GA1.1.1105843403.1705250234; ak_bmsc=10AA5146B8AFEC30C79C55A273F75811~000000000000000000000000000000~YAAQh5YRYF5v0AiNAQAAu4ZZCRawy5fH47EUIpZN+IBwmJ7kZNJsE7K/1tABh7KNpkA6HsaCsZO2/McpBRCu7wxQl5DkhEAY/Zs5BEKo59ONy8b3m+R1wzzZ03GFguGk9a9kSGaUCmpwraXjPiOK4dPQesjudpjPspK7fA/ixHgMSVE/03HCXOzh5aJSVN3q2w+IM8mHbGgQcanDGfrs1PK5zNTAahLHGZPEAt49a/CvecfYjI6kt0wcpBxco/6Y8dnKmTIdkedu2tAfPAZA50G8MRjHpqB+3OHNiLmwtDuGXQ93ZqX8COB98/3IAioNxMNdtbIt1APJI62L5Fnk+villhe3zcD/7hv/x4X1GR3TwiSVrYrwK8vw17uE29rAL6m3zSDqqU5Fu5eu3AROxN2dhw7RgA122Dn4oqGX6eljYpZf4eAMR7niUezK8XB/I4uTefkmQOb3GfplZJVyRI0/6B7xcl8on3lRFFJSZrrRnnFz/YI4am2Xj3ze+Z0=; _ga_WCGKJ5Z7LL=GS1.1.1705258879.3.1.1705259417.44.0.0; bm_sv=2F51842D5E21DACCDD26F93A11BA78D7~YAAQHNYLFwqpzO2MAQAASsBhCRZzV0ORBoIpw0vwxre/RYTis2iSM1WKy+Ie13Tm+FeTxadv4QytB2EMg8H8oHotmcMfSCRrCx9jy1oedxJXvd30lrUNNchDn/Wk2mQqaj40dveRr9a8IeM2gaEZUd4HmQcewoTQN19UN1+zS41kr8nJHgaQUhkwhymatd5vEiNxr/Gx05sX1Sl9rfInTBeFB2YzQqeOXV23B7O9j1ZsI8F0ZFdMatj7d5UETlRc+3Q=~1',
        }

        response = requests.get(
            f'https://www.acnc.gov.au/api/dynamics/entity/{uuid}',
            cookies=cookies,
            headers=headers,
            proxies=proxy_options,
            verify=False,
        )

        # print(response.json())

        ResponsiblePersons=response.json()
        try:
            print(ResponsiblePersons["data"]["ResponsiblePersons"])
            print(len(ResponsiblePersons["data"]["ResponsiblePersons"]))
            # print()
            list.append(ResponsiblePersons["data"]["ResponsiblePersons"])
            list1.append(len(ResponsiblePersons["data"]["ResponsiblePersons"]))
        except:
            pass

df=pd.DataFrame(columns=["Info","Name_charity","Length"])
try:
    df["Info"]=list
    df["Length"]=list1
    df["Name_charity"]=list2
except:
    pass
print(df)
df.to_csv(r'final_data.csv')
print(df)