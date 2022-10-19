import requests

while True:
    user_input = input("Enter Pokemon name: ")
    user_input = user_input.lower()

    URL = f"https://pokeapi.co/api/v2/pokemon/{user_input}"
    req = requests.get(URL)
    if req.status_code == 200:
        pokemon_data= req.json()

        print(f"Name is\t\t{pokemon_data['name']}")
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(ability['ability']['name'])

    else:
        print("Pokemon not found!")
