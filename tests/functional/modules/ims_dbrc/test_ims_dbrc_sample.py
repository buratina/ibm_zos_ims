# -*- coding: utf-8 -*-

from pprint import pprint
import pytest
from ibm_zos_ims.tests.functional.module_utils.ims_test_gen_utils import DBRCInputParameters as ip # pylint: disable=import-error
from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.ims_module_error_messages import DBRCErrorMessages as em # pylint: disable=import-error
__metaclass__ = type

def test_ims_dbrc_sample(ansible_zos_module):
    hosts = ansible_zos_module
    results = hosts.all.ims_dbrc(
        command=[
            "LIST.RECON STATUS", 
            "LIST.DB ALL",
            "LIST.BKOUT ALL",
            "LIST.LOG",
            "LIST.CAGRP"],
        # command=['GENJCL.ARCHIVE SSID(IMS1) OLDS(DFSOLP01, DFSOLP02)'],
        steplib=ip.STEPLIB, dbdlib=ip.DBDLIB, genjcl=ip.GENJCL,
        recon1=ip.RECON1, recon2=ip.RECON2, recon3=ip.RECON3
    )
    for result in results.contacted.values():
        pprint(result)
        assert result['msg'] == em.SUCCESS_MSG
        # assert False