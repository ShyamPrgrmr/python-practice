import requests

contries_list_api_url = "https://covid-193.p.rapidapi.com/countries"
statistics_api_url = "https://covid-193.p.rapidapi.com/statistics"


headers = {
    "x-rapidapi-host": "covid-193.p.rapidapi.com",
    "x-rapidapi-key": "0ede3d2d26msh7ec3836e5b159f6p1d3af9jsn74d7286acbc4"
}

get_request = requests.get(contries_list_api_url, headers=headers)
response = get_request.json()
countries = response["response"]

#filter country name start with 'A'
data = list(map(lambda x: x,filter(lambda y: str(y)[0]=="A", countries)))
#print(data)

get_request = requests.get(statistics_api_url, headers=headers)
response = get_request.json()["response"]

#get 'Africa' continent deaths

deaths = [] 
death_count = 0

for data in response:
    if(data["continent"]=="Africa"):
        country_name = data["country"]
        deaths_data = data["deaths"]
        if(deaths_data["total"] != None):
            deaths.append(dict(
                country_name= country_name,
                death_count= int(deaths_data["total"])
            ))

#Aggreagation

for death in deaths:
    death_count = death_count + death["death_count"] 


print("Total death in Africa : "+ str(death_count))



