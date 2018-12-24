# UTILS AND FUNCTIONALITY
from data import population, clubs
from components import Club, Person

my_name = "myname"
my_age = 42
my_bio = "im old"
myself = Person(my_name, my_bio, my_age)


def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)


def options():
    # your code goes here!
    print("----------------")
    print("Would you like to:")
    print("1) Create a new club.")
    print("or:")
    print("2) Browse and join clubs.")
    print("or:")
    print("3) View existing clubs.")
    print("or:")
    print("-1) Close application.")


def create_club():
    # your code goes here!
    print("Pick a name for your awesome new club:")
    name = input()
    print("What is your club about?")
    desc = input()
    newClub = Club(name, desc)
    newClub.assign_president(myself)
    print("Enter the number os the people you would like to tawtheef to your new club (-1 to stop):")
    for i in population:
        print("[", population.index(i)+1, "] ", i.name)
    num = input()
    while int(num) != -1:
        newClub.recruit_member(population[int(num)-1])
        num = input()

    clubs.append(newClub)
    newClub.print_member_list()


def view_clubs():
    # your code goes here!
    for i in clubs:
        print("NAME: ", i.name)
        print("Description:", i.description)
        print("MEMBERS: ", len(i.members), "\n")
    print("Enter the name of the club you'd like to join: ")
    x = input()
    for y in clubs:
        if x == y.name:
            y.members.append(myself)
            print(myself.name, " has joined ", y.name)


def view_club_members(club):
    # your code goes here!
    club.print_member_list()


def join_clubs():
    # your code goes here!
    pass


def application():
    introduction()
    # your code goes here!
    view_clubs()
