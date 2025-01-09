from generator import generate_people, generate_motorbikes, generate_streets
from handler.csv_list import write_people, write_motorbikes, write_streets
from handler.my_json import write_people as people_json, write_motorbikes as motorbikes_json, write_streets as streets_json
from handler.xslx import write_people as people_xslx, write_motorbikes as motorbikes_xslx, write_streets as streets_xslx

import openpyxl
#

def main():

    num_people = 10
    num_motorbikes = 5
    num_streets = 3

    people = generate_people(num_people)
    motorbikes = generate_motorbikes(num_motorbikes)
    streets = generate_streets(num_streets)

    write_people(people )
    write_motorbikes(motorbikes )
    write_streets(streets)

    people_json(people)
    motorbikes_json(motorbikes)
    streets.json(streets)


    wb = openpyxl.Workbook()
    people_xslx(people, wb, "people")
    motorbikes_xslx(motorbikes, wb, "motorbikes")
    streets_xslx(streets, wb, "street")
    wb.save("data.xlsx")


if __name__ == "__main__":
    main()
