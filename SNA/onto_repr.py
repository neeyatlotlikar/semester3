class Individual:
    def __init__(self, id, name, age=None, gender=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.relationships = []  # List of Relationship objects

    def add_relationship(self, relationship):
        self.relationships.append(relationship)

    def __repr__(self):
        return f"Individual(id={self.id}, name={self.name})"


class Relationship:
    def __init__(self, from_individual, to_individual, relation_type):
        self.from_individual = from_individual
        self.to_individual = to_individual
        self.type = relation_type  # e.g., 'friend', 'colleague', 'family'

    def __repr__(self):
        return f"Relationship({self.from_individual.name} -[{self.type}]-> {self.to_individual.name})"


if __name__ == "__main__":
    # Example
    person_a = Individual(1, "Alice", age=30, gender="Female")
    person_b = Individual(2, "Bob", age=35, gender="Male")

    # Define relationship
    friendship = Relationship(person_a, person_b, "friend")

    # Add relationship to individuals
    person_a.add_relationship(friendship)
    person_b.add_relationship(friendship)

    # Print results
    print(person_a)
    print(person_b)
    print(friendship)
