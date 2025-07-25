# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CollectTracesDetails(object):
    """
    Details for collecting DB traces and alert logs
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CollectTracesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_name:
            The value to assign to the bucket_name property of this CollectTracesDetails.
        :type bucket_name: str

        :param namespace:
            The value to assign to the namespace property of this CollectTracesDetails.
        :type namespace: str

        :param object_name_prefix:
            The value to assign to the object_name_prefix property of this CollectTracesDetails.
        :type object_name_prefix: str

        """
        self.swagger_types = {
            'bucket_name': 'str',
            'namespace': 'str',
            'object_name_prefix': 'str'
        }
        self.attribute_map = {
            'bucket_name': 'bucketName',
            'namespace': 'namespace',
            'object_name_prefix': 'objectNamePrefix'
        }
        self._bucket_name = None
        self._namespace = None
        self._object_name_prefix = None

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CollectTracesDetails.
        Name of the bucket containing the file.


        :return: The bucket_name of this CollectTracesDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CollectTracesDetails.
        Name of the bucket containing the file.


        :param bucket_name: The bucket_name of this CollectTracesDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this CollectTracesDetails.
        Object Storage namespace.


        :return: The namespace of this CollectTracesDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this CollectTracesDetails.
        Object Storage namespace.


        :param namespace: The namespace of this CollectTracesDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def object_name_prefix(self):
        """
        **[Required]** Gets the object_name_prefix of this CollectTracesDetails.
        Object name prefix.


        :return: The object_name_prefix of this CollectTracesDetails.
        :rtype: str
        """
        return self._object_name_prefix

    @object_name_prefix.setter
    def object_name_prefix(self, object_name_prefix):
        """
        Sets the object_name_prefix of this CollectTracesDetails.
        Object name prefix.


        :param object_name_prefix: The object_name_prefix of this CollectTracesDetails.
        :type: str
        """
        self._object_name_prefix = object_name_prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
