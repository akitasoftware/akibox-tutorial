# !/bin/bash

# Copyright 2021 Akita Software, Inc.
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

PORT=8000
HOST="localhost:${PORT}"
USER_1="2b9046ac-6112-11eb-ae07-3e22fb0d93ba"
USER_2="38c15834-6112-11eb-86fb-3e22fb0d93ba"

echo "Get user info"
curl -s -S ${HOST}/users/${USER_1}
echo ""
curl -s -S ${HOST}/users/${USER_2}
echo -e "\n"

echo "Create file 1"
F1=$(curl -s -S -X POST -H 'Content-Type: application/json' \
  -d '{"contents": "Ode to Akita: A poem."}' \
  ${HOST}/users/${USER_1}/files)
FID1=$(echo ${F1} | jq -r .id)
echo -e "$F1\n"

echo "List files"
curl -s -S ${HOST}/users/${USER_1}/files
echo -e "\n"

echo "Get file 1"
curl -s -S ${HOST}/users/${USER_1}/files/${FID1}
echo -e "\n"

echo "Create file 2"
F2=$(curl -s -S -X POST -H 'Content-Type: application/json' \
  -d '{"contents": "Ode to Akita: A poem."}' \
  ${HOST}/users/${USER_1}/files)
FID2=$(echo ${F2} | jq -r .id)
echo -e "$F2\n"

echo "List files"
curl -s -S ${HOST}/users/${USER_1}/files
echo -e "\n"

# echo "Delete file 1"
# curl -s -S -X DELETE ${HOST}/users/${USER_1}/files/${FID1}
# echo -e ""
# 
# echo "Delete file 2"
# curl -s -S -X DELETE ${HOST}/users/${USER_1}/files/${FID2}
# echo -e ""

echo "Try to get missing file"
curl -s -S ${HOST}/users/${USER_1}/files/${FID1}
echo ""

