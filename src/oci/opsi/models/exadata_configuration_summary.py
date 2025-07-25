# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataConfigurationSummary(object):
    """
    Summary of a exadata configuration for a resource.
    """

    #: A constant which can be used with the entity_source property of a ExadataConfigurationSummary.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_EXADATA"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_EXADATA = "EM_MANAGED_EXTERNAL_EXADATA"

    #: A constant which can be used with the entity_source property of a ExadataConfigurationSummary.
    #: This constant has a value of "PE_COMANAGED_EXADATA"
    ENTITY_SOURCE_PE_COMANAGED_EXADATA = "PE_COMANAGED_EXADATA"

    #: A constant which can be used with the entity_source property of a ExadataConfigurationSummary.
    #: This constant has a value of "MACS_MANAGED_CLOUD_EXADATA"
    ENTITY_SOURCE_MACS_MANAGED_CLOUD_EXADATA = "MACS_MANAGED_CLOUD_EXADATA"

    #: A constant which can be used with the exadata_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "DBMACHINE"
    EXADATA_TYPE_DBMACHINE = "DBMACHINE"

    #: A constant which can be used with the exadata_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "EXACS"
    EXADATA_TYPE_EXACS = "EXACS"

    #: A constant which can be used with the exadata_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "EXACC"
    EXADATA_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "FULL"
    EXADATA_RACK_TYPE_FULL = "FULL"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "HALF"
    EXADATA_RACK_TYPE_HALF = "HALF"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "QUARTER"
    EXADATA_RACK_TYPE_QUARTER = "QUARTER"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "EIGHTH"
    EXADATA_RACK_TYPE_EIGHTH = "EIGHTH"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "FLEX"
    EXADATA_RACK_TYPE_FLEX = "FLEX"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "BASE"
    EXADATA_RACK_TYPE_BASE = "BASE"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "ELASTIC"
    EXADATA_RACK_TYPE_ELASTIC = "ELASTIC"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "ELASTIC_BASE"
    EXADATA_RACK_TYPE_ELASTIC_BASE = "ELASTIC_BASE"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "ELASTIC_LARGE"
    EXADATA_RACK_TYPE_ELASTIC_LARGE = "ELASTIC_LARGE"

    #: A constant which can be used with the exadata_rack_type property of a ExadataConfigurationSummary.
    #: This constant has a value of "ELASTIC_EXTRA_LARGE"
    EXADATA_RACK_TYPE_ELASTIC_EXTRA_LARGE = "ELASTIC_EXTRA_LARGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataConfigurationSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.ExadataDatabaseMachineConfigurationSummary`
        * :class:`~oci.opsi.models.ExadataExacsConfigurationSummary`
        * :class:`~oci.opsi.models.ExadataExaccConfigurationSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this ExadataConfigurationSummary.
        :type exadata_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this ExadataConfigurationSummary.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA", "MACS_MANAGED_CLOUD_EXADATA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExadataConfigurationSummary.
        :type compartment_id: str

        :param exadata_name:
            The value to assign to the exadata_name property of this ExadataConfigurationSummary.
        :type exadata_name: str

        :param exadata_display_name:
            The value to assign to the exadata_display_name property of this ExadataConfigurationSummary.
        :type exadata_display_name: str

        :param exadata_type:
            The value to assign to the exadata_type property of this ExadataConfigurationSummary.
            Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_type: str

        :param exadata_rack_type:
            The value to assign to the exadata_rack_type property of this ExadataConfigurationSummary.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", "FLEX", "BASE", "ELASTIC", "ELASTIC_BASE", "ELASTIC_LARGE", "ELASTIC_EXTRA_LARGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_rack_type: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ExadataConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExadataConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param vmcluster_details:
            The value to assign to the vmcluster_details property of this ExadataConfigurationSummary.
        :type vmcluster_details: list[oci.opsi.models.VmClusterSummary]

        """
        self.swagger_types = {
            'exadata_insight_id': 'str',
            'entity_source': 'str',
            'compartment_id': 'str',
            'exadata_name': 'str',
            'exadata_display_name': 'str',
            'exadata_type': 'str',
            'exadata_rack_type': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'vmcluster_details': 'list[VmClusterSummary]'
        }
        self.attribute_map = {
            'exadata_insight_id': 'exadataInsightId',
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'exadata_name': 'exadataName',
            'exadata_display_name': 'exadataDisplayName',
            'exadata_type': 'exadataType',
            'exadata_rack_type': 'exadataRackType',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'vmcluster_details': 'vmclusterDetails'
        }
        self._exadata_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._exadata_name = None
        self._exadata_display_name = None
        self._exadata_type = None
        self._exadata_rack_type = None
        self._defined_tags = None
        self._freeform_tags = None
        self._vmcluster_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'EM_MANAGED_EXTERNAL_EXADATA':
            return 'ExadataDatabaseMachineConfigurationSummary'

        if type == 'PE_COMANAGED_EXADATA':
            return 'ExadataExacsConfigurationSummary'

        if type == 'MACS_MANAGED_CLOUD_EXADATA':
            return 'ExadataExaccConfigurationSummary'
        else:
            return 'ExadataConfigurationSummary'

    @property
    def exadata_insight_id(self):
        """
        **[Required]** Gets the exadata_insight_id of this ExadataConfigurationSummary.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this ExadataConfigurationSummary.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this ExadataConfigurationSummary.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this ExadataConfigurationSummary.
        Source of the exadata entity.

        Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA", "MACS_MANAGED_CLOUD_EXADATA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this ExadataConfigurationSummary.
        Source of the exadata entity.


        :param entity_source: The entity_source of this ExadataConfigurationSummary.
        :type: str
        """
        allowed_values = ["EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA", "MACS_MANAGED_CLOUD_EXADATA"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExadataConfigurationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExadataConfigurationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExadataConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def exadata_name(self):
        """
        **[Required]** Gets the exadata_name of this ExadataConfigurationSummary.
        The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.


        :return: The exadata_name of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._exadata_name

    @exadata_name.setter
    def exadata_name(self, exadata_name):
        """
        Sets the exadata_name of this ExadataConfigurationSummary.
        The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.


        :param exadata_name: The exadata_name of this ExadataConfigurationSummary.
        :type: str
        """
        self._exadata_name = exadata_name

    @property
    def exadata_display_name(self):
        """
        **[Required]** Gets the exadata_display_name of this ExadataConfigurationSummary.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :return: The exadata_display_name of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._exadata_display_name

    @exadata_display_name.setter
    def exadata_display_name(self, exadata_display_name):
        """
        Sets the exadata_display_name of this ExadataConfigurationSummary.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :param exadata_display_name: The exadata_display_name of this ExadataConfigurationSummary.
        :type: str
        """
        self._exadata_display_name = exadata_display_name

    @property
    def exadata_type(self):
        """
        **[Required]** Gets the exadata_type of this ExadataConfigurationSummary.
        Operations Insights internal representation of the the Exadata system type.

        Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_type of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._exadata_type

    @exadata_type.setter
    def exadata_type(self, exadata_type):
        """
        Sets the exadata_type of this ExadataConfigurationSummary.
        Operations Insights internal representation of the the Exadata system type.


        :param exadata_type: The exadata_type of this ExadataConfigurationSummary.
        :type: str
        """
        allowed_values = ["DBMACHINE", "EXACS", "EXACC"]
        if not value_allowed_none_or_none_sentinel(exadata_type, allowed_values):
            exadata_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_type = exadata_type

    @property
    def exadata_rack_type(self):
        """
        **[Required]** Gets the exadata_rack_type of this ExadataConfigurationSummary.
        Exadata rack type.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", "FLEX", "BASE", "ELASTIC", "ELASTIC_BASE", "ELASTIC_LARGE", "ELASTIC_EXTRA_LARGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_rack_type of this ExadataConfigurationSummary.
        :rtype: str
        """
        return self._exadata_rack_type

    @exadata_rack_type.setter
    def exadata_rack_type(self, exadata_rack_type):
        """
        Sets the exadata_rack_type of this ExadataConfigurationSummary.
        Exadata rack type.


        :param exadata_rack_type: The exadata_rack_type of this ExadataConfigurationSummary.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH", "FLEX", "BASE", "ELASTIC", "ELASTIC_BASE", "ELASTIC_LARGE", "ELASTIC_EXTRA_LARGE"]
        if not value_allowed_none_or_none_sentinel(exadata_rack_type, allowed_values):
            exadata_rack_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_rack_type = exadata_rack_type

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ExadataConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ExadataConfigurationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExadataConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ExadataConfigurationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ExadataConfigurationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ExadataConfigurationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExadataConfigurationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ExadataConfigurationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def vmcluster_details(self):
        """
        Gets the vmcluster_details of this ExadataConfigurationSummary.
        Array of objects containing VM cluster information.


        :return: The vmcluster_details of this ExadataConfigurationSummary.
        :rtype: list[oci.opsi.models.VmClusterSummary]
        """
        return self._vmcluster_details

    @vmcluster_details.setter
    def vmcluster_details(self, vmcluster_details):
        """
        Sets the vmcluster_details of this ExadataConfigurationSummary.
        Array of objects containing VM cluster information.


        :param vmcluster_details: The vmcluster_details of this ExadataConfigurationSummary.
        :type: list[oci.opsi.models.VmClusterSummary]
        """
        self._vmcluster_details = vmcluster_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
