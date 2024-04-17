#!/bin/bash
if [ $# -eq 0 ]; then
    MAX_PAGES=3
else
    if [[ "$1" =~ ^[0-9]+$ ]]; then
        MAX_PAGES=$1
        echo "Argument passed: Setting MAX_PAGES to $MAX_PAGES."
    else
        echo "Invalid argument. Please provide a positive integer for number of MAX_PAGES."
    fi
fi

mkdir -p politifact_json
poetry run scrapy crawl politifact -O politifact_json/politifact.json -a MAX_PAGES=$MAX_PAGES