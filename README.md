# Database-Query-Manager
---

# Python MySQL Connector

This program connects Python to a MySQL database and allows users to run various types of SQL queries on a local database server. It handles all basic CRUD operations like `INSERT`, `DELETE`, `DROP`, `SELECT`, `SHOW`, and `CREATE`, while also managing error handling to ensure the code is robust and efficient.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete data in the database.
- **Error Logging**: Logs errors and important messages into a `bug.log_db` file for debugging purposes.
- **Secure Password Input**: Passwords are entered securely via the terminal.
- **Multiple Query Execution**: Supports running multiple queries in a session.
- **User-friendly**: Provides options for executing different types of queries through a command-line interface.

## Technologies Used
- Python 3.x
- MySQL
- MySQL Connector/Python
- Logging module for error handling

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Server
- `mysql-connector-python` library

To install the MySQL connector for Python, run:
```bash
pip install mysql-connector-python
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```

3. Run the program:
   ```bash
   python your_program_name.py
   ```

## Usage

1. When the program starts, you'll be prompted to enter:
   - **Host**: The name of the host (e.g., `localhost`).
   - **User**: Your MySQL username.
   - **Password**: Your MySQL password (entered securely).
   - **Database**: The name of the database you want to work with.

2. After successfully connecting to the database, you will be presented with options:
   - **Option 1**: Perform queries like `CREATE`, `DROP`, `DELETE`, `INSERT`, `GRANT`, and `REVOKE`.
   - **Option 2**: Perform read operations like `SELECT`, `SHOW`, and view table content.
   - **Option 3**: Log into a different user.
   - **Option 4**: Exit the program.

3. After executing a query, you'll be asked if you want to perform another query or exit.

### Example Commands
- To create a new table:
  ```sql
  CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), position VARCHAR(255));
  ```

- To insert data:
  ```sql
  INSERT INTO employees (name, position) VALUES ('John Doe', 'Manager');
  ```

- To view data:
  ```sql
  SELECT * FROM employees;
  ```

## Logging

All errors and important messages are logged into the `bug.log_db` file. This helps track what went wrong during query execution and assists in debugging.

## Project Structure

```bash
|-- your_program_name.py
|-- bug.log_db         # Log file for errors
|-- README.md
```

## License
This project is licensed under the MIT License. Feel free to modify and use it in your projects.

## Contact
For any questions or contributions, please reach out to me at:
- **Email**: bireelvis@gmail.com
- **GitHub**: [Elviskolbire](https://github.com/Elviskolbire)




