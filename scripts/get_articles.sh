#!/bin/bash

titles=(
    "Red One"
    "Heretic"
    "The Best Christmas Pageant Ever"
    "Here"
    "Hitpig"
    "Absolution"
    "Elevation"
    "A Real Pain"
    "Lost on a Mountain in Maine"
    "The Carpenter"
    "Luther: Never Too Much"
    "Wicked"
    "Gladiator II"
    "Venom: The Last Dance"
    "Conclave"
    "Your Monster"
    "Let's Start A Cult"
    "From Embers"
)

studios=(
    "Warner Bros."
    "A24"
    "Lionsgate"
    "Sony Pictures Releasing"
    "Viva Pictures"
    "The Samuel Goldwyn Company"
    "Vertical Entertainment"
    "Searchlight Pictures"
    "Blue Fox Entertainment"
    "Purdie Distribution"
    "Drafthouse Films"
    "Universal Pictures"
    "Paramount Pictures"
    "Sony Pictures Releasing"
    "Focus Features"
    "Vertical Entertainment"
    "Queensbury Pictures"
    "Studio 6688"
    
)

directors=(
    "Kasdan"
    "Beck"
    "Jenkins"
    "Zemeckis"
    "Angelini"
    "Molland"
    "Nolfi"
    "Eisenberg"
    "Kightlinger"
    "Batty"
    "Porter"
    "Chu"
    "Scott"
    "Marcel"
    "Berger"
    "Lindy"
    "Kitnick"
    "Bohan"
)

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

your_api_key="70cde46dc61d4e24ab0b9a799654785c"

start_date="2024-10-25"
end_date="2024-11-24"

for i in ${!tags[@]};
do
    python ./src/download_data.py "$your_api_key" "${titles[i]}" "${studios[i]}" "${directors[i]}" "$start_date" "$end_date" "./data/${tags[i]}.json"
done

