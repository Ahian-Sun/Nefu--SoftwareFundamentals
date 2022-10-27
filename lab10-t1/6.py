# coding: utf-8
# Ahian


class City:
    def __init__(self,city_name, population = 1, area = 1):
        self.__name = city_name
        self.__population = population
        self.__area = area

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    def get_area(self):
        return self.__area

    def set_name(self,name):
        self.__name = name

    def set_population(self,num):
        if num > 0:
            self.__population = num

    def set_area(self,num):
        if num > 0:
            self.__area = num

    def get_population_density(self):
        return float(self.__population) / float(self.__area)

    def __str__(self):
        return "{}({:.2f})".format(self.__name,self.get_population_density())

