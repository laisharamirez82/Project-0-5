# This program is for the company AutoCountry
# CarFinder v0.5 program

# Vehicle list
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Initialize
def printMenu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")


# Input
printMenu() 
enteredNum = int(input())
while enteredNum >=1 and enteredNum !=5:
    if enteredNum == 1:
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for vehicle in AllowedVehiclesList:
            print(vehicle) 

    elif enteredNum == 2:
        print("********************************")
        vehicleName = input("Please Enter the full vehicle name: ")
        
        if vehicleName in AllowedVehiclesList:
            print(f'{vehicleName} is an authorized vehicle')
        else:
            print(f'{vehicleName} is not an authorized vehicle, if you received this in error please check the spelling and try again.')
    
    elif enteredNum ==3:
        print("********************************")
        addedVehicle = input("Please Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(addedVehicle) 
        print (f'You have added {addedVehicle} as an authorized vehicle')
    
    elif enteredNum ==4: 
        print("********************************")
        removedVehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        print (f'Are you sure you want to remove "{removedVehicle}" from the Authorized Vehicles List?')
        response = input()
        if response == 'yes':
            AllowedVehiclesList.remove(removedVehicle)
            print(f'You have REMOVED "{removedVehicle}" as an authorized vehicle')


    printMenu()
    enteredNum = int(input())

print("Thank you for using the AutoCountry Vehicle Finder, good-bye!") 
    