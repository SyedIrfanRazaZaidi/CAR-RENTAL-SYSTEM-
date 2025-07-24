# Car Rental System

This Python project implements a **Car Rental System** with features such as user registration, login, profile editing, and car booking. The system uses a simple text-based interface and stores data in plain text files for persistent storage.

## Features

- **User Registration**: New users can register with a username and password.
- **Login System**: Existing users can log in to access car rental services.
- **Profile Editing**: Logged-in users can update their username and password.
- **Car Rental**:
  - Enter location, destination, date, and time.
  - View a random selection of available cars.
  - Select a car to rent and confirm the booking.
  - View detailed booking and car information after confirmation.
- **Data Persistence**:
  - User accounts are stored in `users.txt`.
  - Rental bookings are saved in `rentals.txt`.

## How It Works

1. **Main Menu Options**:
   - Register a new user
   - Log in as an existing user
   - Edit user profile
   - Exit the program

2. **Booking Process**:
   - Enter trip details (location, destination, date, time).
   - Choose a car from a randomly displayed list of 5 available vehicles.
   - Confirm the rental to save the booking.

3. **Post Booking Options**:
   - View booking details
   - View car details
   - Return to main menu

## Files Used

- `G4-06_CEP.py`: Main Python script that runs the car rental application.
- `users.txt`: Stores registered user credentials in the format: `username,password`.
- `rentals.txt`: Stores rental records in the format:  
  `username,car_name,car_number,car_color,car_price,location,destination,date,time`.

## Example Cars Available

- Suzuki Mehran, Toyota Corolla, Honda Civic, KIA Sportage, MG HS, etc.
- Each car has attributes: name, number, color, and rental price.

## Technologies Used

- Python Standard Library:
  - `random` — for displaying random car options.
  - `os` — to check file existence and handle user data files.

## Booking Sample Format

```
Username: johndoe
Location: Karachi
Destination: Lahore
Date: 2025-06-01
Time: 10:00 AM
Car Name: Toyota Corolla XLI
Car Number: PAK105
Color: White
Price: 2000 PKR
Booking ID: 3257
```

## Notes

- Input is case-insensitive for car selection and menu options.
- Users can type `back` anytime during booking to return to the main menu.
- Duplicate usernames are not allowed during registration.

## License

This project is created for educational purposes and can be freely used and modified.
