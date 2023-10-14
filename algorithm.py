class Object:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color


# Класс для проверок
class Checks:
    def __init__(self, input_order):
        self.input_order = input_order

    def check(self):
        if (len(self.input_order) > 3 or len(self.input_order) < 3 or (self.input_order[0] != "к"
                and self.input_order[0] != "з" and self.input_order[0] != "с")
                or (self.input_order[1] != "к" and self.input_order[1] != "з" and self.input_order[1] != "с"
                or self.input_order[1] == self.input_order[0]) or (self.input_order[2] != "к"
                and self.input_order[2] != "з" and self.input_order[2] != "с"
                or self.input_order[2] == self.input_order[0] or self.input_order[2] == self.input_order[1])
                or self.input_order[0] == "" or self.input_order[1] == "" or self.input_order[2] == ""):
            return "Error: Неверный формат ввода последовательности сортировки"
        return "pass"


class ColorOrder:
    def __init__(self, objects, order):
        self.objects = objects
        self.order = order

    # Сортировка
    def sort(self):
        # Я бы использовал такую сортировку
        # return sorted(objects, key=lambda obj: self.order.index(obj.color))

        blue_elements = []
        red_elements = []
        green_elements = []

        if len(self.objects) < 3:
            return "Error: Неверный формат ввода данных для сортировки"

        # Разбитие строки на 3 массива
        for obj in self.objects:
            if obj.color == "с":
                blue_elements.append(obj)
            elif obj.color == "к":
                red_elements.append(obj)
            elif obj.color == "з":
                green_elements.append(obj)
            elif obj.color == "":
                return "Error: Неверный формат ввода данных для сортировки"
            else:
                return "Error: Неверный формат ввода данных для сортировки"

        # Слияние
        output = []
        if self.order[0] == "с":
            output.extend(blue_elements)
            if self.order[1] == "к":
                output.extend(red_elements)
                output.extend(green_elements)
            else:
                output.extend(green_elements)
                output.extend(red_elements)
        elif self.order[0] == "к":
            output.extend(red_elements)
            if self.order[1] == "с":
                output.extend(blue_elements)
                output.extend(green_elements)
            else:
                output.extend(green_elements)
                output.extend(blue_elements)
        elif self.order[0] == "з":
            output.extend(green_elements)
            if self.order[1] == "к":
                output.extend(red_elements)
                output.extend(blue_elements)
            else:
                output.extend(blue_elements)
                output.extend(red_elements)

        return output
