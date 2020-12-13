from mongoengine import connect
from mongoengine.errors import NotUniqueError, ValidationError
from models import Department, Employee, Role, Task

connect("graphene-mongo-example")


def init_db():
    Department.objects(name="Engineering").update_one(
        set__name="Engineering", upsert=True
    )
    engineering = Department.objects.get(name="Engineering")
    print(engineering)

    Department.objects(name="Human Resources").update_one(
        set__name="Human Resources", upsert=True
    )
    hr = Department.objects.get(name="Human Resources")
    print(hr)

    Role.objects(name="manager").update_one(set__name="manager", upsert=True)
    manager = Role.objects.get(name="manager")
    print(manager)

    engineer = Role.objects(name="engineer").update_one(
        set__name="engineer", upsert=True
    )
    engineer = Role.objects.get(name="engineer")
    print(engineer)

    task1 = Task(name="Build apps")
    # task1.save()
    task2 = Task(name="Graphql tutorials")
    # task2.save()
    task3 = Task(name="Mongodb tutorials")
    # task3.save()
    task4 = Task(name="Graphql Relay")
    # task4.save()

    aman = Employee(
        name="Aman",
        department=engineering,
        roles=[engineer],
        tasks=[task2, task3, task4],
    )
    richa = Employee(
        name="Richa",
        department=engineering,
        roles=[engineer],
        leader=aman,
        tasks=[task1, task2],
    )
    rian = Employee(name="Rian", department=hr, roles=[manager], tasks=[task2, task3])
    try:
        aman.save()
        richa.save()
        rian.save()
    except NotUniqueError:
        pass
    except ValidationError:
        pass
