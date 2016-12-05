# coding: utf-8

"""
    Selectel DNS API

    Simple Selectel DNS API.

    OpenAPI spec version: 1.0.0
    Contact: info@mdsina.ru
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

from __future__ import absolute_import

# import models into model package
from .api_response import ApiResponse
from .batch_update_model import BatchUpdateModel
from .domain import Domain
from .geo_record import GeoRecord
from .new_domain import NewDomain
from .new_or_updated_ptr_record import NewOrUpdatedPTRRecord
from .new_or_updated_record import NewOrUpdatedRecord
from .new_or_updated_tag import NewOrUpdatedTag
from .ptr_record import PTRRecord
from .record import Record
from .tag import Tag
from .updated_domain import UpdatedDomain