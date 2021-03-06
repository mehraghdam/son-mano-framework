"""
Copyright (c) 2015 SONATA-NFV
ALL RIGHTS RESERVED.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Neither the name of the SONATA-NFV [, ANY ADDITIONAL AFFILIATION]
nor the names of its contributors may be used to endorse or promote
products derived from this software without specific prior written
permission.

This work has been performed in the framework of the SONATA project,
funded by the European Commission under Grant number 671517 through
the Horizon 2020 and 5G-PPP programmes. The authors would like to
acknowledge the contributions of their colleagues of the SONATA
partner consortium (www.sonata-nfv.eu).
"""

import logging
import yaml
import time
import os
from sonmanobase import messaging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("son-mano-fakeslm")

LOG.setLevel(logging.DEBUG)
logging.getLogger("son-mano-base:messaging").setLevel(logging.INFO)


class fakeslm(object):

    def __init__(self):

        self.name = 'fake-slm'
        self.version = '0.1-dev'
        self.description = 'description'

        LOG.info("Starting SLM1:...")

        # create and initialize broker connection
        self.manoconn = messaging.ManoBrokerRequestResponseConnection(self.name)

        self.publish_nsd()
        #self.manoconn.subscribe(self.publish_nsd, "specific.manager.registry.ssm.instantiate")
        self.end = False

        self.run()

    def run(self):

        # go into infinity loop

        while self.end == False:
            time.sleep(1)


    def publish_nsd(self):
        # response = yaml.load(str(response))
        # if type(response) == dict:
        #     if response['status'] == 'Instantiated':
        #         LOG.info("instantiation done- uuid: {0}".format(response['uuid']))
        #         self.end = True
        #     else:
        #         LOG.error("SSM instantiation failed.==> '{0}'".format(response['error']))
        #         self.end = True
        #
        #     if response['name']=='sonssmplacement1':
        message = {'NSD':'nsd','Topology':'topology', 'uuid': 'fe9b968b-28d2-40bd-b326-74677477cc46'}
        self.manoconn.call_async(self.on_place_res,topic= "placement.executive.request", msg= yaml.dump(message))

    def on_place_res(self, ch, method, props, response):
        res = yaml.load(response)
        print(res)


def main():
    fakeslm()


if __name__ == '__main__':
    main()
