# No_More_Cookies-
DDOS attacks tool; send superfluous requests to take down a website (For training purposes only!)


## Todo
1. Research what DDOS is (Complete)
2. Look for python modules for DDOS (Complete)
    * socket
    * threading
3. Build multiple DDOS tools 1 for website and the other for networks
    * Brute force DOS tool built
4. Build website to test attacks (Complete)
    * Problem: Connection resets when to many packets are sent.
    This may be because of some built in DOS prevention functionality in flask
5. Build tool to defend against attacks


# Research
A DDOS attack requires multiple nodes on different networks. Normally 2-3 nodes.

A DOS attack is fewer.

## Types of attacks 
### Yo-yo attack:
        This attack targets cloud hosted applications with auto-scaling enabled. The attack floods the networks with traffic causing the app to auto scale to account for the increase in bandwidth, then stopping the attack. Thus leaving the app over provisioned

        Once it scales back down the attack continues and it follows this pattern cuasing a fincancial drain for the host and diminishing quality of service for the users.

    I'm broke I'm not spinning up a host for this :(

### Application Layer Attacks
Application layer DDOS attacks are still use today see [Log4j](https://en.wikipedia.org/wiki/Log4j) and [Log4shell](https://en.wikipedia.org/wiki/Log4Shell)

Simple attacks are bruteforce; flooding a host with a maliciooous packets for data overwhelming to the point where is crashes.

## Plan of attack
You only need the port of the host then to send multiple packets you need to do multi-threading.

send GET requets to flood the host

make sure to spoof your ip addreess

## How to defend
Use wireshark or some network scanning tool to look at the network traffic. From there you can see which ip address is flooding the network. block that ip and you're good. If its just a DOS attack. A DDOS attack will have multiple nodes attacking so it make it much harder

## Blue Team
Automate the detection of bots on the network and automatically blog those that are sending to many packets.