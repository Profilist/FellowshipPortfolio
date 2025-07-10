#!/bin/bash

echo "Making POST request..."
POST_RESPONSE=$(curl -s -X POST http://localhost:5000/api/timeline_post \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john.doe@example.com", "content": "This is a test post"}')

echo "Making GET request..."
GET_RESPONSE=$(curl -s http://localhost:5000/api/timeline_post)

echo "Checking if posted data is in GET response..."
if echo "$GET_RESPONSE" | grep -q "John Doe" && echo "$GET_RESPONSE" | grep -q "john.doe@example.com" && echo "$GET_RESPONSE" | grep -q "This is a test post"; then
    echo "✅ Posted data found in GET response"
else
    echo "❌ Posted data not found in GET response"
fi