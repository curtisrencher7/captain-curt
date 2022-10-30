def on_wifi_connected():
    pass
kittenwifi.on_wifi_connected(on_wifi_connected)

def on_udp_ondata(udpData):
    pass
kittenwifi.udp_ondata(on_udp_ondata)

def on_sound_loud():
    pass
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_mqtt_topic_data(topic, data):
    pass
kittenwifi.on_mqtt_topic_data(on_mqtt_topic_data)

def on_every_interval():
    list2: List[number] = []
    for value in list2:
        pass
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
