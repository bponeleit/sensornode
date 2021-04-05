from datetime import datetime

import serial
import json


class SensorNode:
    """Read .

    Args:


    """
    temp: float
    humidity: float
    light: int

    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1) -> None:
        """

        :param port:
        :param baudrate:
        :param bytesize:
        :param parity:
        :param stopbits:
        """
        self.temp = 0
        self.humidity = 0
        self.light = 0
        self.serial = serial.Serial(parity=parity,
                                    port=port,
                                    baudrate=baudrate,
                                    bytesize=bytesize,
                                    stopbits=stopbits,
                                    timeout=4)

    def __str__(self) -> str:
        environment = {"Temperature": self.temp, "Humidity": self.humidity, "Light": self.light}
        data = {"Time": str(datetime.now()), "ENVIRONMENT": environment}
        return json.dumps(data)

    def read(self) -> None:
        if not self.serial.is_open:
            self.serial.open()
        self.parse(self.serial.read(50))
        self.serial.close()

    def parse(self, message: str) -> None:
        print(message)
        if len(message) >= 28:
            data = message[15:]
            values = data.split()

            try:
                print(values[1])
                print(values[1].decode('utf-8'))
                self.temp = float(values[1].decode('ascii').strip())
            except:
                pass
            try:
                self.humidity = float(values[2].decode('ascii')[:5])
            except:
                pass
            try:
                self.light = int(values[2].decode('ascii')[6:])
            except:
                pass
