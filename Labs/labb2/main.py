import matplotlib.pyplot as plt
import numpy as np


def machine_learning_algorithm(x: float, y: float, pichu: list, pikachu: list):
    """
    This method will define whether the poin is Pichu or Pikachu
    :param: x (float): The position of the point in x-axis 
    :param: y (float): The position of thew point in y-axis
    :return (str) whether pichu or pikachu
    """
    pichu_point = 0
    pikachu_point = 0
    pikachu_smallest_x = 20.216002852334192
    pikachu_smallest_y = 31.418267572382227
    pichu_largest_x = 23.6967469082275
    pichu_largest_y = 35.40347944144049

    distance_pichu = []
    distance_pikachu = []
    for i in pichu:
        distance = []
        distance.append(x - i[0])
        distance.append(y - i[1])
        distance_pichu.append(distance)

    for i in pikachu:
        distance = []
        distance.append(x - i[0])
        distance.append(x - i[1])
        distance_pikachu.append(distance)

    closest_point = [pichu[0][0], pichu[0][1]]
    sorted(pichu)
    print(pichu)

    if x < pikachu_smallest_x:
        return "pichu"
    if y < pikachu_smallest_y:
        return "pichu"
    if x > pichu_largest_x:
        return "pikachu"
    if y > pichu_largest_y:
        return "pikachu"


def find_smallest(num1, num2):
    if num1 < num2:
        return num1
    return num2


def find_largest(num1, num2):
    if num2 > num1:
        return num2
    return num1


def main():
    pikachu = []
    pichu = []
    pichu_x = []
    pichu_y = []
    pikachu_x = []
    pikachu_y = []
    with open("datapoints.txt") as f_reads:
        for line in f_reads.read().split("\n"):
            line = line.split(",")
            if line[-1].strip() == "0":
                pichu.append([float(line[0]), float(line[1])])
                pichu_x.append(float(line[0].strip()))
                pichu_y.append(float(line[1].strip()))
            if line[-1].strip() == "1":
                pikachu.append([float(line[0]), float(line[1])])
                pikachu_x.append(float(line[0].strip()))
                pikachu_y.append(float(line[1].strip()))

    plt.plot(pichu_x, pichu_y)
    plt.plot(pikachu_x, pikachu_y)
    plt.xlabel("X Axel")
    plt.ylabel("Y Axel")
    plt.title("Pichu and Pikachu")
    plt.show()
    print(machine_learning_algorithm(25, 32, pichu, pikachu))


if __name__ == "__main__":
    main()
