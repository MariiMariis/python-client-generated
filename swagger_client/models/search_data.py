# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SearchData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'search_type': 'str',
        'expression': 'str',
        'results': 'list[SearchResult]',
        'error_message': 'str'
    }

    attribute_map = {
        'search_type': 'searchType',
        'expression': 'expression',
        'results': 'results',
        'error_message': 'errorMessage'
    }

    def __init__(self, search_type=None, expression=None, results=None, error_message=None):  # noqa: E501
        """SearchData - a model defined in Swagger"""  # noqa: E501
        self._search_type = None
        self._expression = None
        self._results = None
        self._error_message = None
        self.discriminator = None
        self.search_type = search_type
        self.expression = expression
        if results is not None:
            self.results = results
        if error_message is not None:
            self.error_message = error_message

    @property
    def search_type(self):
        """Gets the search_type of this SearchData.  # noqa: E501


        :return: The search_type of this SearchData.  # noqa: E501
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this SearchData.


        :param search_type: The search_type of this SearchData.  # noqa: E501
        :type: str
        """
        if search_type is None:
            raise ValueError("Invalid value for `search_type`, must not be `None`")  # noqa: E501

        self._search_type = search_type

    @property
    def expression(self):
        """Gets the expression of this SearchData.  # noqa: E501


        :return: The expression of this SearchData.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this SearchData.


        :param expression: The expression of this SearchData.  # noqa: E501
        :type: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def results(self):
        """Gets the results of this SearchData.  # noqa: E501


        :return: The results of this SearchData.  # noqa: E501
        :rtype: list[SearchResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this SearchData.


        :param results: The results of this SearchData.  # noqa: E501
        :type: list[SearchResult]
        """

        self._results = results

    @property
    def error_message(self):
        """Gets the error_message of this SearchData.  # noqa: E501


        :return: The error_message of this SearchData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this SearchData.


        :param error_message: The error_message of this SearchData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SearchData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
