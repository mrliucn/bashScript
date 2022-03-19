#! /bin/bash
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
plain='\033[0m'
echo -e "${green}***********************************${plain}\n
${green}开始准备安装前更新；${plain}\n
${green}***********************************${plain}\n"
apt update && apt upgrade -y

echo -e "${green}***********************************${plain}\n"
echo -e "${green}安装依赖；${plain}\n"
echo -e "${green}***********************************${plain}\n"
apt-get install vim wget curl git openssl python3 socat -y

echo -e "${green}***********************************${plain}\n"
echo -e "${green}安装Docker；${plain}\n"
echo -e "${green}***********************************${plain}\n"
read -p "是否安装Docker(y/n)" wen
if ( $wen == y || $wen == Y );then
	curl -Ls https://get.docker.com | bash
else
	echo -e "${red}你选择不安装Docker${plain}\n"
fi

echo -e "${green}***********************************${plain}\n"
echo -e "${green}安装x-ui；${plain}\n"
echo -e "${green}***********************************${plain}\n"
read -p "是否安装x-ui(y/n)" xu
if ( $xu == y || $xu == Y );then
	bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)
else
	echo -e "${red}你选择不安装x-ui${plain}\n"
fi
echo -e "${green}***********************************${plain}\n"
echo -e "${green}安装acme；${plain}\n"
echo -e "${green}***********************************${plain}\n"
read -p "是否安装acme脚本?(y/n)" ac
if ( " $ac " = y || " $ac " = Y ); then
	read -p "输入Emaild地址：" em
	read -p "输入域名：" domain
	read -p "输入端口：" pro
	curl https://get.acme.sh | sh -s email=${em}
	alias acme.sh=~/.acme.sh/acme.sh
	~/.acme.sh/acme.sh  --issue  -d ${domain}  --standalone --httpport ${pro}
else
	echo -e "${red}你选择不安装acme${plain}\n"
fi
