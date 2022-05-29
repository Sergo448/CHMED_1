# -*- coding: utf-8 -*-


import cmath
import numpy as np


def print_ravn(raz):
    print(raz * 40)


class gamma():
    """Базовый класс для всех расчетов"""

    global k_, n, b, m, a, d, eps, gamma1, f

    def __init__(self, gamma):
        self.gamma = gamma

    def kaa(self, k_, eps, n, b, m, a):
        self.gamma = 0.1
        argument_k = []
        while self.gamma < 2.1:
            arg = (k_ ** 2) * eps - self.gamma ** 2 - (n * np.pi / b) ** 2 - (
                    m * np.pi / a) ** 2
            arg1 = cmath.sqrt(arg)
            argument_k.append(arg1)
            self.gamma += 0.1
        return argument_k

    @staticmethod
    def yaa(k, k_):
        kkk = 0
        kkkk = []
        while kkk < 20:
            k_plus = k[kkk] / k_
            kkkk.append(k_plus)
            kkk += 1
        return kkkk

    @staticmethod
    def y_in_ri(y, k, d):
        yyy_in_ri = []
        yyy_in_ri1 = []
        pk = 0
        fi = complex(0, 1)
        for num in y:
            yyy_in_ri.append(-fi * num)
        for num1 in k:
            yyy_in_ri1.append(yyy_in_ri[pk] * (1 / np.tan(num1 * d)))
            pk += 1
        return yyy_in_ri1

    @staticmethod
    def y_in_le(yy, YY, kk, d_):
        yyy_in_le = []
        pk = 0
        fi = complex(0, 1)
        while pk < 20:
            yyy_in_le.append(
                yy[pk] * ((YY[pk] + fi * yy[pk] * np.tan(kk[pk] * d_)) / (yy[pk] + fi * YY[pk] * np.tan(kk[pk] * d_))))
            pk += 1
        return yyy_in_le

    @staticmethod
    def y_in_le_(yy, kk, d_, LL):
        yyy_in_le1 = []
        pk = 0
        fi = complex(0, 1)
        while pk < 20:
            yyy_in_le1.append(
                yy[pk] * ((LL[pk] + fi * yy[pk] * np.tan(kk[pk] * d_)) / (yy[pk] + fi * LL[pk] * np.tan(kk[pk] * d_))))
            pk += 1
        return yyy_in_le1

    @staticmethod
    def plot_gamma(tb, tbk):
        pk = 0
        im_array = []
        while pk < 20:
            im_array.append(tb[pk] + tbk[pk])
            pk += 1
        return im_array

    # Задаем все необходимые переменные

    # Расчет 1

    trust = True
    while trust:
        c = 3 * (10 ** 11)

        # Введение геометрии волновода в мегагерцах
        # Введенное число

        print('Ввод центральной чатоты (ГГц):')
        try:
            f = float(eval(input())) * 10 ** 9
        # f = 30 * 10 ** 9
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            print_ravn('=')
        print_ravn('=')
        eps_0 = 8.854 * 10 ** (-15)
        mu_0 = 4 * np.pi * 10 ** (-10)

        ms = 0
        while ms < 1:
            try:
                print('Ввод а и b, через enter:')
                print('Например 5 и 3')
                a = float(eval(input('a: ')))
                b = float(eval(input('b: ')))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                print_ravn('=')
            print_ravn('=')
            # Wave type
            n = 0
            m = 0

            lambda_ = c / f
            w_ = 2 * np.pi * f
            k_ = w_ * (eps_0 * mu_0) ** 0.5
            try:
                print('Ввод значений d(толщина слоя), через enter:')
                print("Например: 2.5, 0.001, 0.5, 0, 0.499")
                print("При вводе дробной части использовать точки!")
                d = [float(eval(input("d1: "))),
                     float(eval(input("d2: "))),
                     float(eval(input("d3: "))),
                     float(eval(input("d4: "))),
                     float(eval(input("d5: ")))]
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                print_ravn('=')
            print_ravn('=')
            if a <= (d[0] + d[1] + d[2] + d[3] + d[4]):
                print("Неверно введены  а или d, попробуйте снова")
                print_ravn('=')
            else:
                ms += 1
            d.append(a - d[0] - d[1] - d[2] - d[3] - d[4])

            try:
                print('Ввод значений eps(диэлектрическая проницаемость),через enter:')
                print("Например: 1, 125, 9.8, 1, 1, 1.5")
                print("При вводе дробной части использовать точки!")
                eps = [
                    float(eval(input("eps1: "))),
                    float(eval(input("eps2: "))),
                    float(eval(input("eps3: "))),
                    float(eval(input("eps4: "))),
                    float(eval(input("eps5: "))),
                    float(eval(input("eps6: ")))]
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                print_ravn('=')
            print_ravn('=')

        def funk(self):
            k_0_1 = self.kaa(k_, eps[0], n, b, m, a)
            k_0_2 = self.kaa(k_, eps[1], n, b, m, a)
            k_0_3 = self.kaa(k_, eps[2], n, b, m, a)
            k_0_4 = self.kaa(k_, eps[3], n, b, m, a)
            k_0_5 = self.kaa(k_, eps[4], n, b, m, a)
            k_0_6 = self.kaa(k_, eps[5], n, b, m, a)

            # Расчет 2
            y_0_1 = self.yaa(k_0_1, k_)
            y_0_2 = self.yaa(k_0_2, k_)
            y_0_3 = self.yaa(k_0_3, k_)
            y_0_4 = self.yaa(k_0_4, k_)
            y_0_5 = self.yaa(k_0_5, k_)
            y_0_6 = self.yaa(k_0_6, k_)

            # Расчет 3
            Y_in_4_Ri = self.y_in_ri(y_0_6, k_0_6, d[5])
            Y_in_2_Le = self.y_in_ri(y_0_1, k_0_1, d[0])

            Y_in_3_Ri = self.y_in_le(y_0_5, Y_in_4_Ri, k_0_5, d[4])
            Y_in_1_Le = self.y_in_le(y_0_2, Y_in_2_Le, k_0_2, d[1])

            # Result

            # Высчитываем две результирующие формулы,
            # которые потом понадобятся нам для
            # построения графика

            Y_result_Le = self.y_in_le(y_0_3, Y_in_1_Le, k_0_3, d[2])
            Y_result_Ri = self.y_in_le(y_0_4, Y_in_3_Ri, k_0_4, d[3])

            #    Построение графика

            IM = np.array(self.plot_gamma(Y_result_Ri, Y_result_Le)).imag
            x = np.arange(0.1, 2.1, 0.1)
            y = IM
            return x, y

        trust = False
