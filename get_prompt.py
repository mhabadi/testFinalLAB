from netmiko import Netmiko
devices=[]
for i in range (3):
    ip=f"192.168.1.{101+i}"

    device={"device_type":"cisco_ios","ip":ip,# R1 mgmt Interface
        "username":"student",
        "password":"Meilab123",
        "port":"22",
        "secret":"cisco",
        }
    devices.append(device)


for device in devices:
    net_connect=Netmiko(**device)
    print(f"Default prompt: {net_connect.find_prompt()}")

    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")

    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}\n")
