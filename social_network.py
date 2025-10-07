class Person:
   class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            if person1_name not in self.people:
                print(f"Friendship not created. {person1_name} doesn't exist!")
            if person2_name not in self.people:
                print(f"Friendship not created. {person2_name} doesn't exist!")

    def print_network(self):
        for name, person_obj in self.people.items():
            friend_names = [friend.name for friend in person_obj.friends]
            friends_str = ", ".join(friend_names)
            print(f"{name} is friends with: {friends_str}")


network = SocialNetwork()

alex = Person("Alex")
caden = Person("Caden")
print(alex.friends)
alex.add_friend(caden)
print(alex.friends[0].name)

network.add_person("Alex")
network.add_person("Caden")
network.add_person("Morgan")
network.add_person("Luke")
network.add_person("Nolan")
network.add_person("Jada")

network.add_friendship("Alex", "Caden")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Caden", "Luke")
network.add_friendship("Caden", "Johnny")
network.add_friendship("Morgan", "Nolan")
network.add_friendship("Luke", "Jada")
network.add_friendship("Nolan", "Jada")
network.add_friendship("Morgan", "Jada")
network.add_friendship("Alex", "Luke")

network.print_network()

