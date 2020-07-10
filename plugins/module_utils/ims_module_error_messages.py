class ErrorMessages():
    BATCH_FAILURE_MSG = "Failed. Check 'msg' field in 'ims_output' for more details."
    INVALID_CHAR_IN_CMD = "Invalid character(s) found in command."
    INVALID_MEMBER_LIST_TYPE = "Received unexpected type in member_list. Member_list is expected to be a list of strings specifying the source members and/or single-entry dicts where the key specifies the source member as a str and the value specifies the target name as a str."
    INVALID_MEMBER_NAME = "Received invalid name for a data set member: "
    INVALID_PLEX_MSG = "Malformed Plex."
    INVALID_ROUTE_MSG = "One or more routes specified are malformed."
    JSON_DECODE_ERROR_MSG = "Unable to decode string into JSON."
    MISSING_COMMAND = "Missing required arguments: command"
    MISSING_PLEX = "Missing required arguments: plex"
    NO_OUTPUT_MSG = "No job output was found."
    NO_RC_MSG = "Error verifying return code."
    NON_ZERO_RC_MSG = "Non-zero return code returned."
    NON_ZERO_ERR_MSG = "Refer to IMS return codes."
    REXX_RETURN_CODE_MSG = "The following REXX error code was returned: "
    SUBMISSION_ERROR_MSG = "Error submitting IMS Command."
    SUCCESS_MSG = "Success"