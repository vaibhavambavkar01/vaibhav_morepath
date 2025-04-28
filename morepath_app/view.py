from morepath_app.app import App
from morepath_app.model import Document,User,AddEmployee,Employee,UpdateEmployee

@App.json(model=Document)
def document_default(self, request):
    return {'id': self.id, 'title': self.title, 'content': self.content }


# @App.view(model=User)
# def user_info(self, request):
#     return "User's full name is: %s" % self.fullname


@App.json(model=User)
def user_info(self, request):
    return {"username":self.username,"email":self.email,"fullname":self.fullname}

#
@App.json(model=AddEmployee, request_method='GET')
def add_employee_view(self, request):
    data = request.params  # expects JSON body with eid, ename, edept

    eid = data.get('eid')
    ename = data.get('ename')
    edept = data.get('edept')

    if not eid or not ename or not edept:
        return {"error": "eid, ename, and edept are required"}, 400

    # Create new Employee and add to storage
    new_emp = Employee(eid=eid, ename=ename, edept=edept)
    Employee.add_employee(new_emp)

    return {"message": f"Employee {ename} added successfully."}


@App.json(model=UpdateEmployee, request_method='GET')
def add_employee_view(self, request):
    data = request.params  # expects JSON body with eid, ename, edept

    eid = data.get('eid')
    edept = data.get('edept')

    if not eid or not edept:
        return {"error": "eid, ename, and edept are required"}, 400

    # Create new Employee and add to storage
    Employee.update_employee(eid,edept)

    return {"message": f"Employee {eid} updated successfully."}
