# Tools-lib-python
Toolkit for have some informations about OS in python

&nbsp;
# Requirements

* Linux server
* At leat 2Go RAM and 1 CPU
* python3 and python3-pip installed

&nbsp;
# Install application

* Clone the repository

```console
bngameni@delbechirclara:$ git clone https://github.com/my-esgi-projects/tp-tools-lib-python.git
Cloning into 'tp-tools-lib-python'...
remote: Enumerating objects: 130, done.
remote: Counting objects: 100% (130/130), done.
remote: Compressing objects: 100% (83/83), done.
remote: Total 130 (delta 50), reused 110 (delta 39), pack-reused 0
Receiving objects: 100% (130/130), 141.92 KiB | 2.25 MiB/s, done.
Resolving deltas: 100% (50/50), done
```

* Install requirements

```console
bngameni@delbechirclara:$ cd tp-tools-lib-python/
bngameni@delbechirclara:$ python3 -m pip install -r requirements.txt
```

* Enter in workspace directory
```console
bngameni@delbechirclara:$ cd workspace
```
&nbsp;

## Client-Server application using socket

> * For test this, [Install application both client side and server side](#install-application)
> * Here you have two scripts to launch. First server script and client script after.

&nbsp;

### Server script

* Display help

```console
bngameni@delbechirclara:$ python server.py -h
usage: server.py [-h] [-H HOST] [-P PORT]

Launch without options will use localhost as default host and 8090 as defaut port

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  server listen address
  -P PORT, --port PORT  server listen port
```

* Launch server script

```console
bngameni@delbechirclara:$ python3 server.py --host 0.0.0.0 --port 8989

```

> * Server is muted when it's launched

&nbsp;

### Client Script

* Display help
```console
bngameni@delbechirclara:$ python client.py -h
usage: client.py [-h] [-H HOST] [-P PORT]

Launch without options will use localhost as default host and 8090 as defaut port

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  server listen address
  -P PORT, --port PORT  server listen port
```

* Show network interface of client server
```console
bngameni@ansible-dev:$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:18:52:78 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 84917sec preferred_lft 84917sec
    inet6 fe80::a00:27ff:fe18:5278/64 scope link 
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:6b:f0:dc brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.45/24 brd 192.168.1.255 scope global dynamic enp0s8
       valid_lft 84917sec preferred_lft 84917sec
    inet6 2001:861:5e49:aa00:a00:27ff:fe6b:f0dc/64 scope global dynamic mngtmpaddr noprefixroute 
       valid_lft 86400sec preferred_lft 14400sec
    inet6 fe80::a00:27ff:fe6b:f0dc/64 scope link 
       valid_lft forever preferred_lft forever
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:0d:2c:24:e7 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever

```

* Launch client script
```console
bngameni@delbechirclara:$ python3 client.py --host 192.168.1.94 --port 8989
1. Display OS Informations
2. Display CPU Informations
3. Display Informations About Sensors
4. Display Informations About Memory
0. Quit application
Enter your choice: 1
         1. Show os name
         2. Show os architecture
         3. Show os release
         4. Show os hostname
         0. Back to main menu
Enter your choice: 1
 The os name is : Linux
         1. Show os name
         2. Show os architecture
         3. Show os release
         4. Show os hostname
         0. Back to main menu
Enter your choice: 2
 The architecture of os is : x86_64
         1. Show os name
         2. Show os architecture
         3. Show os release
         4. Show os hostname
         0. Back to main menu
Enter your choice: 3
 The release of os is : 5.19.0-41-generic
         1. Show os name
         2. Show os architecture
         3. Show os release
         4. Show os hostname
         0. Back to main menu
Enter your choice: 4
 The hostname is : delbechirclara
         1. Show os name
         2. Show os architecture
         3. Show os release
         4. Show os hostname
         0. Back to main menu
Enter your choice: 0
1. Display OS Informations
2. Display CPU Informations
3. Display Informations About Sensors
4. Display Informations About Memory
0. Quit application
Enter your choice: 0
         Are you sure to quit ?(yes/no)

Enter your choice: yes
bngameni@delbechirclara:$ 
```
&nbsp;

> * Only first menu is showed on this readme.

&nbsp;


## Filter automation using iptables on linux server from client script in python

* Display help
```console
bngameni@delbechirclara:$ python iptables_ssh.py -h
usage: iptables_ssh [options]

Execute commands througth ssh

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Server for ssh connexion
  -U USERNAME, --username USERNAME
                        Username for login to the server
  -P PASSWORD, --password PASSWORD
                        Password for login to the server
  -F FILE, --file FILE  Path to file which contains commands
  -L LOG, --log LOG     Path to file for logging all informations
```

&nbsp;
* Launch iptables to remote server

   * Content of iptables rules files
   
   ```console
   bngameni@delbechirclara:$ cat files/rules.txt
   # Autoriser les connexions entrantes sur le port 80
   iptables -A OUTPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
   
   # Autoriser les connexions entrantes sur le port 443
   iptables -A INPUT -p tcp --dport 443  -j ACCEPT

   # Autoriser les connexions sortantes sur le port 443
   iptables -A OUTPUT -p tcp --sport 443  -j ACCEPT

   # Autoriser les connexions entrantes sur le port 22
   iptables -A INPUT -p tcp --dport 22 -j ACCEPT

   # Autoriser les connexions sortantes sur le port 22
   iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT
   
   # Bloquer le traffic ICMP entrant et sortant
   iptables -A OUTPUT -p icmp  -j DROP
   iptables -A INPUT -p icmp  -j DROP

   # Accepter les connexions entrantes et sortantes sur le port 123 udp
   iptables -A INPUT -p udp --dport 123  -j ACCEPT
   iptables -A OUTPUT -p udp --dport 123 -j ACCEPT% 
   ```

   * Run script
   ```console
   bngameni@delbechirclara:$ python iptables_ssh.py --host 192.168.1.45 --username=xxxxxx --password=xxxxxxx --file=files/rules.txt --log=./ssh_log.txt
   Sending command: iptables -A OUTPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
   Output: []
   Sending command: iptables -A INPUT -p tcp --dport 443  -j ACCEPT
   Output: []
   Sending command: iptables -A OUTPUT -p tcp --sport 443  -j ACCEPT
   Output: []
   Sending command: iptables -A INPUT -p tcp --dport 22 -j ACCEPT
   Output: []
   Sending command: iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT
   Output: []
   Sending command: iptables -A OUTPUT -p icmp  -j DROP
   Output: []
   Sending command: iptables -A INPUT -p icmp  -j DROP
   Output: []
   Sending command: iptables -A INPUT -p udp --dport 123  -j ACCEPT
   Output: []
   Sending command: iptables -A OUTPUT -p udp --dport 123 -j ACCEPT
   Output: []
   ```

   * Show log files
   ```console
   bngameni@delbechirclara:$ tail -n10 ./ssh_log.txt
   INFO 2023-05-14 10:04:06,529 Authentication (password) successful!
   DEBUG 2023-05-14 10:04:06,529 [chan 0] Max packet in: 32768 bytes
   DEBUG 2023-05-14 10:04:07,033 Received global request "hostkeys-00@openssh.com"
   DEBUG 2023-05-14 10:04:07,033 Rejecting "hostkeys-00@openssh.com" global request from server.
   DEBUG 2023-05-14 10:04:07,076 [chan 0] Max packet out: 32768 bytes
   DEBUG 2023-05-14 10:04:07,076 Secsh channel 0 opened.
   DEBUG 2023-05-14 10:04:07,077 [chan 0] Sesch channel 0 request ok
   DEBUG 2023-05-14 10:04:07,103 [chan 0] EOF received (0)
   DEBUG 2023-05-14 10:04:07,103 [chan 0] EOF sent (0)
   INFO 2023-05-14 10:04:08,081 command: iptables -A OUTPUT -p udp --dport 123 -j ACCEPT -> stdout: []
   ```

   * Show iptables of remote server
   ```console
   ubuntu@ansible-dev:~$ sudo iptables-save 
   # Generated by iptables-save v1.8.4 on Sun May 14 08:24:02 2023
   *filter
   :INPUT ACCEPT [0:0]
   :FORWARD DROP [0:0]
   :OUTPUT ACCEPT [25:1832]
   :DOCKER - [0:0]
   :DOCKER-ISOLATION-STAGE-1 - [0:0]
   :DOCKER-ISOLATION-STAGE-2 - [0:0]
   :DOCKER-USER - [0:0]
   -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
   -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
   -A INPUT -p icmp -j DROP
   -A INPUT -p udp -m udp --dport 123 -j ACCEPT
   -A FORWARD -j DOCKER-USER
   -A FORWARD -j DOCKER-ISOLATION-STAGE-1
   -A FORWARD -o docker0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
   -A FORWARD -o docker0 -j DOCKER
   -A FORWARD -i docker0 ! -o docker0 -j ACCEPT
   -A FORWARD -i docker0 -o docker0 -j ACCEPT
   -A OUTPUT -p tcp -m tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
   -A OUTPUT -p tcp -m tcp --sport 443 -j ACCEPT
   -A OUTPUT -p tcp -m tcp --dport 22 -j ACCEPT
   -A OUTPUT -p icmp -j DROP
   -A OUTPUT -p udp -m udp --dport 123 -j ACCEPT
   -A DOCKER-ISOLATION-STAGE-1 -i docker0 ! -o docker0 -j DOCKER-ISOLATION-STAGE-2
   -A DOCKER-ISOLATION-STAGE-1 -j RETURN
   -A DOCKER-ISOLATION-STAGE-2 -o docker0 -j DROP
   -A DOCKER-ISOLATION-STAGE-2 -j RETURN
   -A DOCKER-USER -j RETURN
   COMMIT
   # Completed on Sun May 14 08:24:02 2023
   # Generated by iptables-save v1.8.4 on Sun May 14 08:24:02 2023
   *nat
   :PREROUTING ACCEPT [17:1058]
   :INPUT ACCEPT [17:1058]
   :OUTPUT ACCEPT [0:0]
   :POSTROUTING ACCEPT [0:0]
   :DOCKER - [0:0]
   -A PREROUTING -m addrtype --dst-type LOCAL -j DOCKER
   -A OUTPUT ! -d 127.0.0.0/8 -m addrtype --dst-type LOCAL -j DOCKER
   -A POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE
   -A DOCKER -i docker0 -j RETURN
   COMMIT
   # Completed on Sun May 14 08:24:02 2023
   ```

   * Try ping to remote server and see effects of ping drop rules
   ```console
   bngameni@delbechirclara:$ ping -c4 192.168.1.45
   PING 192.168.1.45 (192.168.1.45) 56(84) bytes of data.
   ^C
   --- 192.168.1.45 ping statistics ---
   4 packets transmitted, 0 received, 100% packet loss, time 3068ms
   ```

&nbsp;
## Mini wireshark

* Launch application
```console
bngameni@delbechirclara:$ sudo python3 wireshark.py
Mini WireShark - Select protocol to filter:
1. http filtering
2. dns filtering
3. tcp filtering
4. udp filtering
5. icmp filtering
0. Quit
Entrez le numéro du protocole : 3
1. Scan avec scappy
2. Scan with pyshark
Entrez l'outils de filtrage: 1
IP / TCP 10.0.16.13:51372 > 34.107.221.82:http PA / Raw
IP / TCP 34.107.221.82:http > 10.0.16.13:51372 PA / Raw
IP / TCP 10.0.16.13:51372 > 34.107.221.82:http A
IP / TCP 10.0.16.13:51372 > 34.107.221.82:http PA / Raw
IP / TCP 34.107.221.82:http > 10.0.16.13:51372 PA / Raw
```
&nbsp;
> Ps: Others cases will be present later.

&nbsp;
## User-Groups creation script

* Display help

    ```bash
        python3 user.py -h
    ```
    ![server help](images/4-user_help.png)

* Launch script
    ```bash
        python3 user.py --file files/file.txt
    ```


