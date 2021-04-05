import time

import sensornode
import paho.mqtt.client as mqtt

MQTT_ADDRESS = "emqx"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "Bathroom_Sensor"


def main() -> object:
    client = mqtt.Client(client_id=MQTT_CLIENT_ID)
    client.connect(MQTT_ADDRESS, MQTT_PORT)

    node = sensornode.SensorNode()  # port name, slave address (in decimal)
    #    instrument.debug = True

    client.loop_start()

    while True:
        node.read()
        client.publish("/places/our place/basement/bathroom/SENSOR", str(node))
        time.sleep(30)


if __name__ == "__main__":
    print("sensor node: start")
    main()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
