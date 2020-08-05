# -*- coding: utf-8 -*-
from pprint import pprint
import pytest
from ibm_zos_ims.tests.functional.module_utils.ims_test_dbrc_utils import DBRCInputParameters as ip # pylint: disable=import-error
from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.ims_module_error_messages import DBRCErrorMessages as em # pylint: disable=import-error

__metaclass__ = type


"""
Author: An Lam
"""

def test_ims_dbrc_valid_1(ansible_zos_module):
    hosts = ansible_zos_module
    results = hosts.all.ims_dbrc(
        command = [
            "INIT.DB DBD(TESTDB)",
            "LIST.DBDS DBD(TESTDB)",
            # "CHANGE.DB DBD(TESTDB) ALTER NOAUTH ICREQ  TYPEIMS NORAND",
            "DELETE.DB DBD(TESTDB)"],
        steplib = ip.STEPLIB,
        dynalloc = ip.DYNALLOC, 
        genjcl = ip.GENJCL,
        dbdlib = ip.DBDLIB
    )
    for result in results.contacted.values():
        pprint(result)
        assert result['changed'] == True
        assert result['rc'] <= 4
        assert result['msg'] == em.SUCCESS_MSG

def test_ims_dbrc_valid_1a(ansible_zos_module):
    hosts = ansible_zos_module
    results = hosts.all.ims_dbrc(
        command = "DELETE.DB DBD(TESTDB)",
        steplib = ip.STEPLIB,
        dynalloc = ip.DYNALLOC, 
        genjcl = ip.GENJCL,
        dbdlib = ip.DBDLIB,
        max_rc = 12
    )
    for result in results.contacted.values():
        pprint(result)
        # assert result['rc'] <= 4
        assert result['msg'] == em.SUCCESS_MSG

def test_ims_dbrc_sample(ansible_zos_module):
    hosts = ansible_zos_module
    results = hosts.all.ims_dbrc(
        command=[
            "LIST.RECON STATUS", 
            "LIST.DB ALL",
            "LIST.BKOUT ALL",
            "LIST.LOG",
            "LIST.CAGRP"],
        steplib=ip.STEPLIB,
        dbdlib=ip.DBDLIB,
        genjcl=ip.GENJCL,
        recon1=ip.RECON1,
        recon2=ip.RECON2,
        recon3=ip.RECON3
    )
    for result in results.contacted.values():
        pprint(result)
        assert result['rc'] <= 4
        assert result['msg'] == em.SUCCESS_MSG

def test_ims_dbrc_valid_2_commands(ansible_zos_module):
    hosts = ansible_zos_module
    results = hosts.all.ims_dbrc(
        command = ["LIST.RECON STATUS", "LIST.DB ALL "],
        steplib=ip.STEPLIB,
        dynalloc=ip.DYNALLOC,
        genjcl=ip.GENJCL,
        dbdlib=ip.DBDLIB,
        recon1=ip.RECON1,
        recon2=ip.RECON2,
        recon3=ip.RECON3
    )
    for result in results.contacted.values():
        pprint(result)
        assert result['rc'] <= 4
        assert result['msg'] == em.SUCCESS_MSG

def test_ims_dbrc_valid_3_commands(ansible_zos_module):
    hosts = ansible_zos_module
    results = hosts.all.ims_dbrc(
        command = ["LIST.RECON STATUS", "LIST.DB ALL", "LIST.DBDS DBD(CUSTOMER)"],
        steplib=ip.STEPLIB,
        dynalloc=ip.DYNALLOC,
        genjcl=ip.GENJCL,
        dbdlib=ip.DBDLIB,
        recon1=ip.RECON1,
        recon2=ip.RECON2,
        recon3=ip.RECON3
    )
    for result in results.contacted.values():
        pprint(result)
        assert result['rc'] <= 4
        assert result['msg'] == em.SUCCESS_MSG