Simulate:
	echo "#!/bin/bash" > Simulate
	echo "python3 test_script.py \"\$$@\"" >> Simulate
	chmod u+x Simulate