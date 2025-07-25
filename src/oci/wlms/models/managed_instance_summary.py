# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceSummary(object):
    """
    The summary information about a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedInstanceSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagedInstanceSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstanceSummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this ManagedInstanceSummary.
        :type host_name: str

        :param server_count:
            The value to assign to the server_count property of this ManagedInstanceSummary.
        :type server_count: int

        :param plugin_status:
            The value to assign to the plugin_status property of this ManagedInstanceSummary.
        :type plugin_status: str

        :param time_created:
            The value to assign to the time_created property of this ManagedInstanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ManagedInstanceSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'server_count': 'int',
            'plugin_status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'server_count': 'serverCount',
            'plugin_status': 'pluginStatus',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._host_name = None
        self._server_count = None
        self._plugin_status = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstanceSummary.
        The `OCID`__ of the managed instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstanceSummary.
        The `OCID`__ of the managed instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ManagedInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstanceSummary.
        A user-friendly name that does not have to be unique and is changeable.


        :return: The display_name of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstanceSummary.
        A user-friendly name that does not have to be unique and is changeable.


        :param display_name: The display_name of this ManagedInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstanceSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstanceSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ManagedInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this ManagedInstanceSummary.
        The FQDN of the managed instance.


        :return: The host_name of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this ManagedInstanceSummary.
        The FQDN of the managed instance.


        :param host_name: The host_name of this ManagedInstanceSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def server_count(self):
        """
        **[Required]** Gets the server_count of this ManagedInstanceSummary.
        The number of servers running in the managed instance.


        :return: The server_count of this ManagedInstanceSummary.
        :rtype: int
        """
        return self._server_count

    @server_count.setter
    def server_count(self, server_count):
        """
        Sets the server_count of this ManagedInstanceSummary.
        The number of servers running in the managed instance.


        :param server_count: The server_count of this ManagedInstanceSummary.
        :type: int
        """
        self._server_count = server_count

    @property
    def plugin_status(self):
        """
        **[Required]** Gets the plugin_status of this ManagedInstanceSummary.
        The plugin status of the managed instance.


        :return: The plugin_status of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, plugin_status):
        """
        Sets the plugin_status of this ManagedInstanceSummary.
        The plugin status of the managed instance.


        :param plugin_status: The plugin_status of this ManagedInstanceSummary.
        :type: str
        """
        self._plugin_status = plugin_status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagedInstanceSummary.
        The date and time the managed instance was first reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ManagedInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedInstanceSummary.
        The date and time the managed instance was first reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ManagedInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ManagedInstanceSummary.
        The date and time the managed instance was last reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this ManagedInstanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ManagedInstanceSummary.
        The date and time the managed instance was last reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this ManagedInstanceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
