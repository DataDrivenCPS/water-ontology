#!/bin/bash
# Refresh the vendored copy of ASHRAE 223P from open223.info.
#
# libraries/223p.ttl is the single vendored copy: OntoEnv resolves it for the
# build and the tests, and BuildingMOTIF loads it alongside the templates.
set -euo pipefail

URL="https://open223.info/223p.ttl"

curl -sSfL -o libraries/223p.ttl "$URL"

grep -o 'owl:versionInfo "[^"]*"' libraries/223p.ttl | head -1
echo "Re-index with: uv run ontoenv update"
