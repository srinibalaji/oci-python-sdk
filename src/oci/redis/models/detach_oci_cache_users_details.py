# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220315


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachOciCacheUsersDetails(object):
    """
    OCI cache user details to be detached with a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachOciCacheUsersDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oci_cache_users:
            The value to assign to the oci_cache_users property of this DetachOciCacheUsersDetails.
        :type oci_cache_users: list[str]

        """
        self.swagger_types = {
            'oci_cache_users': 'list[str]'
        }
        self.attribute_map = {
            'oci_cache_users': 'ociCacheUsers'
        }
        self._oci_cache_users = None

    @property
    def oci_cache_users(self):
        """
        **[Required]** Gets the oci_cache_users of this DetachOciCacheUsersDetails.
        List of OCI cache user unique IDs (OCIDs).


        :return: The oci_cache_users of this DetachOciCacheUsersDetails.
        :rtype: list[str]
        """
        return self._oci_cache_users

    @oci_cache_users.setter
    def oci_cache_users(self, oci_cache_users):
        """
        Sets the oci_cache_users of this DetachOciCacheUsersDetails.
        List of OCI cache user unique IDs (OCIDs).


        :param oci_cache_users: The oci_cache_users of this DetachOciCacheUsersDetails.
        :type: list[str]
        """
        self._oci_cache_users = oci_cache_users

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
