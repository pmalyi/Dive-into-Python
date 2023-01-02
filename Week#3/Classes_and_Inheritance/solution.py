import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)


    def get_photo_file_ext(self):
        file_type = os.path.splitext(self.photo_file_name)[1]
        if file_type in ('.jpg', '.jpeg', '.png', '.gif'):
            return file_type


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_lwh):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_lwh

        try:
            self.body_length = float(body_lwh[:body_lwh.find('x')])
            self.body_width = float(body_lwh[body_lwh.find('x') + 1:body_lwh.rfind('x')])
            self.body_height = float(body_lwh[body_lwh.rfind('x') + 1:])
        except ValueError:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra



def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 7 and row[1] != '' and \
                    os.path.splitext(row[3])[0] != '' and \
                    os.path.splitext(row[3])[1] in ('.jpg', '.jpeg', '.png', '.gif') \
                    and row[5] != '':
                if row[0] == 'car' and row[2].isdigit() \
                        and row[4] == '' and row[6] == '':
                    car = Car(row[1], row[3], row[5], row[2])
                    car_list.append(car)
                elif row[0] == 'truck' and row[2] == '' \
                        and row[6] == '':
                    truck = Truck(row[1], row[3], row[5], row[4])
                    car_list.append(truck)
                elif row[0] == 'spec_machine' and row[2] == '' \
                        and row[4] == '' and row[6] != '':
                    spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
                    car_list.append(spec_machine)
    return car_list
