# Collection of security demos

## Dependencies
- Python3
- PyQt5
- CherryPy

## Demos
### SQL injection
Discovered around 1998, SQL injection is less common than it was in the late
2000's. The vulnerability manifests when a SQL query is not handled safely,
and a user's input is concatonated directly with the query string. An attacker
can inject arbitrary SQL instructions to a database. [Bobby Tables](https://www.xkcd.com/327/)
is the go-to example for this exploit.

### Eavesdropping
While eavesdropping can be either active or passive, this demo uses wireshark
to passively pick packet data out of a simple TCP chat application. The client
can send data to the server in with or without encryption, which is illustrated
when the wireshark wrapper *sniffer.py* displays the captured packet data.

### Steganography
In contrast to encryption, steganography entails *concealing* data. This demo
uses image steganography to hide an ascii message inside the pixel data of a 
PNG file. By setting the least significant bit of each pixel to a bit of the
message, the colors that make up the image are encoded with the message. Where
encryption can be detected, the goal of steganography is to hide the data so
as not to be detected at all. It is used to sneak malware onto victim's
computers through advertisements, sometimes called *malvertisement*.


## Quickstart
*toolkit.py* is the main launcher, and is intended to wrap each individual demo
into a friendly GUI.
