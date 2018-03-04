# Light It Up

* Communicates on a raw socket to the TP-Link Smart Bulb IP address on port 9999
* No authentication needed

Preset Smart Bulb Commands:  <br />
* bulbon - turn light bulb on
* bulboff - turn light bulb off
* bulbgettime - set time of light bulb
* bulbreboot - reboot light bulb
* bulbtz - timezone of light bulb
* bulbgetstate - status of light bulb
* bulbsysinfo - information of light bulb
* bulbbright - set light bulb brightness


## Author
* Kyle O'Meara
* Created during GeekWeek 2017

## Dependencies
* No dependencies

## Usage
```
$ tplink_smart_bulb_communicator.py --help
```

Pass IP Address of Smart Light Bulb and command
```
$ tplink_smart_bulb_communicator.py -t ipaddress -c command
```

## Notes
* Tested on TP-Link Light Bulb Model LB-110 
* Python script was tested on Kali Linux with Python 2.7
* TP-Link Smart Home Protocol encryption XOR key (171 or 0xab), see References.
* Reserve engineered the payloads of the light bulb communication to determine the commands accepted by light bulb (not-exhaustive).
* Key discovery, for light bulb, is that the first 4 bytes of the payload are 3 null bytes followed by the 4th byte being the length of the command.

## References

* [TP-Link Smart Plug](https://github.com/softScheck/tplink-smartplug)
* [TP-Link Smart Home API](https://github.com/plasticrake/tplink-smarthome-api)
