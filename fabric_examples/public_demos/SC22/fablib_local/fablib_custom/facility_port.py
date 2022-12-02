#!/bin/python3

import os

import json
import time
import paramiko


import pandas as pd
from tabulate import tabulate

from fabrictestbed.util.constants import Constants
from concurrent.futures import ThreadPoolExecutor

from fabrictestbed.slice_editor import (
    ExperimentTopology,
    Capacities
)


class FacilityPort_Custom():
    
    def place_holder():
        pass
   


  




# Add methods to FABlib Classes
from fabrictestbed_extensions.fablib.faclity_port import FacilityPort


#fablib.FacilityPort
#setattr(FacilityPort, 'get_vlan', FacilityPort_Custom.get_vlan)




