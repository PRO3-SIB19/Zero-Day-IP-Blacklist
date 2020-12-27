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

from heralding.reporting.base_logger import BaseLogger

class TcpLogger(BaseLogger):

    def __init__(self,ip_address,port):
        super().__init__()

    
    def handle_auth_log(self, data):

        print(data["timestamp"]+";"+
            data["source_ip"]+";"+
            str(data["source_port"])+";"+
            data["destination_ip"]+";"+
            str(data["destination_port"])
        )