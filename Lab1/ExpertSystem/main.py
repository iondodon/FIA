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


def has_child(fact_name) -> bool:
    for fact_key in knowledge:
        fact = knowledge[fact_key]
        if fact.parent_fact_name == fact_name:
            return True
    return False


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
        for child_fact_name in fact.child_facts:
            if check_fact(child_fact_name) is True:
                return True
        return False
    else:
        return fact_state and ask(fact_name)


if __name__ == '__main__':
    read_knowledge()

    print("---Checking if the person is a tourist---")
    if check_fact("tourist"):
        print("Yes, the person is a tourist")
    else:
        print("No, the person is not a tourist, which means it is a loonie")

    # print()
    # print("---Checking if the person is a loonie---")
    # if check_fact("loonie"):
    #     print("Yes, the person is a loonie")
    # else:
    #     print("No, the person is not a loonie, which means it is a tourist")
