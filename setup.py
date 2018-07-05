#########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.


from setuptools import setup

setup(
    name='cloudify-script-plugin',
    version='1.5.4',
    author='Cloudify',
    author_email='hello@cloudify.co',
    packages=['script_runner'],
    description='Plugin for running scripts',
    install_requires=[
        'cloudify-plugins-common>=4.0'
    ],
    license='LICENSE'
)
