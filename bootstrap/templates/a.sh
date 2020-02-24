while IFS=, read -r field1 field2 
do
    sed "s/1788478126/$field1/g" a.txt >> c1.txt
done < a.csv
