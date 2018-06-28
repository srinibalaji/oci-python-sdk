# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeSourceDetails(object):
    """
    BootVolumeSourceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.BootVolumeSourceFromBootVolumeBackupDetails`
        * :class:`~oci.core.models.BootVolumeSourceFromBootVolumeDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BootVolumeSourceDetails.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'bootVolumeBackup':
            return 'BootVolumeSourceFromBootVolumeBackupDetails'

        if type == 'bootVolume':
            return 'BootVolumeSourceFromBootVolumeDetails'
        else:
            return 'BootVolumeSourceDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BootVolumeSourceDetails.

        :return: The type of this BootVolumeSourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BootVolumeSourceDetails.

        :param type: The type of this BootVolumeSourceDetails.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
