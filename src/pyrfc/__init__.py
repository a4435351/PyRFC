# Copyright 2013 SAP AG.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an.
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific.
# language governing permissions and limitations under the License.

# import from internal modules that they could be directly imported from
# the pyrfc package
from pyrfc._exception import RFCError, RFCLibError,\
    CommunicationError, LogonError,\
    ABAPApplicationError, ABAPRuntimeError,\
    ExternalAuthorizationError, ExternalApplicationError, ExternalRuntimeError

from pyrfc._pyrfc import get_nwrfclib_version, Connection, TypeDescription, FunctionDescription, Server

__version__ = "1.9.91"

# TODO: define __all__ variable
#
