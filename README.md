## MITM_DNS
- ARP Spoofing, DNS Spoofing, Pharming site(WAS), MySQL(DB) 기술을 활용한 MITM 실습 이다.

## 사전 지식
- <a href = ""> ARP</a>
- <a href = ""> ARP Spoofing</a>
- <a href = ""> DNS Spoofing</a>


## 개발 환경
- malicious : KALI Linux
- victim : window 7
- Pharming site : django
- creadential : Python(selenium), chrom driver
- WAS : aws-ubuntu(apache)
- Network : NAT(iptime_wifi)

## iptables, ip_forwarding settings
- echo 1 > /proc/sys/net/ipv4/ip_forward
- iptables -I FORWARD -j NFQUEUE --queue-num 0
- iptables -A OUTPUT -p udp --dport 53 -j NFQUEUE
- iptables -I INPUT -d [Your Network ip /SubmetMask] /24 -j NFQUEUE --queue-num 0


## install python django module setting apt install python3 python3-pip
- apt install python3-venv
- apt install mysql-server
- apt install default-libmysqlclient-dev
- apt install mysql-client
- pip3 install django
- pip3 install mysqlclient
- pip3 install mysqlclient==1.4.6 or pip3 install --upgrade pip
- pip3 install selenium

## Architecture
![project_architecture](https://github.com/hanmin0512/MITM_DNS/assets/37041208/6b8df0fb-7a6a-4a66-8a8b-eec33be19df3)
<br>
---
![Project_architecture2](https://github.com/hanmin0512/MITM_DNS/assets/37041208/a756c970-cc69-44bf-a75d-36afde4bac21)

## 실행 화면
> ARP_Spoofing, DNS_Spoofing 실행 (KALI Linux)
![스크린샷 2023-07-23 오후 5 49 12](https://github.com/hanmin0512/MITM_DNS/assets/37041208/b5282062-3036-4d15-a922-de1633f73208)

> 피해자PC에서 chrome 브라우저로 eclass 접속 요청 
![스크린샷 2023-07-23 오후 5 50 20](https://github.com/hanmin0512/MITM_DNS/assets/37041208/137b1388-269c-43c5-b0a0-b0685625cedd)

> 파밍사이트(url 주목!)로 리다이렉션 및 로그인정보 입력 
![스크린샷 2023-07-23 오후 5 50 59](https://github.com/hanmin0512/MITM_DNS/assets/37041208/c59c1ffb-1dc7-413f-af30-d2150a606a95)

> 로그인성공한 정보 MySQL DB에 저장된 모습
![스크린샷 2023-07-23 오후 5 59 05](https://github.com/hanmin0512/MITM_DNS/assets/37041208/b2cab53f-b815-45d9-a90c-535a7a3bac93)

> DB정보로 실제 사이트에 로그인 성공
![스크린샷 2023-07-23 오후 5 52 05](https://github.com/hanmin0512/MITM_DNS/assets/37041208/fdb06061-a4d4-41bd-b6ac-a43605c09393)

