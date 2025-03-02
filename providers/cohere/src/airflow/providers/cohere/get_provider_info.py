# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-cohere",
        "name": "Cohere",
        "description": "`Cohere <https://docs.cohere.com/docs>`__\n",
        "state": "ready",
        "source-date-epoch": 1740734107,
        "versions": [
            "1.4.2",
            "1.4.0",
            "1.3.0",
            "1.2.1",
            "1.2.0",
            "1.1.3",
            "1.1.2",
            "1.1.1",
            "1.1.0",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Cohere",
                "external-doc-url": "https://docs.cohere.com/docs",
                "how-to-guide": ["/docs/apache-airflow-providers-cohere/operators/embedding.rst"],
                "tags": ["software"],
            }
        ],
        "hooks": [
            {"integration-name": "Cohere", "python-modules": ["airflow.providers.cohere.hooks.cohere"]}
        ],
        "operators": [
            {"integration-name": "Cohere", "python-modules": ["airflow.providers.cohere.operators.embedding"]}
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.cohere.hooks.cohere.CohereHook",
                "connection-type": "cohere",
            }
        ],
        "dependencies": ["apache-airflow>=2.9.0", "cohere>=5.13.4"],
    }
