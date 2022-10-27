# coding: utf-8
# Ahian


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

    def get_print(self):
        return  "{}({:.2f})".format(self.__name, self.get_population_density())

class Country:
    def __init__(self,__name):
        self.__name = __name
        self.__cities_list = []

    def get_name(self):
        return self.__name

    def get_total_population(self):
        a = 0
        for i in self.__cities_list:
            a = a + i.get_population()
        return a

    def get_total_area(self):
        a = 0
        for i in self.__cities_list:
            a = a + i.get_area()
        return a

    def get_population_density(self):
        return float(self.get_total_population()) / float(self.get_total_area())

    def add_city(self,name, population, area):
        name = City(name,population,area)
        return self.__cities_list.append(name)

    def get_city(self, index):
        return self.__cities_list[index]

    def __str__(self):
        a = self.__name
        a = a + ":\n"
        for i in self.__cities_list:
            a = a + i.get_print() + "\n"
        a = a + "Population density = {:.2f}".format(self.get_population_density())
        return a

