# coding: utf-8
# Ahian

import math
class  QuadraticEquation:
    def __init__(self,__coeff_a = 1,__coeff_b = 1,__coeff_c = 1):
        self.__coeff_a = __coeff_a
        self.__coeff_b = __coeff_b
        self.__coeff_c = __coeff_c

    def get_coeff_a(self):
        return self.__coeff_a

    def get_coeff_b(self):
        return self.__coeff_b

    def get_coeff_c(self):
        return self.__coeff_c

    def get_discriminant(self):
        return self.__coeff_b**2 - 4 * self.__coeff_a * self.__coeff_c

    def has_solution(self):
        if self.get_discriminant() < 0:
            return False
        else:
            return True

    def get_root1(self):
        if self.has_solution():
            gen = self.__coeff_b**2 - 4*self.__coeff_a * self.__coeff_c
            return (-self.__coeff_b + math.sqrt(gen)) / (2*self.__coeff_a)
        else:
            return 0

    def get_root2(self):
        if self.has_solution():
            gen = self.__coeff_b**2 - 4*self.__coeff_a * self.__coeff_c
            return (-self.__coeff_b - math.sqrt(gen)) / (2 * self.__coeff_a)
        else:
            return 0

    def __str__(self):
        if self.get_discriminant() < 0:
            return "The equation has no roots."

        elif self.get_discriminant() == 0:
            return "The root is %.2f." % self.get_root1()

        else:
            return "The roots are %.2f and %.2f." % (self.get_root1(), self.get_root2())