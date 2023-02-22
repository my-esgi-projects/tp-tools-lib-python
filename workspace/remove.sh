for user in toto titi chat grosloup
do
	sudo deluser ${user}
done

for group in groupe1 groupe2
do
	sudo groupdel ${group}
done
