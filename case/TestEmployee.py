import requests
import unittest
import app
import json
from api.EmployeeAPI import EmployeeCRUD
from parameterized import parameterized


def read_emp_json():
    data = []
    with open(app.BASE_PATH + "/data/employee_add.json", "r", encoding="utf-8") as f:
        test_data = json.load(f)
        for value in test_data.values():
            username = value.get("username")
            mobile = value.get("mobile")
            timeOfEntry = value.get("timeOfEntry")
            formOfEmployment = value.get("formOfEmployment")
            workNumber = value.get("workNumber")
            departmentName = value.get("departmentName")
            departmentId = value.get("departmentId")
            correctionTime = value.get("correctionTime")
            data.append((username, mobile, timeOfEntry, formOfEmployment, workNumber,
                         departmentName, departmentId, correctionTime))
    return data


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmployeeCRUD()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(read_emp_json())
    def test_add(self, username, mobile, timeOfEntry, formOfEmployment,
                 workNumber, departmentName, departmentId, correctionTime):
        response = self.emp_obj.emp_add(self.session, username, mobile, timeOfEntry, formOfEmployment,
                                        workNumber, departmentName, departmentId, correctionTime)
        app.ID = (response.json().get("data")).get("id")
        print("添加员工的响应结果:", response.json())

    def test_update(self):
        response = self.emp_obj.emp_update(self.session, "玫瑰的凋落")
        print("修改员工的响应结果:", response.json())

    def test_get(self):
        response = self.emp_obj.emp_get(self.session)
        print("查询员工的响应结果:", response.json())

    def test_delete(self):
        response = self.emp_obj.emp_delete(self.session)
        print("删除员工的响应结果:", response.json())
