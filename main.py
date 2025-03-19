import requests

api_url = "https://uselessfacts.jsph.pl/random.json?language=en"

#function to fetch and display a random fact

def get_random_fact():
    response = requests.get(api_url)
    if response.status_code == 200:
        fact_data = response.json()
        fact = fact_data['text']
        print(f"Did you know? {fact}")
    else:
        print("failed to fetch fact!!")

#main loop to interact with the user:
while True:
    input("press enter to get a random fact or type q to quit: ")
    if input().lower() == 'q':
        break 
    else:
        get_random_fact()

