# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SignatureSubTypeDetails(object):
    """
    Signature Document Element Extraction model sub type details
    """

    #: A constant which can be used with the model_sub_type property of a SignatureSubTypeDetails.
    #: This constant has a value of "QR_BAR_CODE"
    MODEL_SUB_TYPE_QR_BAR_CODE = "QR_BAR_CODE"

    #: A constant which can be used with the model_sub_type property of a SignatureSubTypeDetails.
    #: This constant has a value of "SIGNATURE"
    MODEL_SUB_TYPE_SIGNATURE = "SIGNATURE"

    def __init__(self, **kwargs):
        """
        Initializes a new SignatureSubTypeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_sub_type:
            The value to assign to the model_sub_type property of this SignatureSubTypeDetails.
            Allowed values for this property are: "QR_BAR_CODE", "SIGNATURE"
        :type model_sub_type: str

        """
        self.swagger_types = {
            'model_sub_type': 'str'
        }
        self.attribute_map = {
            'model_sub_type': 'modelSubType'
        }
        self._model_sub_type = None

    @property
    def model_sub_type(self):
        """
        **[Required]** Gets the model_sub_type of this SignatureSubTypeDetails.
        The model sub type for DOCUMENT_ELEMENTS_EXTRACTION.
        The allowed values are:
          - `QR_BAR_CODE`
          - `SIGNATURE`

        Allowed values for this property are: "QR_BAR_CODE", "SIGNATURE"


        :return: The model_sub_type of this SignatureSubTypeDetails.
        :rtype: str
        """
        return self._model_sub_type

    @model_sub_type.setter
    def model_sub_type(self, model_sub_type):
        """
        Sets the model_sub_type of this SignatureSubTypeDetails.
        The model sub type for DOCUMENT_ELEMENTS_EXTRACTION.
        The allowed values are:
          - `QR_BAR_CODE`
          - `SIGNATURE`


        :param model_sub_type: The model_sub_type of this SignatureSubTypeDetails.
        :type: str
        """
        allowed_values = ["QR_BAR_CODE", "SIGNATURE"]
        if not value_allowed_none_or_none_sentinel(model_sub_type, allowed_values):
            raise ValueError(
                f"Invalid value for `model_sub_type`, must be None or one of {allowed_values}"
            )
        self._model_sub_type = model_sub_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
