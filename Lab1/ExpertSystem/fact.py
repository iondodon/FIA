class Fact:
    __fact_name = None
    __parent_fact_name = None
    __child_facts = []
    __operand = None

    def __init__(self, fact_name, parent_fact_name, operand):
        self.__fact_name = fact_name
        self.__parent_fact_name = parent_fact_name
        self.__operand = operand

    def set_operand(self, operand):
        self.__operand = operand

    def get_operand(self):
        return self.__operand

    def add_child_fact(self, child_fact):
        self.__child_facts.append(child_fact)

    def set_fact_name(self, fact_name):
        self.__fact_name = fact_name

    def get_fact_name(self):
        return self.__fact_name

    def set_parent_fact_name(self, parent_fact_name):
        self.__parent_fact_name = parent_fact_name

    def get_parent_fact_name(self):
        return self.__parent_fact_name

    def set_child_facts(self, child_facts):
        self.__child_facts = child_facts

    def get_child_facts(self):
        return self.__child_facts
