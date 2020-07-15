# -*- coding: utf-8 -*-

# Copyright (c) IBM Corporation 2020
# LICENSE: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

ANSIBLE_METADATA = {
  'metadata_version': '1.1',
  'status': ['preview'],
  'supported_by': 'community'
}

DOCUMENTATION = r'''
---

module: ims_catalog_populate
short_description: Add datasets to the IMS Catalog
version_added: "2.9"
description:
  - The IMS Catalog Purge  utility DFS3PU10 removes the segments that represent a DBD or PSB instance, 
    all instances of a DBD version, or an entire DBD or PSB record from the IMS catalog. You can also
options:
  mode:
    description:
      - Indicates what mode the Catalog Populate Utility should be run as
    type: str
    required: true
    choices:
      - LOAD
      - UPDATE
      - READ
  irlm_enabled:
    description:
      - Indicates if IRLM is used
    type: bool
    required: false
  irlm_id:
    description:
      - The IRLM id if IRLM is enabled
    type: str
    required: false
  reslib:
    description:
      - Points to an authorized library that contains the IMS SVC modules. 
        The reslib parameter can also be specified in the target inventory's environment_vars.
        The reslib input parameter to the module will take precedence over the value specified in the environment_vars
    type: str
    required: false
  buffer_pool_param_dataset:
    description:
      - Defines the buffer pool parameters data set.
    type: str
    required: true
  primary_log_dataset:
    description:
      - Defines the primary IMS log data set.
    type: dict
    required: true
    suboptions:
      dataset_name:
        description:
          - Describes the name of the dataset
        type: str
        required: true
      disposition:
        description: 
          - Status of dataset
        type: str
        required: false
        choices:
          - NEW
          - OLD
          - SHR
          - EXCL
      record_format:
        description:
          - the record format #Need to expand this
        type: str
        required: false
        choices:
          - FB
          - VB
          - FBA
          - VBA
          - U
      record_length:
        description:
          - the logical record length in bytes #Need to expand this
        type: int
        required: false
      block_size:
        description:
          - the block size #Need to expand this
        type: int
        required: false
      primary:
        description:
          - The amount of primary space to allocate for the dataset
        type: int
        required: false
      primary_unit:
        description:
          - The unit of size to use when specifying primary space
        type: str
        required: false
      secondary:
        description:
          - The amount of secondary space to allocate for the dataset
        type: int
        required: false
      secondary_unit:
        description:
          - The unit of size to sue when specifying secondary space.
        type: str
        required: false
      normal_disposition:
        description:
          - What to do with the dataset after normal termination
        type: str
        required: false
        choices:
          - DELETE
          - KEEP
          - CATLG
          - UNCATLG
      abnormal_disposition:
        description:
          - What to do with the dataset after abnormal termination
        type: str
        required: false
        choices:
          - DELETE
          - KEEP
          - CATLG
          - UNCATLG
      type:
        description: 
          - The type of dataset
        type: str
        required: false
        choices:
          - SEQ
          - BASIC
          - LARGE
          - PDS
          - PDSE
          - LIBRARY
          - LDS
          - RRDS
          - ESDS
          - KSDS
      storage_class:
        description:
          - The storage class for an SMS-managed dataset
        type: str
        required: false
      data_class:
        description:
        type: str
        required: false
      management_class:
        description:
        type: str
        required: false
      key_length:
        description:
        type: int
        required: false
      key_offset:
        description:
        type: int
        required: false
      volumes:
        description:
        type: list
        required: false
        elements: str
      dataset_key_label:
        description: 
        type: str
        required: false
      key_label1:
        description:
        type: str
        required false
      key_encoding1:
        description:
        type: str
        required: false
      key_label2:
        description:
        type: str
        required false
      key_encoding2:
        description:
        type: str
        required: false
  psb_lib:
    description:
      - Defines IMS.PSBLIB dataset
    type: str
    required: true
  dbd_lib:
    description:
      - Defines IMS.DBDLIB datasets
    type: str
    required: true
  proclib:
    description:
      - Defines the IMS.PROCLIB data set that contains the DFSDFxxx member that 
        defines various attributes of the IMS catalog that are required by the utility.
    type: str
    required: true
  steplib:
    description:
      - Points to IMS.SDFSRESL, which contains the IMS nucleus and required IMS modules. 
    type: str
    required: true
  mode:
    description:
      - Determines which mode the utility runs in. ANALYSIS mode generates delete statements based on the
        retention criteria and places them in the SYSUT1 datset. PURGE mode executes delete statements in the
        SYSUT1 dataset. BOTH mode performs ANALYSIS and PURGE mode consecutively. 
    type: str
    required: true
    choices:
      - ANALYSIS
      - PURGE
      - BOTH
  delete_dbd_by_version:
    description:
      - Delete DBD instances based on name and version specified. If ANALYSIS mode is specified, it will 
        generate DELETE DBD statements in the SYSUT1 dataset along with any other delete statements based off the
        retention criteria. If PURGE or BOTH mode is specified, it will write the delete statements to the SYSUT1 dataset 
        and then execute them. 
    type: list
    required: false
    elements: dict
    suboptions:
      member_name:
        description: 
          - The 8 character name of the DBD that you are deleting a version from.
        type: str
        required: true
      version_number:
        description:
          - The version number of the DBD that you are deleting. The value must match the version number
            that is specified on the DBVER keyword in the DBD generation statement of the version that 
            you are deleting
        type: int
        required: true
  update_retention_criteria:
    description:
      - Use this statement to set the retention criteria for dbd or psb records in the catalog database. 
        You can submit any number of update statements. You cannot specify this option if PURGE mode is 
        selected. If used with any other mode options, it will update the retention criteria first.
    type: list
    required: false
    elements: dict
    suboptions:
      resource:
        description:
          - Specifies whether a DBD or PSB should be updated
        choices:
          - DBD
          - PSB
        type: str
        required: true
      member_name:
        description:
          - The 8 character IMS name of the DBD or PSB resource. Wildcards are supported
        type: str
        required: true
      instances:
        description: 
          - The number of instances of a DBD or PSB that must be retained in the DBD or PSB record
        type: int
        required: true
      days: 
        description:
          - The number of days that an instance of a DBD or PSB must be retained before it can be purged
        type: int
        required: false
  delete:
    description:
      - Specifies a DBD or PSB instance or an entire DBD or PSB record to delete from the IMS catalog database.
        This option must be used with PURGE mode and overrides any retention criteria, hence you can remove any 
        DBD or PSB that would not otherwise be eligible for deletion
    type: list:
    required: false
    elements: dict
    suboptions:
      resource:
        description:
          - Specify whether you want to delete a DBD or PSB
        type: str
        required: true
        choices:
          - DBD
          - PSB
      member_name:
        description:
          - The 8 character IMS name of the DBD or PSB resource. Wildcards are supported
        type: str
        required: true 
      time_stamp:
        description:
          - The ACB timestamp that identifies the specific DBD or PSB instance to purge
        type: int
        required: true
  managed_acbs:
    description:
      - Specifies whether deleting DBD and PSB instances from the IMS catalog causes the corresponding DBD and PSB
        instances in the IMS directory to be deleted. If 'analysis_mode' is true, the DBD and PSB instances
        will not be deleted from the IMS directory.
    type: bool
    required: false
  resource_chkp_freq:
    description:
      - Specifies the number of resource instances to be deleted or updated between checkpoints. Can be a 1-8 digit 
        numeric value from 1 to 99999999. The default value is 200.
      type: int
      required: false
  sysut1:
    description:
      - Defines the primary IMS log data set.
    type: dict
    required: true
    suboptions:
      dataset_name:
        description:
          - Describes the name of the dataset
        type: str
        required: true
      disposition:
        description: 
          - Status of dataset
        type: str
        required: false
        choices:
          - NEW
          - OLD
          - SHR
          - EXCL
      block_size:
        description:
          - The block size 
        type: int
        required: false
      primary:
        description:
          - The amount of primary space to allocate for the dataset
        type: int
        required: false
      primary_unit:
        description:
          - The unit of size to use when specifying primary space
        type: str
        required: false
      secondary:
        description:
          - The amount of secondary space to allocate for the dataset
        type: int
        required: false
      secondary_unit:
        description:
          - The unit of size to sue when specifying secondary space.
        type: str
        required: false
      normal_disposition:
        description:
          - What to do with the dataset after normal termination
        type: str
        required: false
        choices:
          - DELETE
          - KEEP
          - CATLG
          - UNCATLG
      abnormal_disposition:
        description:
          - What to do with the dataset after abnormal termination
        type: str
        required: false
        choices:
          - DELETE
          - KEEP
          - CATLG
          - UNCATLG
      type:
        description: 
          - The type of dataset
        type: str
        required: false
        choices:
          - SEQ
          - BASIC
          - LARGE
          - PDS
          - PDSE
          - LIBRARY
          - LDS
          - RRDS
          - ESDS
          - KSDS
      volumes:
        description:
          - A list of volume serials. When providing multiple volumes, processing will begin with
            the first volume in the provided list. Offline volumes are not considered.
        type: list
        required: false
        elements: str
author:
  - Jerry Li 
'''

