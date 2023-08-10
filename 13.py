import requests
my_file = open("URLS.txt")
for url in my_file.readlines():
    curr_url = url.strip()
    response = requests.get(curr_url)
    if response.status_code == 200:
        print(f"{curr_url.split('//')[1]} is up and running")
