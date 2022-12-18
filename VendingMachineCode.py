print("Welcome to ")
print(" █████╗ ██████╗ ██╗███████╗    ██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗\n██╔══██╗██╔══██╗██║██╔════╝    ██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝\n███████║██████╔╝██║███████╗    ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  \n██╔══██║██╔══██╗██║╚════██║    ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  \n██║  ██║██║  ██║██║███████║     ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗\n╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝")

def money_change(money,item_price): #Function that collects correct amount for the item
    if money < item_price:
        print("The money you inputted is not enough.")
        while money < item_price:
            add = int(input("Input more coins please (type 00 if you want to cancel your purchase): "))
            if add == 00:
                print("Thank you for using Ari's Vending Machine. Please come again.")
                print(f"We have given you your {money} back.")
                break
            else: 
                return money + add
    return money

#Global lists
chosen_items,quantity,prices,change_list,money_list = [],[],[],[],[]

#Vending Machine Code Items
items = {"1A": {"Dorito":6}, "2A":{"Cheetos":5}, "3A":{"Lays":5}, "1B": {"Twix":4}, "2B":{"Bueno":5}, "3B":{"M&M's":3}, "1C": {"Cola":3}, "2C":{"Fanta":3}, "3C":{"Water":1}} #Item
items_stock = {"1A":3,"2A":2,"3A":4,"1B":1,"2B":4,"3B":2,"1C":1,"2C":3,"3C":5} #Stock of items
print("These are the products inside the vending machine:")

while True: #A while loop to loop the program allowing the user to choose multiple products
    #A for loop to organize and print the items in the Vending Machine
    for key, value in items.items(): 
        for it in items[key]:
            it = it
            print(f"ID: {key} \t Item: {it} \tPrice: {items[key][it]} \n")
    ID = input("Select your item by entering the Item ID: ") #An input code to get the chosen item
    if items_stock[ID] == 0: #If the chosen item is out of stock, it redirects to the beginning of the loop
        print("Sorry, but", ID, "is unavailable.\nPlease choose another item.\n")
        continue
    money = int(input("Insert money (You will receive the appropriate change): "))
    for item in items[ID]: #Code getting the price of the item and the item
        item = item
        price_item = items[ID][item]
    money = money_change(money,price_item) #Activates the code checking whether the amount of money given is correct
    change = money - price_item
    items_stock[ID] = items_stock[ID] - 1 #A code that removes one of the stock of the chosen item

    #Appending the finalized items into the following lists so they are saved and prepared for the outputted receipt
    money_list.append(money), change_list.append(change), chosen_items.append(item), prices.append(price_item)
    
    ask = input("Do you wish to get another item (yes or no)? ")
    if ask == "no":
        print()
        break
    else:
        print()
        continue

#The code that will activate once the user is done selecting items:
duplicates_removed_list = [*set(chosen_items)] #A code remaking the list into a sorted and no duplicated item list
for i in duplicates_removed_list: #A for loop used to confirm the quantity of the chosen items
    count = chosen_items.count(i) 
    quantity.append(count)
    print(f"You received your {i}.") #A code message informing the user of the items they received 
print(f"You received your change of {change} AED.") 

#The outputted receipt:
print("Here's your receipt: \n\t---RECEIPT---\n\tITEM\tPRICE\tQTY") 
for item,q,p in zip(duplicates_removed_list,quantity,prices): 
    receipt = print(f"\t{item}\t{p}\t{q}")
print(f"\tINPUTTED MONEY: {sum(money_list)} \n\tCHANGE:{sum(change_list)}")
print("\nThank you for using Ari's Vending Machine! \nEnjoy your snacks!") #End of the program
