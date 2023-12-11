from abc import ABC

from Models import RentalProperty


class PropertyFactory(ABC):
    def create_property(self, p_id, city, street, street_num, property_type, area, room_num, floor, size, price):
        pass


class RentalPropertyFactory(PropertyFactory):
    def create_property(self, p_id, city, street, street_num, property_type, area, room_num, floor, size, price):
        return RentalProperty(p_id, city, street, street_num, property_type, area, room_num, floor, size, price, 'rental')


class ForSalePropertyFactory(PropertyFactory):
    def create_property(self, p_id, city, street, street_num, property_type, area, room_num, floor, size, price):
        return RentalProperty(p_id, city, street, street_num, property_type, area, room_num, floor, size, price, 'for_sale')
