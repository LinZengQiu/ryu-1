# Copyright (C) 2014 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2014 YAMAMOTO Takashi <yamamoto at valinux co jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ryu import exception


# base classes

class _ExceptionBase(exception.RyuException):
    def __init__(self, result):
        self.result = result
        super(_ExceptionBase, self).__init__(result=result)


class UnexpectedMultiReply(_ExceptionBase):
    message = 'Unexpected Multi replies %(result)s'


class OFError(_ExceptionBase):
    message = 'OpenFlow errors %(result)s'
