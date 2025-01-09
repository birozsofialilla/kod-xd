from generator import generate_people, generate_cars, generate_airports
from file_handler.csv_list import save_people_to_csv, save_cars_to_csv, save_airports_to_csv
from file_handler.my_json import save_people_to_json, save_cars_to_json, save_airports_to_json
from file_handler.xlsx import save_people_to_xlsx, save_cars_to_xlsx, save_airports_to_xlsx

def main():

    num_people = 10
    num_cars = 5
    num_airports = 3

    people = generate_people(num_people)
    cars = generate_cars(num_cars)
    airports = generate_airports(num_airports)

    save_people_to_csv(people, 'people.csv')
    save_cars_to_csv(cars, 'motorbikes.csv')
    save_airports_to_csv(airports, 'streets.csv')

    save_people_to_json(people, 'people.json')
    save_cars_to_json(cars, 'motorbikes.json')
    save_airports_to_json(airports, 'streets.json')


    save_people_to_xlsx(people, 'people.xlsx')
    save_cars_to_xlsx(cars, 'cars.xlsx')
    save_airports_to_xlsx(airports, 'airports.xlsx')


if __name__ == "__main__":
    main()
