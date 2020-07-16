#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) IBM Corporation 2019, 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r'''
---

module: ims_dbrc

short_description: Submit IMS Database Recovery Control (DBRC) Commands
version_added: "2.9"

description:
  - Use DBRC to record and manage information that is stored in a set of VSAM
    data sets that are collectively called the Recovery Control (RECON) data set.
  - Based on this information, you can use DBRC to advise IMS about how to proceed
    for certain IMS actions.
author:
  - Omar Elbarmawi (@oelbarmawi)
options:
  command:
    description:
      - This is the (well-formatted) DBRC command to submit.
    type: list
    required: true
  dbdlib:
    description:
      - The data set that contains the database descriptions for the databases that are under the control of DBRC.
    type: str
    required: false
  dynalloc:
    description:
      - The DYNALLOC data set that will be used to complete the DBRC execution.
      - Required if `recon` is not specified.
    type: str
    required: false
  genjcl:
    description:
      - The PDS, which contains the JCL and control statements for the utility that DBRC uses to generate a job.
    type: str
    required: false
  recon1:
    description:
      - The RECON1 data set that will be used to complete the DBRC execution.
      - Required if `dynalloc` is not specified.
    type: str
    required: false
  recon2:
    description:
      - The RECON2 data set that will be used to complete the DBRC execution.
    type: str
    required: false
  recon3:
    description:
      - The RECON3 data set that will be used to complete the DBRC execution.
    type: str
    required: false
  steplib:
    description:
      - List of STEPLIB datasets that contain the IMS nucleus and the required action modules.
    type: list
    required: true
'''

EXAMPLES = '''
- name: Sample DBRC Single Command
  ims_dbrc:
    command: LIST.RECON STATUS
    steplib: IMSBANK.IMS1.SDFSRESL
    dynalloc: IMSTESTL.IMS1.DYNALLOC
    genjcl: IMSTESTL.IMS1.GENJCL
    dbdlib: IMSTESTL.IMS1.DBDLIB

- name: Sample DBRC Multiple Commands
  ims_dbrc:
    command: 
      - LIST.RECON STATUS
      - LIST.DB ALL
      - LIST.DBDS DBD(CUSTOMER)
    steplib: IMSBANK.IMS1.SDFSRESL
    dynalloc: IMSTESTL.IMS1.DYNALLOC
    genjcl: IMSTESTL.IMS1.GENJCL
    dbdlib: IMSTESTL.IMS1.DBDLIB

- name: Sample DBRC Multiple Commands with RECON specified
  ims_dbrc:
    command: 
      - LIST.RECON STATUS
      - LIST.DB ALL
    steplib: IMSBANK.IMS1.SDFSRESL
    genjcl: IMSTESTL.IMS1.GENJCL
    recon1: IMSBANK.IMS1.RECON1
    recon2: IMSBANK.IMS1.RECON2
    recon3: IMSBANK.IMS1.RECON3
    dbdlib: IMSTESTL.IMS1.DBDLIB
'''

RETURN = '''
changed:
  description:
    Indicates if this module effectively modified the target state.
  type: boolean
  returned: always
dbrc_output:
  description:
    The output provided by the specified DBRC Command(s).
  type: list
  returned: sometimes
  contains:
    command:
      description:
        The original command input to the module.
      returned: always
      type: str
    data:
      description:
        Parsed fields from the output content that is mapped to its corresponding value.
      returned: always
      type: dict
    output_content:
      description:
        Unformatted output response from the corresponding DBRC command.
      returned: always
      type: str
failed:
  description:
    Indicates the outcome of the module.
  type: boolean
  returned: always
msg:
  description:
    The output message that the `ims_dbrc` module generates.
  type: str
  returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.IMSDbrc.IMSDbrc import IMSDbrc  # pylint: disable=import-error
from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.ims_module_error_messages import DBRCErrorMessages as em # pylint: disable=import-error

def run_module():
  global module
  module_args = dict(
    command=dict(type='list', required=True),
    dbdlib=dict(type='str', required=False),
    dynalloc=dict(type='str', required=False),
    genjcl=dict(type='str', required=False),
    recon1=dict(type='str', required=False),
    recon2=dict(type='str', required=False),
    recon3=dict(type='str', required=False),
    steplib=dict(type='list', required=True)
  )

  result = dict(
    changed=False,
    msg='',
    rc='',
    failed=True,
    dbrc_output={},
    unformatted_output=[]
  )
  
  module = AnsibleModule(
    argument_spec=module_args,
    supports_check_mode=True
  )

  try:
    response = IMSDbrc(
      commands=module.params['command'],
      steplib=module.params['steplib'],
      dynalloc=module.params['dynalloc'],
      dbdlib=module.params['dbdlib'],
      genjcl=module.params['genjcl'],
      recon1=module.params['recon1'],
      recon2=module.params['recon2'],
      recon3=module.params['recon3']).execute()

    result['dbrc_output'] = response['dbrc_fields']
    result['unformatted_output'] = response['original_output']
    result['failed'] = response['failure_detected']
    result['rc'] = response['rc']
    result['changed'] = response['changed']

    if not result['dbrc_output']:
      if response['rc'] and int(response['rc']) > 4:
        result['msg'] = response['error'] if response['error'] else em.FAILURE_MSG
      else:
        result['msg'] = em.EMPTY_OUTPUT_MSG

      if response['error']:
        print("An error occurred:", response['error'])

      result['changed'] = False
      module.fail_json(**result)

    elif result['failed']:
      result['msg'] = em.FAILURE_MSG
      module.fail_json(**result)

    else:
      result['msg'] = em.SUCCESS_MSG

  except Exception as e:
    result['msg'] = repr(e)
    module.fail_json(**result)
    
  finally:
    # _delete_data_set(sysin_data_set)
    pass

  module.exit_json(**result)

def main():
  run_module()

if __name__ == '__main__':
  main()