#!/bin/bash

titles=("Heretic" "The Best Christmas Pageant Ever" "Elevation" "The Sacred Kingdom" "Christmas Eve in Miller’s Point" "Bird")
director=("Beck" "Jenkins" "Nolfi" "movie" "Taormina" "Arnold")
your_api_key="7893c8073cb841aa9f69296b5df063e2"
tags=("heretic" "pageant" "elevation" "overlord" "miller" "bird")

start_date="2024-11-01"
end_date="2024-11-22"

for i in {0..5}
do
    python ./src/download_data.py "$your_api_key" "${titles[i]}" "$start_date" "$end_date" "./data/${tags[i]}.json"
done