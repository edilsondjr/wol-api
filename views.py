from wol import app
from flask import request, json, jsonify
from models import *
import logging

logging.basicConfig(filename="wolapi.log",
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y | %I:%M:%S %p | %Z |')
base_url = '/api/v1/'


@app.route('/', methods=['GET'])
def index():
    return '''<h1>Wake on Lan API</h1>'''


@app.route(base_url+'all', methods=['GET'])
def allmacs():
    lmacs = query_macs()
    return jsonify(lmacs)


@app.route(base_url+'/wake/<int:mac_id>', methods=['GET'])
def wake_one(mac_id):
    try:
        send_packet_one(mac_id)
        logging.info(f'Magic Packet sent to ID: {mac_id}')
        return 'The magic packet has been sent to ID: ' + str(mac_id)
    except TypeError:
        return 'Invalid ID, please provide a valid one'


@app.route(base_url+'/wakeall', methods=['GET'])
def wake_all():
    send_packet_all()
    logging.info(f'Magic Packet sent to all IDs')
    return 'The magic packet has been sent to all hosts'


@app.route(base_url+'/addnew', methods=['POST'])
def add_new():
    name = request.args.get('name')
    ip = request.args.get('ip')
    mac = request.args.get('mac')
    fmac = f"{mac[0:2]}-{mac[2:4]}-{mac[4:6]}-{mac[6:8]}-{mac[8:10]}-{mac[10:12]}"
    fmac = fmac.upper()
    try:
        add_mac(name, ip, fmac)
        logging.info(f'The following record has been added: Name: {name} - IP: {ip} - MAC: {mac}')
        return 'The data has been inserted'
    except TypeError:
        logging.info(f'ERROR INSERTING: Name: {name} - IP: {ip} - MAC: {mac}')
        return 'Something went wrong'


@app.route(base_url+'/delete/<int:mac_id>', methods=['DELETE'])
def delete_mac(mac_id):
    delete_host(mac_id)
    logging.info(f'The following ID has been deleted: {mac_id}')
    return 'The data has been deleted'


@app.route(base_url+'/ping/<int:ip_id>', methods=['GET'])
def ping_id(ip_id):
    pings = ping_host(ip_id)
    if pings is not None:
        logging.info(f'Pinging ID: {ip_id}')
        return json.dumps(pings)
    else:
        logging.info(f'ERROR: ID {ip_id} Invalid')
        return 'Invalid ID, please provide a valid one'
