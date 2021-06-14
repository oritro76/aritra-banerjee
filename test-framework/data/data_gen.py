import string
from random import randint, choices

from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def __get_random_product_name(self):
        prd_names = [
            "Dragonball: Evolution - PRE-OWNED - PS2",
            "Dynex™ - Case for Apple® iPhone® 10 - Green/White",
            "High School Musical 3: Senior Year DANCE - PRE-OWNED - PlayStation 5",
            "Best Buy Buckets",
            "Rock Band Unplugged — PRE-OWNED - PS2",
            "Sony - ES SXRD 3D-Ready 4K Home Theater Projector - Black"
        ]
        return prd_names[randint(0, len(prd_names)-1)]

    def __get_random_product_type(self):
        types = [
            "HardGood",
            "SoftGood"
        ]
        return types[randint(0, len(types)-1)]

    def __get_random_upc(self):
        return ''.join(str(randint(0, 9)) for _ in range(12))

    def __get_random_description(self):
        return self.fake.sentence()

    def __get_random_manufacturer(self):
        manufacturers = [
            "canon",
            "sony",
            "samsung",
            "toshiba"
        ]
        return manufacturers[randint(0, len(manufacturers)-1)]

    def __get_random_model(self):
        return ''.join(choices(string.ascii_uppercase + string.digits, k=8))

    def __get_random_url(self):
        urls = [
            "http://www.bestbuy.com/site/canon-ef-600mm-f-4l-is-ii-usm-super-telephoto-lens-for-most-canon-eos-slr-cameras-white/1688841.p?id=1219060409045&skuId=1688841&cmp=RMXCC",
            "http://www.bestbuy.com/site/nikon-af-s-nikkor-400mm-f-2-8e-fl-ed-vr-lens-for-select-nikon-dslr-cameras/9324006.p?id=1219405808498&skuId=9324006&cmp=RMXCC",
            "http://www.bestbuy.com/site/canon-ef-200-400mm-f-4l-is-usm-super-telephoto-lens-for-most-canon-eos-slr-cameras-white/1757296.p?id=1219062656772&skuId=1757296&cmp=RMXCC",
            "http://www.bestbuy.com/site/nikon-af-s-nikkor-500mm-f-4e-fl-ed-vr-super-telephoto-lens-black/4262000.p?id=1219732457043&skuId=4262000&cmp=RMXCC",
            "http://www.bestbuy.com/site/magnolia-home-theater-free-in-home-consultation/3552309.p?id=1218412707201&skuId=3552309&cmp=RMXCC"
            ]
        return urls[randint(0, len(urls)-1)]

    def __get_random_image_url(self):
        urls = [
            "http://img.bbystatic.com/BestBuy_US/images/products/3552/3552309_sa.jpg",
            "http://img.bbystatic.com/BestBuy_US/images/products/1339/1339042_sa.jpg",
            "http://img.bbystatic.com/BestBuy_US/images/products/1478/1478398_sa.jpg",
            "http://img.bbystatic.com/BestBuy_US/images/products/2341/2341234_sa.jpg",
            "http://img.bbystatic.com/BestBuy_US/images/products/6574/6574562_sa.jpg"
        ]
        return urls[randint(0, len(urls)-1)]

    def create_product(self):
        return {
            "name": self.__get_random_product_name(),
            "type": self.__get_random_product_type(),
            "price": 100.99,
            "shipping": 15.99,
            "upc": self.__get_random_upc(),
            "description": self.__get_random_description(),
            "manufacturer": self.__get_random_manufacturer(),
            "model": self.__get_random_model(),
            "url": self.__get_random_url(),
            "image": self.__get_random_image_url()
        }

    def __get_random_store_name(self):
        store_names = [
            "Minnetonka",
            "Inver Grove Heights",
            "Northtown",
            "St Cloud",
            "Fargo"
        ]
        return store_names[randint(0, len(store_names)-1)]

    def __get_random_store_type(self):
        store_types = [
            "BigBox",
            "SmallBox",
            "BigShop",
            "SmallShop",
            "LocalShop"
        ]
        return store_types[randint(0, len(store_types)-1)]

    def __get_random_address(self):
        return self.fake.address()

    def __get_random_city(self):
        return self.fake.city()

    def __get_random_state(self):
        return "MN"

    def __get_random_zip(self):
        return self.fake.zipcode()

    def __get_random_lat(self):
        return float(self.fake.latitude())

    def __get_random_lng(self):
        return float(self.fake.longitude())

    def __get_random_hours(self):
        hours = [
            "Mon: 10-9; Tue: 10-9; Wed: 10-9; Thurs: 10-9; Fri: 10-9; Sat: 10-9; Sun: 10-8",
            "Mon: 10-12; Tue: 10-5; Wed: 10-6; Thurs: 10-5; Fri: 10-5; Sat: 10-5; Sun: 10-5",
            "Mon: 9-9; Tue: 9-9; Wed: 10-12; Thurs: 10-12; Fri: 10-12; Sat: 10-9",
            "Mon: 10-9; Tue: 10-9; Wed: 10-9; Thurs: 10-9; Fri: 10-9; Sun: 10-8",
            "Mon: 10-9; Tue: 10-9; Wed: 10-9; Thurs: 10-9; Sat: 10-9; Sun: 10-8",
        ]
        return hours[randint(0, len(hours)-1)]

    def create_store(self):
        return {
            "name": self.__get_random_store_name(),
            "type": self.__get_random_store_type(),
            "address": "13513 Ridgedale Dr",
            "address2": "13513 Ridgedale Dr",
            "city": self.__get_random_city(),
            "state": self.__get_random_state(),
            "zip": self.__get_random_zip(),
            "lat": self.__get_random_lat(),
            "lng": self.__get_random_lng(),
            "hours": self.__get_random_hours(),
        }

    def __get_random_service_names(self):
        service_names = [
            "Geek Squad Services",
            "Best Buy Mobile",
            "Best Buy For Business",
            "Apple Shop",
            "Camera Experience Shop "
        ]
        return service_names[randint(0, len(service_names)-1)]

    def create_service(self):
        return {
            "name": self.__get_random_service_names()
        }

    def __get_random_id(self):
        return "abcat" + ''.join(choices(string.digits, k=7))

    def __get_random_category(self):
        categories = [
            "TV & Home Theater",
            "Blu-ray & DVD Players",
            "Musical Instruments",
            "Computers & Laptops",
            "Furnitures"
        ]
        return categories[randint(0, len(categories)-1)]

    def create_category(self):
        return {
            "id": self.__get_random_id(),
            "name": self.__get_random_category()
        }
