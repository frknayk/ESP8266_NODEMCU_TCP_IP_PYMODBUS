#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GitHub_Writer : Furkan Ayik cheers :))

from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST1 = "192.168.43.233"
SERVER_HOST2 = "192.168.43.12"

SERVER_PORT = 502


c = ModbusClient()

# uncomment this line to see debug message
#c.debug(True)
# Register Addresses
addr = [10,11,12,13,14,15] # Unused Register Addresses
toggle = [1,2,3,4,5,6] # Register Values for writing ...

hosts = [ SERVER_HOST1,SERVER_HOST2]


while True:
    # print("Enter Port Number ( 0 : MASTER-1 ---- 1 : MASTER2 )")
    HOST = int ( input("Enter Port Number (MASTER-1 :  1 ***** MASTER-2 : 2 ) :  ") )
    if(HOST == 1):
        print("MASTER - 1 ( IP : {0} ) is choosen.".format(SERVER_HOST1))
        SERVER_HOST = SERVER_HOST1
        c.host(SERVER_HOST)
        c.port(SERVER_PORT)
        if not c.is_open():
            if not c.open():
                print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

        # if open() is ok, write coils (modbus function 0x01)
        if c.is_open():
            # write 4 bits in modbus address 0 to 3
            addr = 10
            toggle = 22
            is_ok = c.write_single_register(addr, toggle)
            if is_ok:
                print("Writint register to " + str(addr) + " : " + str(toggle))
            else:
                print("Unable to write " + str(addr) + " : " + str(toggle))

            read_reg_address = 12
            how_many = 1

            bits = c.read_holding_registers(read_reg_address,how_many)

            if bits:
                print("Holding Register Value of :  " + str(read_reg_address) + " : " + str(bits) )
            else:
                print("Unable to read")

    elif(HOST == 2):
        print("MASTER - 2 ( IP : {0} ) is choosen.".format(SERVER_HOST2))
        SERVER_HOST = SERVER_HOST2
        c.host(SERVER_HOST)
        c.port(SERVER_PORT)
            # open or reconnect TCP to server
        if not c.is_open():
            if not c.open():
                print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

        # if open() is ok, write coils (modbus function 0x01)
        if c.is_open():
            # write 4 bits in modbus address 0 to 3
            addr = 14
            toggle = 22
            is_ok = c.write_single_register(addr, toggle)
            if is_ok:
                print("Writint register to " + str(addr) + " : " + str(toggle))
            else:
                print("Unable to write " + str(addr) + " : " + str(toggle))

            read_reg_address = 16
            how_many = 1

            bits = c.read_holding_registers(read_reg_address,how_many)

            if bits:
                print("Holding Register Value of :  " + str(read_reg_address) + " : " + str(bits) )
            else:
                print("Unable to read")
