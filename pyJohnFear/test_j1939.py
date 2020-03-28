#!/usr/bin/env python

from scapy.all import *
import logging
from scapy.config import conf

logger = logging.getLogger("scapy")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler)


class J1939(Packet):
    name = 'j1939'
    fields_desc = [XByteField('canid', bytes(4)),
                   IntField('pgn', 0),
                   ByteField('priority', bytes(1)),
                   BitField('extDataPage', 0, 1),
                   BitField('dataPage', 0, 1),
                   ByteField('pduFormat', bytes(1)),
                   ByteField('pduSpecs', bytes(0)),
                   IntField('srcAdr', 0),
                   IntField('groupExt', 255),
                   XByteField('data', bytes(8))]

    def pre_dissect(self, s):
        # TODO: read DBC file if set
        return s

    def do_dissect(self, s):
        canid = bytearray(s[:4])
        canid.reverse()
        canid[0] &= 0x1f
        self.fields['canid'] = bytes(canid)

        pgn = bytearray(canid[:-1])
        pgn[0] &= 0x03
        self.fields['pgn'] = int.from_bytes(pgn, byteorder='big')

        self.fields['data'] = s[8:]
        self.fields['priority'] = (canid[0] & 0b00011100) >> 2
        self.fields['extDataPage'] = (canid[0] & 0b00000010) >> 1
        self.fields['dataPage'] = canid[0] & 0b00000001
        self.fields['pduFormat'] = canid[1]
        self.fields['pduSpecs'] = canid[2]
        self.fields['srcAdr'] = canid[3]
        self.fields['groupExt'] = canid[2]
        return s

    def post_dissection(self, s):
        # TODO: spn resolution if DBC file exists
        return s


def make_test():
    return J1939(canid=bytes([0x01, 0x02]), pgn=10, data=bytes([0x03, 0x04]))


if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Test add-on v3.14")
    split_layers(CookedLinux, CAN)
    bind_layers(CookedLinux, J1939, proto=12)
    
