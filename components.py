# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []
        self.presedent = Person("dummy", "dummy", 123)

    def assign_president(self, person):
        # your code goes here!
        self.presedent = person

    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)

    def print_member_list(self):
        # your code goes here!
        print("Members:")
        avg = self.presedent.age
        print("- ", self.presedent.name, "(", self.presedent.age,
              "years old, President)", "-", self.presedent.bio)
        for x in self.members:
            print("- ", x.name, "(", x.age, "years old)", "-", x.bio)
            avg = avg + x.age
        avg = avg/(len(self.members)+1)
        print("Average age in this club:", avg, "yr")
