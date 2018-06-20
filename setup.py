#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("./netblocks/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netblocks",
    author='hm-distro',
    version="0.0.4",
    description="Get the Google netblocks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hm-distro/netblocks/",
    packages=['netblocks'],
    platforms=['any'],
    install_requires=[
          'requests',
      ],
    include_package_data=True,
    license="Apache 2",
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
