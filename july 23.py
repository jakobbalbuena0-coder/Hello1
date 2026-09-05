name = input("What is your name? ")

print("Hello, " + name + ".")

print("Per the Cleveland Clinic, you should eat 2400 calories each day.")


caloriesToday = int(input("How many calories have you eaten so far today? "))

#caloriesToday = int(caloriesToday)
caloriesRemaining = 2400 - caloriesToday

print("You can eat another" , caloriesRemaining , "calories today. ")

print(name, type(name))
print(caloriesToday, type(caloriesToday))

players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
}

print(players)
print(type(players))
print(players['Lionel Messi'])
print(type(players['Lionel Messi']))