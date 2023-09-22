from csv import *

hotel_rates = {}
exchange_rates = {}
flight_costs = {}

def load_hotel_rates(file):  
    with open(file) as h:
        hotel_rates = reader(h)
        for row in hotel_rates:
            hotel_rates[row[0]] = float(row[1])

def load_exchange_rates(file): 
    with open(file) as e:
        hotel_rates = reader(e)
        for row in hotel_rates:
            exchange_rates[row[0].upper()] = float(row[1]) * 1 

def load_flight_costs(file):
    with open(file) as flight_costs:
        hotel_rates = reader(flight_costs)
        for row in hotel_rates:
            flight_costs[row[0]] = float(row[1])

def main():
    load_hotel_rates('data/hotel_rates.csv')
    load_exchange_rates('data/exchange_rates.csv')
    load_flight_costs('data/flight_costs.csv')

    destination = input("Enter your destination: ").upper()

    flight_cost = flightCosts.get(destination, 0.0)
    hotel_cost = hotelRates.get(destination, 0.0)

    stay_duration = int(input("Enter your stay duration in days: "))
    hotel_cost *= days
    total_cost = flight_cost + hotel_cost

    print(f"Flight cost: USD {flight_cost:.2f}")
    print(f"Hotel cost for {days} days: USD {hotel_cost:.2f}")
    print(f"Total: USD {total:.2f}")

    currency = input(f"Select your currency for final price estimation ({', '.join(exchange_rates.keys())}): ")

    p = total * exchangeRates[currency]
    print(f"Total in {currency}: {p:.2f}")

if __name__ == "__main__":
    main()
