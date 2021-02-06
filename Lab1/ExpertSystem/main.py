import csv
import pprint
from fact import Fact

pp = pprint.PrettyPrinter(indent=4)

knowledge = {}


def read_knowledge():
    with open('data.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for raw in reader:
            fact_name = raw[0]
            parent_fact_name = raw[1]
            operand = raw[2]
            new_fact = Fact(fact_name, parent_fact_name, operand)
            # set_fact(new_fact)


if __name__ == '__main__':
    read_knowledge()
    pp.pprint(knowledge)
