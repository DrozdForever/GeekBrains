from time import sleep
from itertools import cycle


class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [10, 32]], ['yellow', [2, 33]]]

    def running(self):
        for light in cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            sleep(light[1][0])


traffic_light = TrafficLight()
traffic_light.running()
