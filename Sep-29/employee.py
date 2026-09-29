from database import db


class Employee(db.Model):

    __tablename__ = "Employ"

    empno = db.Column(
        "Empno",
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        "Name",
        db.String(30),
        nullable=False
    )

    gender = db.Column(
        "Gender",
        db.Enum("MALE", "FEMALE")
    )

    dept = db.Column(
        "Dept",
        db.String(30)
    )

    desig = db.Column(
        "Desig",
        db.String(30)
    )

    basic = db.Column(
        "Basic",
        db.Numeric(9, 2)
    )

    def to_dict(self):

        return {
            "empno": self.empno,
            "name": self.name,
            "gender": self.gender,
            "dept": self.dept,
            "desig": self.desig,
            "basic": float(self.basic)
            if self.basic is not None else None
        }