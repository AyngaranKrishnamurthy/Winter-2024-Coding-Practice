#Context managers allow you to allocate and release resources precisely when you want to.
#The most widely used example of context managers is the with statement.
#Just by defining __enter__ and __exit__ methods we can use our new class in a with statement

class DatabaseConnection(object):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        # Simulate opening a database connection
        print(f"Connecting to database {self.database} at {self.host} as {self.user}...")
        self.connection = f"Connected to {self.database} at {self.host}"
        return self.connection

    def __exit__(self, type, value, traceback):
        # Simulate closing the database connection
        print("Closing the database connection...")
        self.connection = None

# Using the context manager
with DatabaseConnection('localhost', 'admin', 'password123', 'my_database') as db_conn:
    print(db_conn)

# Explanation:
# The __enter__ method simulates the process of opening a database connection.
# The __exit__ method simulates closing the connection when the block is exited, even if an exception occurs.
# The with statement allows you to automatically manage the setup and teardown of resources (in this case, a database connection).
# This is analogous to your file handling example but adapted for a simulated database connection!



