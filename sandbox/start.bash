#!/bin/bash

base_port=1234

for ((i=1; i<=12; i++)); do
  port=$((base_port + i))
  node main.js "$port" &
done

echo "Servers are running."
read -p "Press Enter to exit."
