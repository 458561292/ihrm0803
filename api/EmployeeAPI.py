import app


class EmployeeCRUD:
    def __init__(self):
        self.emp_url = app.BASE_URL + "user"

    def emp_add(self, session, username, mobile, timeOfEntry, formOfEmployment, workNumber, departmentName,
                departmentId, correctionTime):
        myempJson = {"username": username,
                     "mobile": mobile,
                     "timeOfEntry": timeOfEntry,
                     "formOfEmployment": formOfEmployment,
                     "workNumber": workNumber,
                     "departmentName": departmentName,
                     "departmentId": departmentId,
                     "correctionTime": correctionTime}
        return session.post(self.emp_url, json=myempJson, headers={"Authorization": "Bearer " + app.TOKEN})

    def emp_update(self, session, username):
        return session.put(self.emp_url + "/" + app.ID, json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def emp_get(self, session):
        return session.get(self.emp_url + "/" + app.ID, headers={"Authorization": "Bearer " + app.TOKEN})

    def emp_delete(self, session):
        return session.delete(self.emp_url + "/" + app.ID, headers={"Authorization": "Bearer " + app.TOKEN})
