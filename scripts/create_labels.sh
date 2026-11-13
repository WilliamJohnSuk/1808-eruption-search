#!/bin/bash
# Create or update the repository's labels from community/labels.json.
# Needs the GitHub CLI (gh, logged in) and python3. Run from the repo root:
#   bash scripts/create_labels.sh WilliamJohnSuk/1808-eruption-search
# Licence: MIT.
set -e
REPO=${1:?usage: create_labels.sh owner/repo}
python3 -c 'import json,sys; [print("\t".join([l["name"],l["color"],l["description"]])) for l in json.load(open("community/labels.json"))]' |
while IFS=$'\t' read -r name color desc; do
  gh label create "$name" --repo "$REPO" --color "$color" --description "$desc" --force
done
