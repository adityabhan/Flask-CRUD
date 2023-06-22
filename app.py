from flask import request, jsonify
from Student import Student, students_schema, student_schema, app, db
from sqlalchemy import func
from datetime import datetime


@app.route("/")
def hello_world():
    return "<h2>Hello World</h2>"


@app.route("/getAllStudents", methods=["GET"])
def get_all_students():
    print(request.remote_addr)

    students = Student.query.all()
    return students_schema.dump(students)


@app.route("/addNewStudent", methods=["POST"])
def add_new_students():
    student_data = request.get_json()

    response = ""

    try:
        validation = student_schema.load(student_data)
        student = Student(
            name=validation["name"],
            addr=validation["addr"],
            city=validation["city"],
            pin=validation["pin"],
        )

        db.session.add(student)
        db.session.commit()
        print(type(validation))
        print(validation)
        response = "Entry added to database"
    except Exception as exp:
        print("Exception")
        print(exp)
        response = "Not valid schema"

    return jsonify(response)


@app.route("/getStudentsByName", methods=["GET"])
def get_students_by_name():
    name = request.args.get("name")
    students = Student.query.filter(func.lower(Student.name) == func.lower(name))
    # print(students)
    response = students_schema.dump(students)
    if not students:
        response = "No Student data available"

    return response


@app.route("/getStudentById", methods=["GET"])
def get_student_by_id():
    student_id = request.args.get("id")
    if student_id:
        student = db.session.get(Student, student_id)
    if not student:
        student = {"message": "Student not found"}

    return jsonify(student)


@app.route("/getStudentsByEnrollmentDate")
def get_students_by_enrollment_date():
    enrollment_date = request.args.get("enrollment_datetime")
    date_format = "%d-%m-%Y"
    # print(enrollment_date)
    enrollment_date = datetime.strptime(enrollment_date, date_format)
    # print(enrollment_date)
    students = Student.query.filter(Student.enrollment_datetime >= enrollment_date)
    # print(students)
    return students_schema.dump(students)


@app.route("/deleteStudentById", methods=["DELETE"])
def delete_student_by_id():
    student_id = request.form["id"]
    print(student_id)

    response = {"message": "Unable to delete student with id={}".format(student_id)}

    student = db.session.get(Student, student_id)

    if student:
        print("deleting student")
        response["message"] = "Deleted student record."
        db.session.delete(student)
        db.session.commit()
    else:
        response["message"] = "No student found with id={}".format(student_id)

    return jsonify(response)


@app.route("/updateStudentName", methods=["PUT"])
def rename_student():
    student_id = request.form["id"]
    new_name = request.form["newName"].strip()
    if not new_name:
        return jsonify("Invalid Name")
    print(f"new name {new_name}")

    student = db.session.get(Student, student_id)

    response = {}
    if student:
        current_name = student.name
        print(f"current name {current_name}")
        if new_name != current_name:
            student.name = new_name
            student.last_update = func.now()
            db.session.commit()
            response[
                "message"
            ] = f"Record updated! Name changed from {current_name} to {new_name}"

        else:
            response["message"] = "New name is same as the current one!"

    else:
        response["message"] = "No student found with id={}".format(student_id)

    return jsonify(response)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0")
