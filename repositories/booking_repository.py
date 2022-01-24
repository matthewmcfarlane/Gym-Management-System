from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository


#CRUD


#CREATE
def save(booking):
    sql = "INSERT INTO bookings( member_id, fitness_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.fitness_class.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

#READ

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row['member_id'])
        fitness_class = fitness_class_repository.select(row['fitness_class_id'])
        booking = Booking(member, fitness_class, row['id'])
        bookings.append(booking)
    return bookings

#UPDATE


#DELETE
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)









