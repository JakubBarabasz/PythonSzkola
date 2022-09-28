class Delta(object):

    def oblicz(self, a, b, c):

        delta = (b*b) - (4*a*c)
        print(a, b, c, delta)

        if delta > 0:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print("x1 = ", x1, "x2 = ", x2)
            return a, b, c, delta, x1, x2

        elif delta == 0:

            x0 = -b / (2 * a)
            print("x0 = ", x0)
            return a, b, c, delta, x0

        elif delta < 0:
            print("Brak rozwiązań")
            return a, b, c, delta


if __name__ == "__main__":
    deltaObj = Delta()
    deltaObj.oblicz(int(input("Podaj a: ")), int(input("Podaj b: ")), int(input("Podaj c: ")))
