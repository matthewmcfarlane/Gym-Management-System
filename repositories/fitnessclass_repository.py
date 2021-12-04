from flask.helpers import get_template_attribute
from db.run_sql import run_sql
from models.fittness_class import FitnessClass

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (name, active, capacity, start_time, duration, day) VALUES (%s, %s, %s, %s, %s, %s")
    values = [fitness_class.name, fitness_class.active, fitness_class.capacity, fitness_class.start_time, fitness_class.duration, fitness_class.day]
    results = run_sql(sql, values)
    id = results[0]['id']
    fitness_class.id = id
    return fitness_class

