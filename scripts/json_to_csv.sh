# clean up and save the saved json files to tsv files for annotation

# This script is used to convert the CSV files to JSON files. The CSV files are the output of the get_articles.sh script. The JSON files are used to store the data in a more structured format. The JSON files are then used to create the TSV files for annotation. The TSV files are used to store the data in a format that can be easily read by the annotation tool.

tags=(
    "red_one"
    "heretic"
    "the_best_christmas_pageant_ever"
    "here"
    "hitpig"
    "absolution"
    "elevation"
    "a_real_pain"
    "lost_on_a_mountain_in_maine"
    "the_carpenter"
    "luther_never_too_much"
    "wicked"
    "gladiator_ii"
    "venom_the_last_dance"
    "conclave"
    "your_monster"
    "lets_start_a_cult"
    "from_embers"
)

for i in ${!tags[@]};
do
    python ./src/json_to_csv.py "./data/${tags[i]}.json"
done

