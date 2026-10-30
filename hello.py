import requests

response = requests.get('https://api.github.com')
print(response.status_code)
if response.status_code == 200:
    print('Success!')
    print(response.json())
    
    
def fetch_github_api():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from GitHub API', 'status_code': response.status_code}
    
data = fetch_github_api()
print("Fetched Data: \n", data)

try:
    print("Hello, World!" + 3) # will throw error, use str()
except:
    print(f"Error: Converting integer to string.")
    
print("Hello, World!" + 3) # will throw error, use str()