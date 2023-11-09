import requests

health = requests.get("http://20.122.46.168/eurowings/flights/health")
print(f"Server Response: {health.json()} with HTTP Header Data: {health.headers.values()}")

# health.json(), health.text, health.raw and other formats also possible.

response = requests.get("http://20.122.46.168/eurowings/flights/status?status=delayed")
delayed_flights = response.json()

for flight in delayed_flights:
    flight_number = flight["flight_number"]
    flight_name = flight["name"]
    flight_status = flight["status"]
    flight_source = flight["source"]
    flight_destination = flight["destination"]
    flight_airline = flight["airline"]

    print(f"The Flight details are:\n flight number: {flight_number} \n flight name: {flight_name} \n current flight status: {flight_status} \n flight is from {flight_source} to {flight_destination} \n airlines name: {flight_airline}")


