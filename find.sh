find . -type f

find . -type d

find . -type -name "hello"

find . -type f -name "hello"

find . -type f -name "hello*"

find . -type f -iname "Hello*"

find . -type f -iname "*.js"

find . -type f -mmin -10

find . -type f -mmin +10

find . -type f -mmin +1 -mmin -5

find . -size +5M

find . -size +5G

find . -size +5k

find . -perm 777

find . -empty

