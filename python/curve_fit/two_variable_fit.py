import math

class TwoVariableFit:
    @staticmethod
    def solve_equation (x_values, y_values):
        best_a_b_c_difference_values = []   # array of tuples as a, b, c and difference
        have_result = False
        num_x_values = len(x_values)
        for i in range(0, num_x_values):
            x = x_values[i]
            y = y_values[i]
            smallest_difference = math.inf
            best_a_b_c_difference = (0,0,0)
            for a in range(-11, 11):
                for b in range(-11, 11):
                    for c in range(-11,11):
                        result_y = a*(x*x) + b*(x) + c
                        if abs(result_y - y) < abs(smallest_difference):
                            smallest_difference = result_y - y
                            best_a_b_c_difference = (a, b, c, smallest_difference)
            best_a_b_c_difference_values.append(best_a_b_c_difference)

        return best_a_b_c_difference_values

    @staticmethod
    def known_equation_1():
        y_values = []
        x_values = []
        for x in range (-10,20):
            y = 2*x*x + 5*x + 10
            x_values.append(x)
            y_values.append(y)
        return (x_values, y_values)

if __name__ == '__main__':
    (x_values, y_values) = TwoVariableFit.known_equation_1()

    print (TwoVariableFit.solve_equation(x_values, y_values))
