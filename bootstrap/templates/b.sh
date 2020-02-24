while IFS=, read -r field1 field2 
do
    cp 1789612160.html $field1.html
done < a.csv
