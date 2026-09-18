from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # Change to your MySQL password
        database="crt"
    )


# READ - Display all employees
@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Employ ORDER BY Empno")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", employees=employees)


# CREATE - Add employee
@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        empno = request.form["empno"]
        name = request.form["name"]
        gender = request.form["gender"]
        dept = request.form["dept"]
        desig = request.form["desig"]
        basic = request.form["basic"]

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO Employ
        (Empno, Name, Gender, Dept, Desig, Basic)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (empno, name, gender, dept, desig, basic)

        try:
            cursor.execute(sql, values)
            conn.commit()
        except mysql.connector.Error as err:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"Error: {err}", 400

        cursor.close()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


# UPDATE - Edit employee
@app.route("/edit/<int:empno>", methods=["GET", "POST"])
def edit_employee(empno):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"]
        gender = request.form["gender"]
        dept = request.form["dept"]
        desig = request.form["desig"]
        basic = request.form["basic"]

        sql = """
        UPDATE Employ
        SET Name=%s,
            Gender=%s,
            Dept=%s,
            Desig=%s,
            Basic=%s
        WHERE Empno=%s
        """

        values = (
            name,
            gender,
            dept,
            desig,
            basic,
            empno
        )

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("index"))

    cursor.execute(
        "SELECT * FROM Employ WHERE Empno=%s",
        (empno,)
    )

    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    if employee is None:
        return "Employee not found", 404

    return render_template(
        "edit.html",
        employee=employee
    )


# DELETE - Delete employee
@app.route("/delete/<int:empno>", methods=["POST"])
def delete_employee(empno):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Employ WHERE Empno=%s",
        (empno,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)