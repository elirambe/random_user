import requests

num_of_users = int(input("Please enter a positive number smaller than 100: "))

if num_of_users > 100 or num_of_users < 1:
    print("Invalid input. Please enter a positive number smaller than 100.")
else:
    for i in range(num_of_users):
        response = requests.get("https://randomuser.me/api/")
        data = response.json()
        name = data["results"][0]["name"]["first"] + " " + data["results"][0]["name"]["last"]
        print(name)