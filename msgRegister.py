from pathlib import Path

from rosbags.typesys import get_types_from_msg
from rosbags.typesys import Stores, get_typestore

add_types = {}

#UWB
msg_uwbFrame3block = Path('./sensors_msg/msg/UwbFrame3Block.msg').read_text()
msg_uwbFrame3 = Path('./sensors_msg/msg/UwbFrame3.msg').read_text()
add_types.update(get_types_from_msg(msg_uwbFrame3block, 'sensors_msg/msg/UwbFrame3Block'))
add_types.update(get_types_from_msg(msg_uwbFrame3, 'sensors_msg/msg/UwbFrame3'))

#CGI1010
msg_CGI1010 = Path('./sensors_msg/msg/Gpfpd.msg').read_text()
add_types.update(get_types_from_msg(msg_CGI1010, 'sensors_msg/msg/Gpfpd'))
msg_CGI1010_NEW = Path('./sensors_msg/msg/GpfpdNEW.msg').read_text()
add_types.update(get_types_from_msg(msg_CGI1010_NEW, 'sensors_msg/msg/GpfpdNEW'))
#GNSS
msg_GNSS1RAWXblock = Path('./sensors_msg/msg/GNSS1RAWXblock.msg').read_text()
msg_GNSS1SATblock = Path('./sensors_msg/msg/GNSS1SATblock.msg').read_text()
msg_GNSS1HPPOSLLHblock = Path('./sensors_msg/msg/GNSS1HPPOSLLHblock.msg').read_text()
msg_GNSS = Path('./sensors_msg/msg/GNSSmsg.msg').read_text()
add_types.update(get_types_from_msg(msg_GNSS1RAWXblock, 'sensors_msg/msg/GNSS1RAWXblock'))
add_types.update(get_types_from_msg(msg_GNSS1SATblock, 'sensors_msg/msg/GNSS1SATblock'))
add_types.update(get_types_from_msg(msg_GNSS1HPPOSLLHblock, 'sensors_msg/msg/GNSS1HPPOSLLHblock'))
add_types.update(get_types_from_msg(msg_GNSS, 'sensors_msg/msg/GNSSmsg'))

#IMU
msg_imu = Path('./sensors_msg/msg/imu.msg').read_text()
add_types.update(get_types_from_msg(msg_imu, 'sensors_msg/msg/Imu'))




#yi
GnssFrame = Path('./sensors_interfaces/msg/GnssFrame.msg').read_text()
MtiFrame = Path('./sensors_interfaces/msg/MtiFrame.msg').read_text()
MtiStatusFrame = Path('./sensors_interfaces/msg/MtiStatusFrame.msg').read_text()
UwbFrame3 = Path('./sensors_interfaces/msg/UwbFrame3.msg').read_text()
add_types.update(get_types_from_msg(GnssFrame, 'sensors_interfaces/msg/GnssFrame'))
add_types.update(get_types_from_msg(MtiFrame, 'sensors_interfaces/msg/MtiFrame'))
add_types.update(get_types_from_msg(MtiStatusFrame, 'sensors_interfaces/msg/MtiStatusFrame'))
add_types.update(get_types_from_msg(UwbFrame3, 'sensors_interfaces/msg/UwbFrame3'))

MtiGnssFrame = Path('./sensors_interfaces/msg/MtiGnssFrame.msg').read_text()
OpticalFrame = Path('./sensors_interfaces/msg/OpticalFrame.msg').read_text()
UwbStatusFrame = Path('./sensors_interfaces/msg/UwbStatusFrame.msg').read_text()
add_types.update(get_types_from_msg(MtiGnssFrame, 'sensors_interfaces/msg/MtiGnssFrame'))
add_types.update(get_types_from_msg(OpticalFrame, 'sensors_interfaces/msg/OpticalFrame'))
add_types.update(get_types_from_msg(UwbStatusFrame, 'sensors_interfaces/msg/UwbStatusFrame'))
UwbFrame3Block = Path('./sensors_interfaces/msg/UwbFrame3Block.msg').read_text()
add_types.update(get_types_from_msg(UwbFrame3Block, 'sensors_interfaces/msg/UwbFrame3Block'))

typestore = get_typestore(Stores.ROS2_HUMBLE)
typestore.register(add_types)



