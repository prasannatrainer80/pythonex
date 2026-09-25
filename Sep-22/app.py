from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)


# =========================================================
# GENERATE ACCOUNT NUMBER
# =========================================================

def generateAccountNo():

    connection = get_connection()

    cursor = connection.cursor()

    sql = """
        SELECT CASE
        WHEN MAX(AccountNo) IS NULL THEN 1
        ELSE MAX(AccountNo) + 1
        END AS accno
        FROM Accounts
    """

    cursor.execute(sql)

    row = cursor.fetchone()

    cursor.close()

    connection.close()

    return row[0]


# =========================================================
# HOME / DASHBOARD
# =========================================================

@app.route("/")
def index():

    return render_template("index.html")


# =========================================================
# CREATE ACCOUNT
# =========================================================

@app.route("/createAccount", methods=["GET", "POST"])
def createAccount():

    if request.method == "POST":

        # Generate Account Number
        accno = generateAccountNo()

        # Get form values
        name = request.form["name"]
        username = request.form["username"]
        passcode = request.form["passcode"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        amount = request.form["amount"]

        connection = get_connection()

        cursor = connection.cursor()

        sql = """
            INSERT INTO Accounts
            (
                AccountNo,
                AccHolderName,
                UserName,
                Passcode,
                Email,
                MobileNo,
                Amount
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            accno,
            name,
            username,
            passcode,
            email,
            mobile,
            amount
        )

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()

        connection.close()

        return render_template(
            "result.html",
            message="Account Created with Account No " + str(accno)
        )

    return render_template("create_account.html")


# =========================================================
# SEARCH ACCOUNT
# =========================================================

@app.route("/searchAccount", methods=["GET", "POST"])
def searchAccount():

    account = None

    if request.method == "POST":

        accno = request.form["account_no"]

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        sql = """
            SELECT *
            FROM Accounts
            WHERE AccountNo = %s
        """

        cursor.execute(sql, (accno,))

        account = cursor.fetchone()

        cursor.close()

        connection.close()

    return render_template(
        "search_account.html",
        account=account
    )


# =========================================================
# UPDATE ACCOUNT
# =========================================================

@app.route("/updateAccount", methods=["GET", "POST"])
def updateAccount():

    if request.method == "POST":

        accno = request.form["account_no"]

        name = request.form["name"]

        username = request.form["username"]

        passcode = request.form["passcode"]

        email = request.form["email"]

        mobile = request.form["mobile"]

        connection = get_connection()

        cursor = connection.cursor()

        sql = """
            UPDATE Accounts
            SET
                AccHolderName = %s,
                UserName = %s,
                Passcode = %s,
                Email = %s,
                MobileNo = %s
            WHERE AccountNo = %s
        """

        values = (
            name,
            username,
            passcode,
            email,
            mobile,
            accno
        )

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()

        connection.close()

        return render_template(
            "result.html",
            message="Account Updated Successfully"
        )

    return render_template("update_account.html")


# =========================================================
# DEPOSIT ACCOUNT
# =========================================================

@app.route("/depositAccount", methods=["GET", "POST"])
def depositAccount():

    if request.method == "POST":

        accno = request.form["account_no"]

        deposit_amount = request.form["amount"]

        connection = get_connection()

        cursor = connection.cursor()

        # Update balance
        sql = """
            UPDATE Accounts
            SET Amount = Amount + %s
            WHERE AccountNo = %s
        """

        cursor.execute(
            sql,
            (deposit_amount, accno)
        )

        # Insert transaction
        sql = """
            INSERT INTO Trans
            (AccountNo, TranAmount, TranType)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            sql,
            (accno, deposit_amount, "C")
        )

        connection.commit()

        cursor.close()

        connection.close()

        return render_template(
            "result.html",
            message="Amount Credited Successfully"
        )

    return render_template("deposit_account.html")


# =========================================================
# WITHDRAW ACCOUNT
# =========================================================

@app.route("/withdrawAccount", methods=["GET", "POST"])
def withdrawAccount():

    if request.method == "POST":

        accno = request.form["account_no"]

        withdraw_amount = request.form["amount"]

        connection = get_connection()

        cursor = connection.cursor()

        # Check current balance
        sql = """
            SELECT Amount
            FROM Accounts
            WHERE AccountNo = %s
        """

        cursor.execute(sql, (accno,))

        row = cursor.fetchone()

        if row is None:

            cursor.close()

            connection.close()

            return render_template(
                "result.html",
                message="Account Not Found"
            )

        balance = row[0]

        if balance < float(withdraw_amount):

            cursor.close()

            connection.close()

            return render_template(
                "result.html",
                message="Insufficient Balance"
            )

        # Update balance
        sql = """
            UPDATE Accounts
            SET Amount = Amount - %s
            WHERE AccountNo = %s
        """

        cursor.execute(
            sql,
            (withdraw_amount, accno)
        )

        # Insert transaction
        sql = """
            INSERT INTO Trans
            (AccountNo, TranAmount, TranType)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            sql,
            (accno, withdraw_amount, "D")
        )

        connection.commit()

        cursor.close()

        connection.close()

        return render_template(
            "result.html",
            message="Amount Debited Successfully"
        )

    return render_template("withdraw_account.html")


# =========================================================
# CLOSE ACCOUNT
# =========================================================

@app.route("/closeAccount", methods=["GET", "POST"])
def closeAccount():

    if request.method == "POST":

        accno = request.form["account_no"]

        connection = get_connection()

        cursor = connection.cursor()

        # First delete transactions
        sql = """
            DELETE FROM Trans
            WHERE AccountNo = %s
        """

        cursor.execute(sql, (accno,))

        # Then delete account
        sql = """
            DELETE FROM Accounts
            WHERE AccountNo = %s
        """

        cursor.execute(sql, (accno,))

        connection.commit()

        cursor.close()

        connection.close()

        return render_template(
            "result.html",
            message="Account Closed Successfully"
        )

    return render_template("close_account.html")


# =========================================================
# START FLASK APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)