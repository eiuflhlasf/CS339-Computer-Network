


"""Grouptable example

              Switch2 
            /         \                   
h1 ---Switch1         Switch4-----h2
            \         /
              Switch3



# static arp entry addition

h1 arp -s 192.168.1.2 00:00:00:00:00:02
h2 arp -s 192.168.1.1 00:00:00:00:00:01



ryu stuff:

ryu-manager group_table_lb.py

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep
from mininet.node import OVSBridge
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

from sys import argv


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        
        switch1 = self.addSwitch('s1',stp=True)
        switch2 = self.addSwitch('s2',stp=True)
        switch3 = self.addSwitch('s3',stp=True)
        switch4 = self.addSwitch('s4',stp=True)
        
        host1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24", cpu=.25)
        host2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24", cpu=.25)

        self.addLink(host1, switch1, bw=10, delay='5ms', loss=0, use_htb=True)
        self.addLink(host2, switch4, bw=10, delay='5ms', loss=0, use_htb=True)
        
        self.addLink(switch1, switch3, bw=10, delay='5ms', loss=5, use_htb=True)
        self.addLink(switch1, switch2, bw=10, delay='5ms', loss=5, use_htb=True)
        self.addLink(switch4, switch3, bw=10, delay='5ms', loss=5, use_htb=True)
        self.addLink(switch4, switch2, bw=10, delay='5ms', loss=5, use_htb=True)
        


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    h1, h2 = net.getNodeByName('h1', 'h2')
    CLI(net)
    net.stop()
