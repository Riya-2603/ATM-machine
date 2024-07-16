# ATM Simulation Program

## Overview

This project simulates an ATM machine where users can perform various banking transactions such as checking their account balance, withdrawing cash, depositing cash, changing their PIN, and viewing their transaction history.

## Features

- **Account Balance Inquiry**: Users can check their current account balance.
- **Cash Withdrawal**: Users can withdraw cash from their account.
- **Cash Deposit**: Users can deposit cash into their account.
- **PIN Change**: Users can change their ATM PIN.
- **Transaction History**: Users can view their transaction history.
- **Exit**: Users can exit the ATM session.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Program

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the program using the command:
   ```sh
   python atm_simulation.py
   ```

### Code Walkthrough

1. **Card Insertion Simulation**:
   ```python
   print("Please Insert your Card")
   time.sleep(5)
   ```
   Simulates the card insertion process with a delay of 5 seconds.

2. **Password Initialization**:
   ```python
   password = 6789
   ```

3. **PIN Input and Account Balance Input**:
   ```python
   pin = int(input("Enter PIN Number: "))
   Account_balance = int(input("Enter your Account Balance: "))
   ```

4. **Transaction History Initialization**:
   ```python
   Transaction_history = []
   ```

5. **Main ATM Loop**:
   - Users can choose from multiple options:
     - Check account balance.
     - Withdraw cash.
     - Deposit cash.
     - Change PIN.
     - View transaction history.
     - Exit the ATM session.

6. **Option Handling**:
   - Each option is handled using `if-elif` statements.
   - Transactions are logged in the `Transaction_history` list.

### Contributing

If you have any suggestions or improvements, feel free to submit a pull request.
