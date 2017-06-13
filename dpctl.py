from flask import Flask, jsonify
import subprocess

sp = Flask(__name__)

OVS_CMD = 'ovs-dpctl'

"""
This library provides basic access to create, modify and delete Open vSwitch
datapaths.
Some function descriptions taken from the ovs
man (8) pages or inspired by.
"""


def add_dp(dp):
    
    add = subprocess.call(['sudo', 'ovs-dpctl', 'add-dp' , dp]) 


def del_dp(dp):
    delete = subprocess.call(['sudo', 'ovs-dpctl', 'del-dp', dp]) 


def add_if(dp, netdev):
    addif = subprocess.call(['sudo', 'ovs-dpctl', 'add-if', dp, netdev])
def del_if(dp, netdev):
    delif = subprocess.call(['sudo', 'ovs-dpctl', 'del-if', dp, netdev])
def dump_dps():
    dump = subprocess.check_output(['sudo', 'ovs-dpctl', 'dump-dps'])
    return dump
def show(dp):
    showdp = subprocess.check_output(['sudo', 'ovs-dpctl', 'show', dp])
    return showdp
def dump_flows(dp):
    dump = subprocess.check_output(['sudo', 'ovs-dpctl', 'dump-flows', dp])
    return dump
def del_flows(dp):
    delete = subprocess.call(['sudo', 'ovs-dpctl', 'del-flows', dp])

def set_if(dp, port):
    update = subprocess.call(['sudo', 'ovs-dpctl', 'set-if', dp, port])

