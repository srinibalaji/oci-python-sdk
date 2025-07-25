# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BarCode(object):
    """
    A single bar code.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BarCode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param confidence:
            The value to assign to the confidence property of this BarCode.
        :type confidence: float

        :param value:
            The value to assign to the value property of this BarCode.
        :type value: str

        :param code_type:
            The value to assign to the code_type property of this BarCode.
        :type code_type: str

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this BarCode.
        :type bounding_polygon: oci.ai_document.models.BoundingPolygon

        """
        self.swagger_types = {
            'confidence': 'float',
            'value': 'str',
            'code_type': 'str',
            'bounding_polygon': 'BoundingPolygon'
        }
        self.attribute_map = {
            'confidence': 'confidence',
            'value': 'value',
            'code_type': 'codeType',
            'bounding_polygon': 'boundingPolygon'
        }
        self._confidence = None
        self._value = None
        self._code_type = None
        self._bounding_polygon = None

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this BarCode.
        the confidence score between 0 and 1.


        :return: The confidence of this BarCode.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this BarCode.
        the confidence score between 0 and 1.


        :param confidence: The confidence of this BarCode.
        :type: float
        """
        self._confidence = confidence

    @property
    def value(self):
        """
        **[Required]** Gets the value of this BarCode.
        the bar code value.


        :return: The value of this BarCode.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this BarCode.
        the bar code value.


        :param value: The value of this BarCode.
        :type: str
        """
        self._value = value

    @property
    def code_type(self):
        """
        Gets the code_type of this BarCode.
        the encoding schema of bar code.


        :return: The code_type of this BarCode.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """
        Sets the code_type of this BarCode.
        the encoding schema of bar code.


        :param code_type: The code_type of this BarCode.
        :type: str
        """
        self._code_type = code_type

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this BarCode.

        :return: The bounding_polygon of this BarCode.
        :rtype: oci.ai_document.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this BarCode.

        :param bounding_polygon: The bounding_polygon of this BarCode.
        :type: oci.ai_document.models.BoundingPolygon
        """
        self._bounding_polygon = bounding_polygon

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
