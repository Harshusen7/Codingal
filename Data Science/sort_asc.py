import numpy as np

data_type = [('name', 'S15'), ('class', int), ('haight', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

# create a structured array
students = np.array(students_details, dtype=data_type)
data_type = [(name = )]