#!/bin/bash

# Bash 3.2: Text Cleaner
# This script cleans text by tokenizing and removing invalid tokens and stop words

# Function to convert input to lowercase
function lower_case() {
    echo "$1" | tr '[:upper:]' '[:lower:]'
}

# Function to check if a token is a stop word
function is_stop_word() {
    local token="$1"
    local stop_words=" of the a by is was for with were in on there this that at be been to or and if then else will would shall should could are am an I we you your me has he she him her them their there "
    # Add spaces around the token and check if it's in the stop words list
    [[ "$stop_words" == *" $token "* ]]
}

# Function to check if token contains invalid characters
# Invalid: non-alpha printable ASCII that is NOT a token separator
# Token separators: " ' , . ; space - ! ?
# Since tokens are split by separators, tokens themselves shouldn't contain separators
# So we check if token contains any non-alpha characters
function has_invalid_char() {
    local token="$1"
    # Check if token contains any character that is not a letter
    if [[ "$token" =~ [^a-zA-Z] ]]; then
        return 0  # Has invalid character
    fi
    return 1  # No invalid characters (only letters)
}

# Function to clean text
function clean_text() {
    local input="$1"
    
    # Step 1: Convert to lowercase
    local lower_input=$(lower_case "$input")
    
    # Step 2: Tokenize using separator characters
    # Token separators: " ' , . ; space - ! ?
    # Replace all separators with spaces, then split by spaces
    # Put hyphen at end of character class to avoid escaping issues
    local tokens=$(echo "$lower_input" | sed "s/[\"',.;!?-]/ /g" | tr -s ' ' '\n' | grep -v '^$')
    
    # Step 3: Process each token
    local result=""
    while IFS= read -r token; do
        # Skip empty tokens
        [[ -z "$token" ]] && continue
        
        # Remove token if it contains invalid characters
        if has_invalid_char "$token"; then
            continue
        fi
        
        # Remove token if it's a stop word
        if is_stop_word "$token"; then
            continue
        fi
        
        # Add valid token to result
        if [[ -z "$result" ]]; then
            result="$token"
        else
            result="$result $token"
        fi
    done <<< "$tokens"
    
    echo "$result"
}

# Main: Read input and process
read -r input_line
clean_text "$input_line"

