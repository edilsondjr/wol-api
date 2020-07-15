from wakeonlan import send_magic_packet
import config
from ping3 import *


def ping_host(ip_id):
    mac = query_macs(ip_id).json
    dumpip = mac['ip']
    sping = ping(dumpip, timeout=1)
    if sping is not None:
        return True
    else:
        return False


def add_mac(name, ip, mac):
    new_row = config.Hosts(name=name, ip=ip, mac=mac)
    config.db.session.add(new_row)
    config.db.session.commit()


def delete_host(num):
    config.Hosts.query.filter_by(id=num).delete()
    config.db.session.commit()


def query_macs(mac_id=None):
    if mac_id is None:
        macs = config.Hosts.get_delete_put_post()
    else:
        macs = config.Hosts.get_delete_put_post(mac_id)
    return macs


def send_packet_all():
    macs = query_macs().json
    for mac in macs:
        dumpmac = mac['mac']
        send_magic_packet(dumpmac)


def send_packet_one(mac_id):
    mac = query_macs(mac_id).json
    dumpmac = mac['mac']
    send_magic_packet(dumpmac)


def get_info(ip_id):
    is_on = ping_host(ip_id)
    if is_on:
        pass

