# School Management System

## Project Overview

This is a console-based School Management System developed in Python, utilizing `mysql.connector` to interact with a MySQL database. It provides a menu-driven interface to manage various aspects of a school, including student, employee, fee, and exam details.

## Features

* **Student Management**:
    * New admission (add student details)
    * Update student information (class, city)
    * Issue TC (delete student record)
    * View all student records
* **Employee Management**:
    * Add new employees
    * Update staff details (designation)
    * Delete employee records
    * View all employee records
* **Fee Management**:
    * Add new fee records
    * Update fee details (month)
    * Exempt fee (delete fee record)
    * View all fee records
* **Exam Management**:
    * Add exam details (student name, admission number, percentage, result)
    * Update exam results
    * Delete exam records
    * View all exam details

## Prerequisites

To run this project locally (after downloading the code), you'll need:

* **Python 3.x**: Make sure Python is installed on your system.
* **MySQL Database**: A running MySQL server instance.
* **`mysql.connector`**: The Python library for MySQL interaction. You can install it using pip:
    ```bash
    pip install mysql-connector-python
    ```
* **Database Setup**: You'll need a database named `mysql` (as per your code's connection string) and the following tables with appropriate columns. The `root` user with password `12345` is assumed in the connection.

    * **`student` table:**
        ```sql
        CREATE TABLE student (
            sname VARCHAR(255),
            admno INT PRIMARY KEY,
            dob DATE,
            cls VARCHAR(50),
            cty VARCHAR(100)
        );
        ```
    * **`emp` table:**
        ```sql
        CREATE TABLE emp (
            ename VARCHAR(255),
            empno INT PRIMARY KEY,
            job VARCHAR(100),
            hiredate DATE
        );
        ```
    * **`fee` table:**
        ```sql
        CREATE TABLE fee (
            admno INT PRIMARY KEY,
            fee DECIMAL(10, 2),
            month VARCHAR(50)
        );
        ```
    * **`exam` table:**
        ```sql
        CREATE TABLE exam (
            sname VARCHAR(255),
            admno INT PRIMARY KEY,
            per DECIMAL(5, 2),
            res VARCHAR(50)
        );
        ```
    *(Note: The database used in your code is `mysql`, which is typically the default system database. For production, it's highly recommended to create a dedicated database for your application instead of using the `mysql` system database.)*

## Usage

1.  **Download the project code**: You can download the code directly from this GitHub repository.
2.  **Set up your MySQL database** as described in the "Prerequisites" section.
3.  **Run the Python script**:
    ```bash
    python src/school_management.py
    ```
4.  Follow the on-screen menu prompts to interact with the system.

## Sample Output

Here are some sample interactions and outputs from the system.

---

### Main Menu Interaction
