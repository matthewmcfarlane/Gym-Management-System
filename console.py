import pdb

from flask.globals import current_app
from models.fittness_class import FitnessClass
from models.member import Member
from models.booking import Booking


import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
fitness_class_repository.delete_all()
member_repository.delete_all()

member1 = Member('Jack', 'Sparrow', '1950-12-01', 'js@poc.com', 'Standard', True)
member2 = Member('John', 'Snow', '1970-10-04', 'jsnow@stark', 'Premium', True)
member3 = Member('Homer', 'Simpson', '1960-10-09', 'homerjsimpson@sprfnuclear.com', 'Standard', False)
member_repository.save(member1)
member_repository.save(member2)
member_repository.save(member3)


fitness_class1 = FitnessClass('Zumba', 10, '18:30', 45, 'Monday', True)
fitness_class2 = FitnessClass('Spin', 18, '12:30', 25, 'Wednesday', True)
fitness_class3 = FitnessClass('Inductions', 4, '17:30', 75, 'Friday', False)
fitness_class_repository.save(fitness_class1)
fitness_class_repository.save(fitness_class2)
fitness_class_repository.save(fitness_class3)

booking1 = Booking(member1, fitness_class1)
booking2 = Booking(member2, fitness_class2)
booking3 = Booking(member3, fitness_class3)
booking_repository.save(booking1)
booking_repository.save(booking2)
booking_repository.save(booking3)
pdb.set_trace()
booking_repository.select_all()


pdb.set_trace()
