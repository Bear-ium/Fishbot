import os, sqlite3

DB_NAME = "users.py"

SQL = [
]

def main():
    if not os.path.isfile(DB_NAME):
        print(f"{DB_NAME} not found in current directory.")
        return

    print(f"Found {DB_NAME}, running SQL...")
    
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        for command in SQL:
            cursor.execute(command)
        conn.commit()
        print("All tables created (if they didn't already exist).")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
