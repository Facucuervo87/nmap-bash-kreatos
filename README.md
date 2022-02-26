# nmap-bash-kreatos
Just put the targets on a .csv file and it will make the nmap's commands for you.

Full the scope.csv file with your own scope.

Thenn run the .py file as follow:

`python3 nmap-bash.py -i inputfile.csv -a <name_of_the_assesment>`


This command return two files .sh one for UDP scan and other for TCP scan.

The default TCP nmap command is: 

`nmap -sSCV -Pn --top-ports=2000 -vvv <tartget> -oA target_TCP`


The default TCP nmap command is: 

`nmap -sUCV -Pn --top-ports=20 -vvv <tartget> -oA target_UDP`
