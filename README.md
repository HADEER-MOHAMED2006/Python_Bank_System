# Python Bank – Account Management System

A simple command-line banking system built with core Python (no external libraries). It lets users register, log in, and manage their account through an interactive menu.

## Features

- **Register** a new account with a username and password
- **Login** with a limited number of attempts (3), with the option to cancel at any point
- **Check Balance**
- **Deposit** money
- **Withdraw** money (with insufficient-balance check)
- **Transfer** money to another registered user
- **Change Password**
- **Change Username**
- **Show Last Transaction**
- **Logout**

## How It Works

The system stores all users in memory using a dictionary, where each username maps to their account details (password, balance, and last transaction).

```
users = {
    "username": {
        "Password": "...",
        "Balance": 0,
        "last_transaction": "..."
    }
}
```

Input validation is handled throughout — empty fields, invalid amounts, duplicate usernames, wrong passwords, and non-existent accounts are all caught with clear error messages.

## Getting Started

### Requirements
- Python 3.x

### Run the program
```bash
python bank_system.py
```

### Example Flow
1. Choose `1` to register a new account
2. Choose `2` to log in
3. Once logged in, pick an option from the bank menu (check balance, deposit, withdraw, transfer, etc.)

## Project Structure

```
bank_system.py   # Main script containing all program logic
```

## Notes & Known Limitations

- Data is stored **in memory only** — all accounts are lost when the program closes (no file/database persistence yet).
- Passwords are stored in **plain text** (no hashing) — this is a learning project, not meant for real-world use.
- After performing one action from the bank menu, the user returns to the main menu instead of staying logged in — planned as a future improvement.

## Roadmap / Possible Improvements

- [ ] Loop the bank menu so users can perform multiple actions per session
- [ ] Persist data using a file (JSON) or database
- [ ] Hash passwords instead of storing them as plain text
- [ ] Add transaction history (not just the last transaction)
- [ ] Refactor into functions/classes as OOP concepts are learned

## Author

Built by Hadeer Mohammed
