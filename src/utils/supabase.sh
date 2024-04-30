#!/bin/bash

source .env

insert_row() {
    echo "Inserting a new row into the 'articles' table..."
    curl -X POST "${SUPABASE_URL}/rest/v1/articles" \
    -H "apikey: ${SUPABASE_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_KEY}" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=minimal" \
    -d "$1"
}

update_row() {
    echo "Updating an existing row in the 'articles' table..."
    curl -X PATCH "${SUPABASE_URL}/rest/v1/articles?title=eq.$2" \
    -H "apikey: ${SUPABASE_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_KEY}" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=minimal" \
    -d "$1"
}

delete_row() {
    echo "Deleting a row from the 'articles' table..."
    curl -X DELETE "${SUPABASE_URL}/rest/v1/articles?title=eq.$1" \
    -H "apikey: ${SUPABASE_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_KEY}"
}
