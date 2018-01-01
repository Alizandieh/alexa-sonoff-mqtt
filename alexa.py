import logging, os
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import paho.mqtt.client as mqtt

app = Flask(__name__)
ask = Ask(app, '/alexa')
client = mqtt.Client("kitchen")

#logging.getLogger('flask_ask').setLevel(logging.DEBUG)

mqtt_server=os.environ['MQTT_SERVER']

@app.route('/')
def homepage():
    return "Uh oh, spaghettios"

@ask.intent('KitchenOff')
def switch_off():
    client.publish("cmnd/home/kitchen/POWER", "off")
    speech_text = "Yes Dear"
    return statement(speech_text)

@ask.intent('KitchenOn')
def switch_on():
    client.publish("cmnd/home/kitchen/POWER", "on")
    speech_text = "Yes Dear"
    return statement(speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    client.connect(mqtt_server)
    client.loop_start()
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(host='0.0.0.0', debug=False, port=80)
