'''
class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)


class Shark:

    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Jimmy", 10)
print(new_shark.name)
print(new_shark.age)



class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0

    def __init__(self, name_p, age_p):
        self.name = name_p
        self.age = age_p

    def set_followers(self, followers_p):
        self. followers = followers_p
        print(f"This user has {self.followers} followers.")

new_shark = Shark("Brutus", 14)
print(new_shark.followers) #0
new_shark.set_followers(5) #This user has 5 followers.
print(new_shark.followers) #5



class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0

    def __init__(self, name_p, age_p):
        self.name = name_p
        self.age = age_p

    def set_name(self, name_p):
        self.name = name_p
        print(f"This user name is {self.name}.")

new_shark = Shark("Rony", 8)
print(new_shark.name) #Rony
new_shark.set_name("Marcos") #This user name is <name>.
print(new_shark.name) #Marcos

'''
class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0

    def __init__(self, name_p, age_p):
        self.name = name_p
        self.age = age_p

    def limpa(self):

        self.animal_type = ""
        self.location = ""
        self.followers = None
        self.age = None
        self.name = ""
        print("tudo foi limpo")

new_shark = Shark("Rony", 8)
new_shark.limpa()
print(new_shark.name)