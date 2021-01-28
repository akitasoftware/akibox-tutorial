# !/bin/bash

PORT=8000
HOST="localhost:${PORT}"
USER_1="2b9046ac-6112-11eb-ae07-3e22fb0d93ba"
USER_2="38c15834-6112-11eb-86fb-3e22fb0d93ba"

echo "Get user info"
curl -s ${HOST}/users/${USER_1}
echo ""
curl -s ${HOST}/users/${USER_2}
echo -e "\n"

echo "Create file 1"
F1=$(curl -s -X POST -H 'Content-Type: application/json' \
  -d '{"contents": "Ode to Akita: A poem."}' \
  ${HOST}/users/${USER_1}/files)
FID1=$(echo ${F1} | jq -r .id)
echo -e "$F1\n"

echo "List files"
curl -s ${HOST}/users/${USER_1}/files
echo -e "\n"

echo "Get file 1"
curl -s ${HOST}/users/${USER_1}/files/${FID1}
echo -e "\n"

echo "Create file 2"
F2=$(curl -s -X POST -H 'Content-Type: application/json' \
  -d '{"contents": "Ode to Akita: A poem."}' \
  ${HOST}/users/${USER_1}/files)
FID2=$(echo ${F2} | jq -r .id)
echo -e "$F2\n"

echo "List files"
curl -s ${HOST}/users/${USER_1}/files
echo -e "\n"

# echo "Delete file 1"
# curl -s -X DELETE ${HOST}/users/${USER_1}/files/${FID1}
# echo -e ""
# 
# echo "Delete file 2"
# curl -s -X DELETE ${HOST}/users/${USER_1}/files/${FID2}
# echo -e ""

echo "Try to get missing file"
curl -s ${HOST}/users/${USER_1}/files/${FID1}
echo ""

