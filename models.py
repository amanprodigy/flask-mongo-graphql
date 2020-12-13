from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ListField,
    DateTimeField,
    ReferenceField,
    StringField,
    EmbeddedDocumentField,
)


class Department(Document):
    name = StringField(unique=True, required=True)

    meta = {"collection": "department"}

    def __repr__(self):
        return "Department <%s>" % self.name

    def __str__(self):
        return "Department <%s>" % self.name


class Role(Document):
    name = StringField(unique=True, required=True)

    meta = {"collection": "role"}

    def __repr__(self):
        return "Role <%s>" % self.name

    def __str__(self):
        return "Role <%s>" % self.name


class Task(EmbeddedDocument):
    name = StringField()
    deadline = DateTimeField(default=datetime.now)


class Employee(Document):
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department, required=True)
    roles = ListField(ReferenceField(Role))
    leader = ReferenceField("Employee", require=False)
    tasks = ListField(EmbeddedDocumentField(Task))

    meta = {
        "collection": "employee",
        "indexes": [
            {"fields": ["name", "department"], "unique": True},
        ],
    }

    def __repr__(self):
        return "Employee <%s>" % self.name

    def __str__(self):
        return "Employee <%s>" % self.name
