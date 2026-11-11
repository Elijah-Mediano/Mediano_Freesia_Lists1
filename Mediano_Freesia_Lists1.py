#Input list

oglist = input("Input list in this way: (Item1, Item2, Item3, Item4, Item5): ")
list = oglist.split(",")

print("")

#Replace item

while True:
    choice1 = input("Do you want to replace an item? Yes or No? ")
    
    while choice1 != "Yes" and choice1 != "No":
        choice1 = input("I said 'Yes' or 'No'! ")
        
    if choice1 == "No":
        break
    elif choice1 == "Yes":
        replacenum = int(input("Which number item in the list do you want to replace? Note: If you want to replace ItemX, type X-1, not X. "))
        replacestr = input("What do you want to replace the item with? ")
        list[replacenum] = replacestr
        print(f"The updated list is {list}")

print("")

#Slice list

while True:
    choice2 = input("Do you want to slice the list for no apparent reason? Yes or No? ")
    
    while choice2 != "Yes" and choice2 != "No":
        choice2 = input("I said 'Yes' or 'No'! ")

    if choice2 == "No":
        break
    elif choice2 == "Yes":
        slice1 = int(input("Which number item do you want the sliced list to start with? Note: If you want it to start with Item#, type X-1, not X. "))
        slice2 = int(input("Which number item do you want the sliced list to end with? Note: If you want it to end with Item#, type X-1, not X. "))
        list = list[slice1:slice2 + 1]
        print(f"The updated list is {list}.")

print("")

#Search result

while True:
    choice3 = input("Do you want to check if something is in the current list? Yes or No? ")

    while choice3 != "Yes" and choice3 != "No":
        choice3 = input("I said 'Yes' or 'No'! ")

    if choice3 == "No":
        break
    elif choice3 == "Yes":
        searchup = input("What do you want to check if it's in the list? ")

    if searchup in list:
        print(f"{searchup} is in the current list!")
    else:
        print(f"{searchup} is not in the current list!")

print("")
        

#The illusion of choice

choicefalse = input("Are you done? Yes or No? ")

if choicefalse == "Yes":
    print(f"Alright! The final list is {list}")
elif choicefalse == "No":
    print(f"Too bad. The final list is {list}")
else:
    print(f"I can't tell what you're saying. The final list is {list}")