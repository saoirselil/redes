#!/usr/bin/python

'This example creates a simple network topology with 1 AP and 2 stations'

from mininet.net import Mininet
from mininet.node import  Controller, OVSKernelAP
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    "Create a network."
    net = Mininet(controller=Controller, link=TCLink, accessPoint=OVSKernelAP)

    print "*** Creating nodes"
    h1 = net.addHost('h1', ip='176.16.10.1/27')
    h2 = net.addHost('h2', ip='176.16.10.34/27')
    h3 = net.addHost('h3', ip='176.16.10.65/27')
    h4 = net.addHost('h4', ip='176.16.10.24/27')
    h5 = net.addHost('h5', ip='176.16.10.33/27')
    h6 = net.addHost('h6', ip='176.16.10.90/27')
    s1 = net.addSwitch('s1')

    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633)

    print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    print "*** Associating Stations"
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.addLink(h5, s1)
    net.addLink(h6, s1)

    print "*** Starting network"
    net.build()
    c0.start()
    s1.start([c0])

    print "*** Running CLI"
    CLI(net)

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
