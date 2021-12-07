
from db.run_sql import run_sql
from models.fittness_class import FitnessClass

#CRUD FUNCTIONALITY - CREATE, READ, UPDATE, DELTE

#CREATE
def save(fitness_class):
    sql = "INSERT INTO fitness_classes (name, capacity, start_time, duration, day, active) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [fitness_class.name, fitness_class.capacity, fitness_class.start_time, fitness_class.duration, fitness_class.day, fitness_class.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    fitness_class.id = id
    return fitness_class


#READ
def select(id):
    fitness_class = None
    sql = "SELECT * FROM fitness_classes WHERE id = %s"
    values = [id]
    result= run_sql(sql, values)[0]
    if result is not None:
        fitness_class = FitnessClass(result['name'],
        result['capacity'], result['start_time'], result['duration'], result['day'],result['active'], result['id'])
    return fitness_class

def select_all():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)
    for row in results:
        fitness_class = FitnessClass(row['name'], row['capacity'], row['start_time'], row['duration'], row['day'], row['active'], row['id'])
        fitness_classes.append(fitness_class)
    return fitness_classes


#UPDATE
def update(fitness_class):
    sql = "UPDATE fitness_classes SET (name, capacity, duration, day, active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [fitness_class.name, fitness_class.capacity, fitness_class.start_time, fitness_class.duration, fitness_class.day, fitness_class.active, fitness_class.id]
    run_sql(sql,values)


#DELETE
def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete_class(id):
    sql = "DELETE FROM fitness_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def fitness_classes(member):
    fitness_classes = []

    sql = "SELECT fitness_classes.* FROM fitness_classes INNER JOIN bookings ON bookings.fitness_class_id = fitness-classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        fitness_class = FitnessClass(row["name"], row["capacity"], row["start_time"], row["duration"], row["day"], row["active"], row["id"])
        fitness_classes.append(fitness_class)
    return fitness_classes