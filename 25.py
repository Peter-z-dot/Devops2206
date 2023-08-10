import requests
response = requests.post('http://127.0.0.1:5001/whatismyname')
print(response.status_code)
print(response.text)
expected = 'saved new car'
actual = response.text
assert expected == actual
assert response.status_code == 200
