from fact import Fact
import csv

knowledge = {}


def get_children_list(new_fact) -> list:
    children_list = []
    for fact_name in knowledge:
        fact: Fact = knowledge[fact_name]
        if fact.parent_fact_name == new_fact.fact_name:
            children_list.append(fact.fact_name)

    return children_list


def set_fact(new_fact):
    if not (new_fact.operand is None):
        children_list = get_children_list(new_fact)
        new_fact.child_facts = children_list

    knowledge[new_fact.fact_name] = new_fact


def read_knowledge():
    with open('data.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for raw in reader:
            fact_name = raw[0] if raw[0] != '' else None
            parent_fact_name = raw[1] if raw[1] != '' else None
            operand = raw[2] if raw[2] != '' else None
            new_fact = Fact(fact_name, parent_fact_name, operand)
            set_fact(new_fact)


def ask(fact_name) -> bool:
    response = input(fact_name + "? (y/n): ")
    return True if response == 'y' else False


def check_fact(fact_name) -> bool:
    fact_state = True
    fact = knowledge[fact_name]
    if fact.operand == "and":
        for child_fact_name in fact.child_facts:
            fact_state = fact_state and check_fact(child_fact_name)
        return fact_state
    elif fact.operand == "or":
        aux = False
        for child_fact_name in fact.child_facts:
            next_fact_status = check_fact(child_fact_name)
            if next_fact_status is True:
                print()
                print(child_fact_name.upper())
                print(fact_name.upper() + ", because " + child_fact_name)
                aux = True
        return aux
    else:
        return fact_state and ask(fact_name)


if __name__ == '__main__':
    read_knowledge()
    if check_fact("person"):
        print("Tourist types printed above")
    else:
        print("No tourist type found, probably a loonie")
