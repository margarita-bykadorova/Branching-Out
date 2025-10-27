# Branching-Out
**Branching Out project for Masterschool**

## User Filter Script 🧑‍💻

A simple Python script that loads users from a JSON file and lets you filter them by **name**, **age**, or **email**.

## 📦 Requirements
- Python 3.10+
- A `users.json` file in the same directory.

Example `users.json`:
```json
[
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
```

## 🚀 Usage
Run the script in your terminal:
```bash
python main.py
```

Then choose a filter option:
- `name` → Filter by user name
- `age` → Filter by age
- `email` → Filter by email

## 🧪 Example
```
What would you like to filter by? name
Enter a name to filter users: Alice
{'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}
```

## 🧰 Project Structure
```
.
├── main.py
├── users.json
└── README.md
```

## 📝 Notes
- Matching by name and email is **case-insensitive**.
- If no users are found, a message will be displayed.
