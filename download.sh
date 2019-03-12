#!/usr/bin/expect -f

set timeout 10
spawn /bin/bash wget-script.sh -H https://esgf-node.llnl.gov/esgf-idp/openid/takaito2 takaito2
expect "Enter password : "
send -- "\r"

wait
