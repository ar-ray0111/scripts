import requests

def api_call():
    res = requests.get(f"https://www.affirmations.dev/")

    json_data = res.json()


    affirmation = json_data['affirmation']
    return affirmation

run = 'y'
while run == 'y':
    print(api_call())

    run = input("Do you want another one? y/n: ").strip()

