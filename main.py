import usb.core
import usb.util
import sys

VID = 0x1A86
PID = 0x7523

# находим наше устройство
dev = usb.core.find(idVendor=VID, idProduct=PID)

# оно было найдено?
if dev is None:
	raise ValueError('Device not found')

print(dev)
print()
print(f"bDeviceClass: {hex(dev.bDeviceClass)}")
print(f"bcdDevice: {hex(dev.bcdDevice)}")
print()

for cfg in dev:
	sys.stdout.write(f"bConfigurationValue: {str(cfg.bConfigurationValue)}\n")

	for intf in cfg:
		sys.stdout.write(f"\tbInterfaceNumber,bAlternateSetting:  {str(intf.bInterfaceNumber)},{str(intf.bAlternateSetting)}\n")

		for ep in intf:
			sys.stdout.write(f"\t\tbEndpointAddress: {str(ep.bEndpointAddress)}\n")

'''
# поставим активную конфигурацию. Без аргументов, первая же
# конфигурация будет активной
dev.set_configuration()

# получим экземпляр источника
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
	intf,
	# сопоставим первый источник данных
	custom_match = \
	lambda e: \
		usb.util.endpoint_direction(e.bEndpointAddress) == \
		usb.util.ENDPOINT_OUT)

assert ep is not None

# записываем данные
ep.write('test')
'''

