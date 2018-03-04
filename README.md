# Light It Up

* Communicates on a raw socket to the TP-Link Smart Bulb IP address on port 9999
* No authentication needed

Preset Smart Bulb Commands:  <br />
* on - turn light bulb on
* off - turn light bulb off
* gettime - set time of light bulb
* reboot - reboot light bulb
* tz - timezone of light bulb
* getstate - status of light bulb
* sysinfo - information of light bulb
* bright - set light bulb brightness
* cldfwinfo - information of light bulb firmware


## Author
* Kyle O'Meara
* Created during [GeekWeek 2017](https://g33kw33k.ca/en/index.html)

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
* Light It Up was tested on Kali Linux with Python 2.7
* TP-Link Smart Home Protocol encryption XOR key (171 or 0xab), see References.
* Reserve engineered the payloads of the light bulb communication to determine the commands accepted by light bulb (not-exhaustive).
* Key discovery, for light bulb, the first 4 bytes of the payload are 3 null bytes followed by the 4th byte being the length of the command.

## References

* [TP-Link Smart Plug](https://github.com/softScheck/tplink-smartplug)
* [TP-Link Smart Home API](https://github.com/plasticrake/tplink-smarthome-api)
