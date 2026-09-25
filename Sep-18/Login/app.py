from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

# Secret key for session
app.secret_key = "jbiet"


# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # Change to your MySQL password
        database="crt"
    )


# =========================
# LOGIN PAGE
# =========================

@app.route("/")
def login_page():

    # Default page is login.html
    return render_template("login.html")


# =========================
# LOGIN VALIDATION
# =========================

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT * FROM login
    WHERE username=%s AND password=%s
    """

    cursor.execute(sql, (username, password))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:

        # Store username in session
        session["username"] = username

        # Login success → Employee page
        return redirect(url_for("employshow"))

    else:

        return render_template(
            "login.html",
            error="Invalid username or password"
        )


# =========================
# EMPLOYEE SHOW PAGE
# =========================

@app.route("/employshow")
def employshow():

    # Check whether user is logged in
    if "username" not in session:
        return redirect(url_for("login_page"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Employ ORDER BY Empno")

    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "employshow.html",
        employees=employees,
        username=session["username"]
    )


# =========================
# ADD EMPLOYEE
# =========================

@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if "username" not in session:
        return redirect(url_for("login_page"))

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

        cursor.execute(
            sql,
            (empno, name, gender, dept, desig, basic)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("employshow"))

    return render_template("add.html")


# =========================
# EDIT EMPLOYEE
# =========================

@app.route("/edit/<int:empno>", methods=["GET", "POST"])
def edit_employee(empno):

    if "username" not in session:
        return redirect(url_for("login_page"))

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

        cursor.execute(
            sql,
            (name, gender, dept, desig, basic, empno)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("employshow"))

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


# =========================
# DELETE EMPLOYEE
# =========================

@app.route("/delete/<int:empno>", methods=["POST"])
def delete_employee(empno):

    if "username" not in session:
        return redirect(url_for("login_page"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Employ WHERE Empno=%s",
        (empno,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("employshow"))


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(debug=True)