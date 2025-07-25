# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109

from .document_feature import DocumentFeature
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentTableExtractionFeature(DocumentFeature):
    """
    Detecting and extracting data in tables.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentTableExtractionFeature object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_document.models.DocumentTableExtractionFeature.feature_type` attribute
        of this class is ``TABLE_EXTRACTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this DocumentTableExtractionFeature.
            Allowed values for this property are: "LANGUAGE_CLASSIFICATION", "TEXT_EXTRACTION", "TABLE_EXTRACTION", "KEY_VALUE_EXTRACTION", "DOCUMENT_CLASSIFICATION", "DOCUMENT_ELEMENTS_EXTRACTION"
        :type feature_type: str

        :param model_id:
            The value to assign to the model_id property of this DocumentTableExtractionFeature.
        :type model_id: str

        """
        self.swagger_types = {
            'feature_type': 'str',
            'model_id': 'str'
        }
        self.attribute_map = {
            'feature_type': 'featureType',
            'model_id': 'modelId'
        }
        self._feature_type = None
        self._model_id = None
        self._feature_type = 'TABLE_EXTRACTION'

    @property
    def model_id(self):
        """
        Gets the model_id of this DocumentTableExtractionFeature.
        Unique identifier custom model OCID that should be used for inference.


        :return: The model_id of this DocumentTableExtractionFeature.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this DocumentTableExtractionFeature.
        Unique identifier custom model OCID that should be used for inference.


        :param model_id: The model_id of this DocumentTableExtractionFeature.
        :type: str
        """
        self._model_id = model_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
