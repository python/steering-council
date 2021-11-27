# Updates the list of of "Updates" in the README
update:
	cog -v > /dev/null || python3 -m pip cog
	cog -Pr README.md
