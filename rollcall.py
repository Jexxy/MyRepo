club_members = ["William Summers", "Amos Gordon", "Sage Getts", "Cameron Medsker", "Cheryl Rossi Hui", "Jackson Kelp", "Sam Stewart", "Holt Hutchins", "Marco Rocha", "Oliva Staggs", "Esme Fernandez", "Jeremy Mckee", "Jesse Wallzs", "Gannon Densford", "Arek Holloway", "Andrew Holloway", "Jon Lofgren", " Davis Tracey", "Kianna Mitchell", "Yvette Meraz", "Cooper Bailey", "Ethan Love"]
attending_members = []

for i in club_members:
    rollcall = input(f"Is {i} Attending today? Y/n: ")
    if rollcall.lower() == "y" or rollcall.lower() == "":
        attending_members.append(f"{i}\n")

with open("rollcall.txt", "w") as file:
    file.writelines(attending_members)
print(attending_members)


yays = []
nays = []
attending_members.strip()
while True:
    vote_prompt = input("Please Input the prompt for the vote: ")
    print(f"Today we are voting on: {vote_prompt}")
    for i in attending_members:
        vote = input(f"{i}, Yay are Nay? Y/n")
        if vote.lower() == "y" or vote.lower() == "":
            yays.append(f"{i}\n")
        elif vote.lower() == "n":
            nays.append(f"{i}\n")
    with open(f"{vote_prompt}.txt", "w") as file:
        file.write("Yays from attending members: \n")
        file.writelines(yays)
        file.write("Nays from attending members: \n")
        file.writelines(nays)
    stop = input("Do you want to vote again? Y/n")
    if stop.lower() == "n":
        break
