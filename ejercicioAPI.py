import requests
 
url = "https://randomuser.me/api/?results=3&inc=name,picture,nat"
 
response = requests.get(url, timeout=10)

data = response.json()
 
for i, user in enumerate(data["results"], start=1):

    first_name = user["name"]["first"]

    last_name = user["name"]["last"]

    country = user["nat"]

    image_url = user["picture"]["large"]
 
    image_response = requests.get(image_url, timeout=10)
 
    filename = f"{i}{first_name}{last_name}.jpg".replace(" ", "_")
 
    with open(filename, "wb") as file:

        file.write(image_response.content)
 
    print(f"Saved: {filename} | Country: {country}")