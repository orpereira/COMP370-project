# clean up and save the saved json files to tsv files for annotation

# This script is used to convert the CSV files to JSON files. The CSV files are the output of the get_articles.sh script. The JSON files are used to store the data in a more structured format. The JSON files are then used to create the TSV files for annotation. The TSV files are used to store the data in a format that can be easily read by the annotation tool.

tags=("heretic" "pageant" "elevation" "overlord" "miller" "bird")

for i in {0..5}
do
    python ./src/json_to_csv.py "./data/${tags[i]}.json"
done

