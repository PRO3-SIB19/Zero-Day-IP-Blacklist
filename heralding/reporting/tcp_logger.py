# Copyright (C) 2017 Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket

from heralding.reporting.base_logger import BaseLogger

class TcpLogger(BaseLogger):

    def __init__(self,ip_address,port):
        super().__init__()

    
    def handle_auth_log(self, data):

        sendstring = data["timestamp"] + ";"
        sendstring += data["source_ip"] + ";"
        sendstring += str(data["source_port"])+";"
        sendstring += data["destination_ip"]+";"
        sendstring += str(data["destination_port"])+";"
        sendstring += data["protocol"]

        print(sendstring)

        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 12345        # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(bytes(sendstring, 'utf-8'))