EXAMPLES = r'''

'''

RETURN = r'''




'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.catalog.catalog import catalog # pylint: disable=import-error
from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.catalog_parser.catalog_parser import catalog_parser # pylint: disable=import-error


def run_module():
    module_args = dict(
      irlm_enabled=dict(type="bool", required=False),
      irlm_id=dict(type="str", required=False),
      reslib=dict(type="str", required=False),
      buffer_pool_param_dataset=dict(type="str", required=False),
      primary_log_dataset=dict(type="dict", required=False),
      psb_lib=dict(type="str", required=False),
      dbd_lib=dict(type="str", required=False),
      proclib=dict(type="str", required=False),
      steplib=dict(type="str", required=False),
      mode=dict(type="str", required=True),
      delete_dbd_by_version=dict(type="dict", required=False),
      sysut1=dict(type="dict", required=False),
      update_retention_criteria=dict(type="list", required=False),
      delete=dict(type="list", required=False),
      managed_acbs=dict(type="bool", required=False),
      resource_chkp_freq=dict(type="int", required=False)
    )

    global module
    module = AnsibleModule(
          argument_spec=module_args,
          supports_check_mode=True
      )
    
    result = {}
    result["changed"] = False

    parsed_args=catalog_parser(module, module.params, result).validate_purge_input()
    response = catalog(module, result, parsed_args).execute_catalog_purge()
    
  
    module.exit_json(**response)




def main():
    run_module()

if __name__ == '__main__':
    main()
