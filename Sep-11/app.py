from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)


@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO employees
            (name, email, department, salary)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (name, email, department, salary))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        sql = """
            UPDATE employees
            SET name=%s,
                email=%s,
                department=%s,
                salary=%s
            WHERE id=%s
        """

        cursor.execute(
            sql,
            (name, email, department, salary, id)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("index"))

    cursor.execute(
        "SELECT * FROM employees WHERE id=%s",
        (id,)
    )

    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template(
        "edit.html",
        employee=employee
    )


@app.route("/delete/<int:id>")
def delete_employee(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)