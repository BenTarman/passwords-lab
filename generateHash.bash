


for (( i = 0; i < 8; i++ )); do
	#statements

	if [[ i -eq 0 ]]; then
		file=twitter-banned.txt
	else
		file=twitter-banned$i.txt
	fi

	while read p; do
		mkpasswd -5 -s <<< $p >> hash-$file
	done < $file
done
