class Fact:
    fact_name = None
    parent_fact_name = None
    child_facts = []
    operand = None

    def __init__(self, fact_name, parent_fact_name, operand):
        self.fact_name = fact_name
        self.parent_fact_name = parent_fact_name
        self.operand = operand
