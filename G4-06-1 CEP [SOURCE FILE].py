import random
import os

class CarRentalSystem:
    def __init__(self):
        self.user_account = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as f:
                for line in f:
                    username, password = line.strip().split(",")
                    self.user_account.append({'username': username, 'password': password})
        self.car_list = [
            {"name": "Suzuki Mehran", "number": "PAK101", "color": "White", "price": 1200},
            {"name": "Suzuki Alto", "number": "PAK102", "color": "Silver", "price": 1500},
            {"name": "Suzuki Cultus", "number": "PAK103", "color": "Gray", "price": 1600},
            {"name": "Suzuki Wagon R", "number": "PAK104", "color": "Blue", "price": 1700},
            {"name": "Toyota Corolla XLI", "number": "PAK105", "color": "White", "price": 2000},
            {"name": "Toyota Corolla GLI", "number": "PAK106", "color": "Black", "price": 2200},
            {"name": "Toyota Yaris", "number": "PAK107", "color": "Red", "price": 2300},
            {"name": "Toyota Fortuner", "number": "PAK108", "color": "Black", "price": 4500},
            {"name": "Toyota Hilux Revo", "number": "PAK109", "color": "Gray", "price": 5000},
            {"name": "Honda Civic", "number": "PAK110", "color": "Silver", "price": 2500},
            {"name": "Honda City", "number": "PAK111", "color": "White", "price": 2200},
            {"name": "Honda BR-V", "number": "PAK112", "color": "Red", "price": 2600},
            {"name": "KIA Sportage", "number": "PAK113", "color": "Blue", "price": 4200},
            {"name": "Hyundai Tucson", "number": "PAK114", "color": "Black", "price": 4300},
            {"name": "Hyundai Elantra", "number": "PAK115", "color": "Gray", "price": 3000},
            {"name": "Changan Alsvin", "number": "PAK116", "color": "White", "price": 2100},
            {"name": "Prince Pearl", "number": "PAK117", "color": "Silver", "price": 1300},
            {"name": "DFSK Glory 580", "number": "PAK118", "color": "Gray", "price": 3500},
            {"name": "Haval Jolion", "number": "PAK119", "color": "Red", "price": 3900},
            {"name": "Haval H6", "number": "PAK120", "color": "White", "price": 4400},
            {"name": "Proton Saga", "number": "PAK121", "color": "Silver", "price": 1800},
            {"name": "Proton X70", "number": "PAK122", "color": "Black", "price": 4100},
            {"name": "MG HS", "number": "PAK123", "color": "Blue", "price": 4600},
            {"name": "MG ZS", "number": "PAK124", "color": "Gray", "price": 4200},
            {"name": "Suzuki Bolan", "number": "PAK125", "color": "White", "price": 1400},
            {"name": "Suzuki Ravi", "number": "PAK126", "color": "White", "price": 1300}
        ]
        self.rented_cars = []

    def main_menu(self):
        while True:
            print("----------------------------------------------------------------------------------------------------------------------------------------------")
            print("WELCOME TO THE CAR RENTAL SYSTEM")
            print("1. REGISTER")
            print("2. LOGIN")
            print("3. EDIT PROFILE")
            print("4. EXIT")
            choice = input("ENTER YOUR CHOICE: ").strip()
            print("\n\n")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.edit_profile()
            elif choice == '4':
                print("THANK YOU FOR USING THE CAR RENTAL SYSTEM. GOODBYE!\n\n")
                break
            else:
                print("INVALID CHOICE. PLEASE TRY AGAIN.\n\n")

    def register(self):
        username = input("ENTER USERNAME: ").strip()
        password = input("ENTER PASSWORD: ").strip()
        for user in self.user_account:
            if user['username'] == username:
                print("USERNAME ALREADY EXISTS.\n\n")
                return
        self.user_account.append({'username': username, 'password': password})
        with open("users.txt", "a") as f:
            f.write(f"{username},{password}\n")
        print("REGISTERED SUCCESSFULLY.\n\n")

    def edit_profile(self):
        username = input("ENTER OLD USERNAME: ").strip()
        password = input("ENTER OLD PASSWORD: ").strip()
        for user in self.user_account:
            if user["username"] == username and user["password"] == password:
                print("ENTER NEW INFORMATION:")
                user["username"] = input("ENTER NEW USERNAME: ").strip()
                user["password"] = input("ENTER NEW PASSWORD: ").strip()
                print("PROFILE UPDATED SUCCESSFULLY.\n\n")
                return
        print("INVALID CREDENTIALS.\n\n")

    def login(self):
        username = input("ENTER USERNAME: ").strip()
        password = input("ENTER PASSWORD: ").strip()
        found = False
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as f:
                for line in f:
                    file_username, file_password = line.strip().split(",")
                    if file_username == username and file_password == password:
                        found = True
                        break
        if found:
            print("LOGIN SUCCESSFUL.\n\n")
            while True:
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
                print("1. RENT A CAR")
                print("2. EXIT")
                choice = input("ENTER YOUR CHOICE: ").strip()
                print("\n\n")
                if choice == '1':
                    self.rent_a_car_flow(username)
                    break
                elif choice == '2':
                    return
                else:
                    print("INVALID CHOICE.\n\n")
        else:
            print("INVALID CREDENTIALS.\n\n")

    def available_cars(self):
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("AVAILABLE CARS:")
        print(f"{'NAME':<25} {'NUMBER':<10} {'COLOR':<10} {'PRICE':<10}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        for car in random.sample(self.car_list, 5):
            print(f"{car['name']:<25} {car['number']:<10} {car['color']:<10} {car['price']:<10}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------\n\n")

    def rent_a_car_flow(self, username):
        print("ENTER YOUR DETAILS (type 'back' at any time to return):")
        location = input("ENTER YOUR LOCATION: ").strip()
        if location.lower() == 'back':
            print("\n\n")
            return
        destination = input("ENTER YOUR DESTINATION: ").strip()
        if destination.lower() == 'back':
            print("\n\n")
            return
        date = input("ENTER THE DATE OF BOOKING: ").strip()
        if date.lower() == 'back':
            print("\n\n")
            return
        time = input("ENTER THE TIME OF BOOKING: ").strip()
        if time.lower() == 'back':
            print("\n\n")
            return

        print("BOOKING DETAILS:")
        print(f"LOCATION: {location}")
        print(f"DESTINATION: {destination}")
        print(f"DATE: {date}")
        print(f"TIME: {time}")
        print("NOW, LET'S SELECT A CAR FOR YOUR BOOKING.\n\n")

        while True:
            self.available_cars()
            print("TYPE 'back' TO RETURN TO MAIN MENU.")
            car_name = input("ENTER THE NAME OF THE CAR YOU WANT TO RENT: ").strip()
            if car_name.lower() == 'back':
                print("\n\n")
                return

            selected_car = None
            for car in self.car_list:
                if car['name'].lower() == car_name.lower():
                    selected_car = car
                    break

            if selected_car:
                print(f"\nYOU HAVE SELECTED: {selected_car['name']} PRICED AT {selected_car['price']} PKR.\n")
                confirm = input("DO YOU WANT TO CONFIRM THIS CAR? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    self.rented_cars.append(selected_car)
                    self.car_list.remove(selected_car)

                    with open("rentals.txt", "a") as f:
                        f.write(f"{username},{selected_car['name']},{selected_car['number']},{selected_car['color']},{selected_car['price']},{location},{destination},{date},{time}\n")

                    print("CAR RENTAL CONFIRMED!\n\n")
                    while True:
                        print("----------------------------------------------------------------------------------------------------------------------------------------------")
                        print("1. VIEW BOOKING DETAILS")
                        print("2. VIEW CAR DETAILS")
                        print("3. EXIT TO MAIN MENU")
                        choice = input("ENTER YOUR CHOICE: ").strip()
                        print("\n\n")

                        if choice == '1':
                            print("BOOKING DETAILS:")
                            print(f"USERNAME: {username}")
                            print(f"LOCATION: {location}")
                            print(f"DESTINATION: {destination}")
                            print(f"DATE: {date}")
                            print(f"TIME: {time}")
                            print(f"CAR NAME: {selected_car['name']}")
                            print(f"CAR NUMBER: {selected_car['number']}")
                            print(f"CAR COLOR: {selected_car['color']}")
                            print(f"CAR PRICE: {selected_car['price']} PKR")
                            print(f"BOOKING ID: {random.randint(1000, 9999)}\n\n")
                        elif choice == '2':
                            print("CAR DETAILS:")
                            print(f"NAME: {selected_car['name']}")
                            print(f"NUMBER: {selected_car['number']}")
                            print(f"COLOR: {selected_car['color']}")
                            print(f"PRICE: {selected_car['price']} PKR\n\n")
                        elif choice == '3':
                            print("\n\n")
                            return
                        else:
                            print("INVALID CHOICE. TRY AGAIN.\n\n")
                    return
                else:
                    print("CHOOSE A DIFFERENT CAR.\n\n")
            else:
                print("CAR NOT FOUND. TRY AGAIN.\n\n")


# Run the program
app = CarRentalSystem()
app.main_menu()
