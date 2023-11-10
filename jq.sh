echo '{"fruit":{"name":"apple","color":"green","price":1.20}}' | jq '.'

jq '.' fruit.json

curl http://api.open-notify.org/iss-now.json | jq '.'

jq '.fruit' fruit.json

jq '.fruit.color' fruit.json

jq '.fruit.color,.fruit.price' fruit.json

echo '{ "with space": "hello" }' | jq '."with space"'

echo '["x","y","z"]' | jq '.[]'

jq '.[] | .name' fruits.json

jq '.[1].price' fruits.json


echo '[1,2,3,4,5,6,7,8,9,10]' | jq '.[:6]' | jq '.[-2:]'

echo '[1,2,3,4,5,6,7,8,9,10]' | jq '.[:6]' | jq '.[-2:]'

jq '.fruit | keys' fruit.json

jq '.fruit | length' fruit.json


jq 'map(has("name"))' fruits.json


jq 'map(.price+2)' fruits.json

jq '[.[].price] | min' fruits.json



jq '[.[].price] | max' fruits.json

jq '.[] | select(.price>0.5)' fruits.json


jq '.[] | select(.color=="yellow")' fruits.json


jq '.[] | select(.color=="yellow" and .price>=0.5)' fruits.json


jq '.[] | select(.name|test("^a.")) | .price' fruits.json


jq 'map(.color) | unique' fruits.json


jq 'del(.fruit.name)' fruit.json


jq '.query.pages | [.[] | map(.) | .[] | {page_title: .title, page_description: .extract}]' wikipedia.json








