from wakeonlan import send_magic_packet
from config import connect, connect_row_factory
from dao import *
from ping3 import *


def ping_host(ip_id):
    ips = list(query_macs(ip_id))
    for ip in ips:
        dumpip = str(ip['ip'])
        sping = ping(dumpip, timeout=1)
        if sping is not None:
            return True
        else:
            return False


def add_mac(name, ip, mac):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(SQL_INCLUDE, (name, ip, mac))
    conn.commit()
    cursor.close()


def delete_host(num):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(SQL_DELETE, (num,))
    conn.commit()
    cursor.close()


def query_macs(mac_id=None):
    conn = connect_row_factory()
    cursor = conn.cursor()
    if mac_id is None:
        macs = cursor.execute(SQL_LIST_ALL)
        macsd = macs.fetchall()
    else:
        macs = cursor.execute(SQL_LIST_BY_ID, (mac_id,))
        macsd = macs.fetchall()
    return macsd


def send_packet_all():
    macs = list(query_macs())
    for mac in macs:
        dumpmac = str(mac['mac'])
        send_magic_packet(dumpmac)


def send_packet_one(mac_id):
    macs = list(query_macs(mac_id))
    for mac in macs:
        dumpmac = str(mac['mac'])
        send_magic_packet(dumpmac)


def get_info(ip_id):
    is_on = ping_host(ip_id)
    if is_on:
        pass

