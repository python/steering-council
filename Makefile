# Updates the list of "Updates" in the README
update:
	cog -v > /dev/null || python3 -m pip install cogapp
	cog -Pr README.md

# Check if update needed to the list of "Updates" in the README
check:
	cog -v > /dev/null || python3 -m pip install cogapp
	cog -P --check README.md
