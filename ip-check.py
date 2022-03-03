from colorama import Fore
b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX
import requests, argparse, socket

parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Input domain/ip')
args = parse.parse_args()

if args.target:
    target = socket.gethostbyname(args.target)
    url = f'https://ipinfo.io/{target}/json'
    r = requests.get(url)
    a = r.json()
    city = a['city']
    hostname = a['hostname']
    region = a['region']
    country = a['country']
    loc = a['loc']
    org = a['org']
    timezone = a['timezone']
    
    print(c+f'IP: {target}\nCity: {city}\nHostName: {hostname}\nRegion: {region}\nCountry: {country}\nLocation: {loc}\nORG: {org}\nTime Zone: {timezone}')
else:
    exit(red+'''Expected Ergument\n  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Input domain/ip''')