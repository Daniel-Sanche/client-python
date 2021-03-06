# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Source(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, storage_source=None, repo_source=None, artifact_storage_source=None, source_context=None, additional_source_contexts=None, file_hashes=None):
        """
        Source - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'storage_source': 'StorageSource',
            'repo_source': 'RepoSource',
            'artifact_storage_source': 'StorageSource',
            'source_context': 'ExtendedSourceContext',
            'additional_source_contexts': 'list[ExtendedSourceContext]',
            'file_hashes': 'dict(str, FileHashes)'
        }

        self.attribute_map = {
            'storage_source': 'storageSource',
            'repo_source': 'repoSource',
            'artifact_storage_source': 'artifactStorageSource',
            'source_context': 'sourceContext',
            'additional_source_contexts': 'additionalSourceContexts',
            'file_hashes': 'fileHashes'
        }

        self._storage_source = storage_source
        self._repo_source = repo_source
        self._artifact_storage_source = artifact_storage_source
        self._source_context = source_context
        self._additional_source_contexts = additional_source_contexts
        self._file_hashes = file_hashes

    @property
    def storage_source(self):
        """
        Gets the storage_source of this Source.
        If provided, get the source from this location in in Google Cloud Storage.

        :return: The storage_source of this Source.
        :rtype: StorageSource
        """
        return self._storage_source

    @storage_source.setter
    def storage_source(self, storage_source):
        """
        Sets the storage_source of this Source.
        If provided, get the source from this location in in Google Cloud Storage.

        :param storage_source: The storage_source of this Source.
        :type: StorageSource
        """

        self._storage_source = storage_source

    @property
    def repo_source(self):
        """
        Gets the repo_source of this Source.
        If provided, get source from this location in a Cloud Repo.

        :return: The repo_source of this Source.
        :rtype: RepoSource
        """
        return self._repo_source

    @repo_source.setter
    def repo_source(self, repo_source):
        """
        Sets the repo_source of this Source.
        If provided, get source from this location in a Cloud Repo.

        :param repo_source: The repo_source of this Source.
        :type: RepoSource
        """

        self._repo_source = repo_source

    @property
    def artifact_storage_source(self):
        """
        Gets the artifact_storage_source of this Source.
        If provided, the input binary artifacts for the build came from this location.

        :return: The artifact_storage_source of this Source.
        :rtype: StorageSource
        """
        return self._artifact_storage_source

    @artifact_storage_source.setter
    def artifact_storage_source(self, artifact_storage_source):
        """
        Sets the artifact_storage_source of this Source.
        If provided, the input binary artifacts for the build came from this location.

        :param artifact_storage_source: The artifact_storage_source of this Source.
        :type: StorageSource
        """

        self._artifact_storage_source = artifact_storage_source

    @property
    def source_context(self):
        """
        Gets the source_context of this Source.
        If provided, the source code used for the build came from this location.

        :return: The source_context of this Source.
        :rtype: ExtendedSourceContext
        """
        return self._source_context

    @source_context.setter
    def source_context(self, source_context):
        """
        Sets the source_context of this Source.
        If provided, the source code used for the build came from this location.

        :param source_context: The source_context of this Source.
        :type: ExtendedSourceContext
        """

        self._source_context = source_context

    @property
    def additional_source_contexts(self):
        """
        Gets the additional_source_contexts of this Source.
        If provided, some of the source code used for the build may be found in these locations, in the case where the source repository had multiple remotes or submodules. This list will not include the context specified in the source_context field.

        :return: The additional_source_contexts of this Source.
        :rtype: list[ExtendedSourceContext]
        """
        return self._additional_source_contexts

    @additional_source_contexts.setter
    def additional_source_contexts(self, additional_source_contexts):
        """
        Sets the additional_source_contexts of this Source.
        If provided, some of the source code used for the build may be found in these locations, in the case where the source repository had multiple remotes or submodules. This list will not include the context specified in the source_context field.

        :param additional_source_contexts: The additional_source_contexts of this Source.
        :type: list[ExtendedSourceContext]
        """

        self._additional_source_contexts = additional_source_contexts

    @property
    def file_hashes(self):
        """
        Gets the file_hashes of this Source.
        Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build.  The keys to this map are file paths used as build source and the values contain the hash values for those files.  If the build source came in a single package such as a gzipped tarfile (.tar.gz), the FileHash will be for the single path to that file.

        :return: The file_hashes of this Source.
        :rtype: dict(str, FileHashes)
        """
        return self._file_hashes

    @file_hashes.setter
    def file_hashes(self, file_hashes):
        """
        Sets the file_hashes of this Source.
        Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build.  The keys to this map are file paths used as build source and the values contain the hash values for those files.  If the build source came in a single package such as a gzipped tarfile (.tar.gz), the FileHash will be for the single path to that file.

        :param file_hashes: The file_hashes of this Source.
        :type: dict(str, FileHashes)
        """

        self._file_hashes = file_hashes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
