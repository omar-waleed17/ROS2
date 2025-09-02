import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/omarwaleed/turtle_catch_ws/install/turtle_catch'
