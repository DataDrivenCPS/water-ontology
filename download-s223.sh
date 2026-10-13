#!/bin/bash
# Refresh the vendored copy of ASHRAE 223P from open223.info.
#
# s223/223p.ttl is what OntoEnv resolves for the build and the tests;
# libraries/223p.ttl is the same file, loaded alongside the BuildingMOTIF
# templates. Keep the two identical.
set -euo pipefail

URL="https://open223.info/223p.ttl"

# remove the old s223/ folder
rm -rf s223
mkdir s223
curl -sSfL -o s223/223p.ttl "$URL"
cp s223/223p.ttl libraries/223p.ttl

grep -o 'owl:versionInfo "[^"]*"' s223/223p.ttl | head -1
echo "Re-index with: uv run ontoenv update"
