import mysql.connector
from mysql.connector import Error

# --- Database Connection Parameters (for better management) ---
DB_CONFIG = {
    'host': 'localhost',
    'database': 'mysql', # Consider creating a dedicated database like 'school_db'
    'user': 'root',
    'password': '12345' # NEVER hardcode passwords in a real application! Use environment variables or config files.
}

def get_db_connection():
    """Establishes and returns a database connection and cursor."""
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        if connection and connection.is_connected():
            connection.close() # Close connection if it was opened but cursor creation failed
        return None, None

def close_db_connection(connection, cursor):
    """Closes the database cursor and connection if they are open."""
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
    # print("MySQL connection is closed") # Uncomment for debugging

def selection():
    while True:
        print('----------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n-----------------------------------')
        print("1. STUDENT MANAGEMENT")
        print("2. EMPLOYEE MANAGEMENT")
        print("3. FEE MANAGEMENT")
        print("4. EXAM MANAGEMENT")
        print("5. EXIT")

        try:
            ch = int(input("\nEnter your choice (1-5) : "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if ch == 1:
            while True:
                print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
                print('a. NEW ADMISSION')
                print('b. UPDATE STUDENT DETAILS')
                print('c. ISSUE TC')
                print('d. VIEW ALL STUDENTS')
                print('e. BACK TO MAIN MENU')
                c = input("Enter your choice (a-e) : ").lower() # Convert to lowercase for consistent checking

                if c == 'a':
                    print('\nInitially the details are..\n')
                    display_students()
                    insert_student()
                    print('\nModified details are..\n')
                    display_students()
                elif c == 'b':
                    print('\nInitially the details are..\n')
                    display_students()
                    update_student()
                    print('\nModified details are..\n')
                    display_students()
                elif c == 'c':
                    print('\nInitially the details are..\n')
                    display_students()
                    delete_student()
                    print('\nModified details are..\n')
                    display_students()
                elif c == 'd':
                    display_students()
                elif c == 'e':
                    break
                else:
                    print('Enter correct choice...!!')

        elif ch == 2:
            while True:
                print('\nWELCOME TO EMPLOYEE MANAGEMENT SYSTEM\n')
                print('a. NEW EMPLOYEE')
                print('b. UPDATE STAFF DETAILS')
                print('c. DELETE EMPLOYEE')
                print('d. VIEW EMPLOYEE')
                print('e. BACK TO MAIN MENU')

                c = input("Enter your choice (a-e) : ").lower()
                if c == 'a':
                    insert_employee()
                    print('\nModified details are..\n')
                    display_employees()
                elif c == 'b':
                    update_employee()
                    print('\nModified details are..\n')
                    display_employees()
                elif c == 'c':
                    delete_employee()
                    print('\nModified details are..\n')
                    display_employees()
                elif c == 'd':
                    display_employees()
                elif c == 'e':
                    break
                else:
                    print('Enter correct choice...!!')
        elif ch == 3:
            while True:
                print('\nWELCOME TO FEE MANAGEMENT SYSTEM\n')
                print('a. NEW FEE')
                print('b. UPDATE FEE')
                print('c. EXEMPT FEE')
                print('d. VIEW FEES')
                print('e. BACK TO MAIN MENU')

                c = input("Enter your choice (a-e) : ").lower()
                if c == 'a':
                    insert_fee()
                    print('\nModified details are..\n')
                    display_fees()
                elif c == 'b':
                    update_fee()
                    print('\nModified details are..\n')
                    display_fees()
                elif c == 'c':
                    delete_fee()
                    print('\nModified details are..\n')
                    display_fees()
                elif c == 'd':
                    display_fees()
                elif c == 'e':
                    break
                else:
                    print('Enter correct choice...!!')
        elif ch == 4:
            while True:
                print('\nWELCOME TO EXAM MANAGEMENT SYSTEM\n')
                print('a. EXAM DETAILS')
                print('b. UPDATE DETAILS ')
                print('c. DELETE DETAILS')
                print('d. VIEW EXAM DETAILS')
                print('e. BACK TO MAIN MENU')

                c = input("Enter your choice (a-e) : ").lower()
                if c == 'a':
                    insert_exam()
                    print('\nModified details are..\n')
                    display_exams()
                elif c == 'b':
                    update_exam()
                    print('\nModified details are..\n')
                    display_exams()
                elif c == 'c':
                    delete_exam()
                    print('\nModified details are..\n')
                    display_exams()
                elif c == 'd':
                    display_exams()
                elif c == 'e':
                    break
                else:
                    print('Enter correct choice...!!')
        elif ch == 5:
            print("Exiting School Management System. Goodbye!")
            break
        else:
            print('Enter correct choice (1-5)...!!')

# --- STUDENT DETAILS CRUD OPERATION ---
def insert_student():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        sname = input("Enter Student Name : ")
        admno = int(input("Enter Admission No : "))
        dob = input("Enter Date of Birth (yyyy-mm-dd): ")
        cls = input("Enter Class for admission: ")
        cty = input("Enter City : ")

        sql = "INSERT INTO student(sname, admno, dob, cls, cty) VALUES (%s, %s, %s, %s, %s)"
        # Use a tuple for parameters for parameterized queries
        data = (sname, admno, dob, cls, cty)
        cursor.execute(sql, data)
        connection.commit()
        print('Data inserted successfully.')

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number and DOB is in correct format.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error inserting student data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def update_student():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Admission No To Update: "))
        cls = input("Enter New Class: ")
        cty = input("Enter new City: ")

        sql = "UPDATE student SET cls=%s, cty=%s WHERE admno=%s"
        data = (cls, cty, admno)
        cursor.execute(sql, data)
        connection.commit()
        if cursor.rowcount > 0:
            print("\nStudent details updated successfully.")
        else:
            print("\nNo student found with that Admission No.")

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error updating student data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def delete_student():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Admission No To Delete: "))
        ans = input(f"Are you sure you want to delete the record for Admission No {admno}? (y/n) : ").lower()

        if ans == 'y':
            sql = "DELETE FROM student WHERE admno=%s"
            cursor.execute(sql, (admno,)) # Note the comma for a single-element tuple
            connection.commit()
            if cursor.rowcount > 0:
                print("Record deleted successfully.")
            else:
                print("No student found with that Admission No.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error deleting student data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def display_students():
    print("\n--- STUDENT DETAILS ---")
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        sql = "SELECT sname, admno, dob, cls, cty FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()

        if not results:
            print("No student records found.")
            return

        print(f"{'Name':<20} {'Adm No':<10} {'DOB':<12} {'Class':<10} {'City':<15}")
        print("-" * 67)
        for sname, admno, dob, cls, cty in results:
            print(f"{sname:<20} {admno:<10} {str(dob):<12} {cls:<10} {cty:<15}")
        print("-" * 67)

    except Error as e:
        print(f"Error fetching student data: {e}")
    finally:
        close_db_connection(connection, cursor)

# --- EMPLOYEE DETAILS CRUD OPERATION ---
def insert_employee():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        ename = input("Enter Employee Name : ")
        empno = int(input("Enter Employee No : "))
        job = input("Enter Designation: ")
        hiredate = input("Enter date of joining (yyyy-mm-dd): ")

        sql = "INSERT INTO emp(ename, empno, job, hiredate) VALUES (%s, %s, %s, %s)"
        data = (ename, empno, job, hiredate)
        cursor.execute(sql, data)
        connection.commit()
        print('Employee data inserted successfully.')

    except ValueError:
        print("Invalid input. Please ensure Employee No is a number and hiredate is in correct format.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error inserting employee data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def update_employee():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        empno = int(input("Enter Employee No To Update: "))
        job = input("Enter New Designation: ")

        sql = "UPDATE emp SET job=%s WHERE empno=%s"
        data = (job, empno)
        cursor.execute(sql, data)
        connection.commit()
        if cursor.rowcount > 0:
            print("\nEmployee details updated successfully.")
        else:
            print("\nNo employee found with that Employee No.")

    except ValueError:
        print("Invalid input. Please ensure Employee No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error updating employee data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def delete_employee():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        empno = int(input("Enter Employee No To Delete: "))
        ans = input(f"Are you sure you want to delete the record for Employee No {empno}? (y/n) : ").lower()

        if ans == 'y':
            sql = "DELETE FROM emp WHERE empno=%s"
            cursor.execute(sql, (empno,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Record deleted successfully.")
            else:
                print("No employee found with that Employee No.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input. Please ensure Employee No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error deleting employee data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def display_employees():
    print("\n--- EMPLOYEE DETAILS ---")
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        sql = "SELECT empno, ename, job, hiredate FROM emp"
        cursor.execute(sql)
        results = cursor.fetchall()

        if not results:
            print("No employee records found.")
            return

        print(f"{'Emp No':<10} {'Name':<20} {'Designation':<15} {'Hire Date':<12}")
        print("-" * 60)
        for empno, ename, job, hiredate in results:
            print(f"{empno:<10} {ename:<20} {job:<15} {str(hiredate):<12}")
        print("-" * 60)

    except Error as e:
        print(f"Error fetching employee data: {e}")
    finally:
        close_db_connection(connection, cursor)

# --- FEES DETAILS CRUD OPERATION ---
def insert_fee():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Student Admission No : "))
        fee = float(input("Enter fee amount : "))
        month = input("Enter Month : ")

        sql = "INSERT INTO fee(admno, fee, month) VALUES (%s, %s, %s)"
        data = (admno, fee, month)
        cursor.execute(sql, data)
        connection.commit()
        print('Fee data inserted successfully.')

    except ValueError:
        print("Invalid input. Please ensure Admission No and Fee are numbers.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error inserting fee data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def update_fee():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Admission No to Update Fee: "))
        month = input("Enter New Month for Fee: ")

        sql = "UPDATE fee SET month=%s WHERE admno=%s"
        data = (month, admno)
        cursor.execute(sql, data)
        connection.commit()
        if cursor.rowcount > 0:
            print("\nFee details updated successfully.")
        else:
            print("\nNo fee record found for that Admission No.")

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error updating fee data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def delete_fee():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Admission No To Delete Fee Record: "))
        ans = input(f"Are you sure you want to delete the fee record for Admission No {admno}? (y/n) : ").lower()

        if ans == 'y':
            sql = "DELETE FROM fee WHERE admno=%s"
            cursor.execute(sql, (admno,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Fee record deleted successfully.")
            else:
                print("No fee record found for that Admission No.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error deleting fee data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def display_fees():
    print("\n--- FEES DETAILS ---")
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        sql = "SELECT admno, fee, month FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()

        if not results:
            print("No fee records found.")
            return

        print(f"{'Adm No':<10} {'Fee Amount':<12} {'Month':<10}")
        print("-" * 35)
        for admno, fee, month in results:
            print(f"{admno:<10} {fee:<12.2f} {month:<10}") # .2f for float formatting
        print("-" * 35)

    except Error as e:
        print(f"Error fetching fee data: {e}")
    finally:
        close_db_connection(connection, cursor)

# --- EXAM DETAILS CRUD OPERATION ---
def insert_exam():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        sname = input("Enter Student Name : ")
        admno = int(input("Enter Admission No : "))
        per = float(input("Enter percentage : "))
        res = input("Enter result (e.g., Pass/Fail): ")

        sql = "INSERT INTO exam(sname, admno, per, res) VALUES (%s, %s, %s, %s)"
        data = (sname, admno, per, res)
        cursor.execute(sql, data)
        connection.commit()
        print('Exam data inserted successfully.')

    except ValueError:
        print("Invalid input. Please ensure Admission No and Percentage are numbers.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error inserting exam data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def update_exam():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Admission No to Update Exam Record: "))
        result = input("Enter new result (e.g., Pass/Fail) : ")

        sql = "UPDATE exam SET res=%s WHERE admno=%s"
        data = (result, admno)
        cursor.execute(sql, data)
        connection.commit()
        if cursor.rowcount > 0:
            print("\nExam details updated successfully.")
        else:
            print("\nNo exam record found for that Admission No.")

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error updating exam data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def delete_exam():
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        admno = int(input("Enter Admission No To Delete Exam Record: "))
        ans = input(f"Are you sure you want to delete the exam record for Admission No {admno}? (y/n) : ").lower()

        if ans == 'y':
            sql = "DELETE FROM exam WHERE admno=%s"
            cursor.execute(sql, (admno,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Exam record deleted successfully.")
            else:
                print("No exam record found for that Admission No.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input. Please ensure Admission No is a number.")
        if connection: connection.rollback()
    except Error as e:
        print(f"Error deleting exam data: {e}")
        if connection: connection.rollback()
    finally:
        close_db_connection(connection, cursor)

def display_exams():
    print("\n--- EXAM DETAILS ---")
    connection, cursor = get_db_connection()
    if not connection: return

    try:
        sql = "SELECT sname, admno, per, res FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()

        if not results:
            print("No exam records found.")
            return

        print(f"{'Student Name':<20} {'Adm No':<10} {'Percentage':<12} {'Result':<10}")
        print("-" * 55)
        for sname, admno, per, res in results:
            print(f"{sname:<20} {admno:<10} {per:<12.2f} {res:<10}")
        print("-" * 55)

    except Error as e:
        print(f"Error fetching exam data: {e}")
    finally:
        close_db_connection(connection, cursor)

if __name__ == '__main__':
    selection()
