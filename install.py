import os


def car(i, c=1):
    red = "\033[0;31m"
    end = "\033[0m"
    green = "\033[0;32m"
    if c == 1 or c != 2:
        print(f"{red}{i}{end}")
    if c == 2:
        print(f"{green}{i}{end}")


def home():
    print("""
                          ./+o+-
                  yyyyy- -yyyyyy+      
               ://+//////-yyyyyyo      
           .++ .:/++++++/-.+sss/`      
         .:++o:  /++++++++/:--:/-      
        o:+o+:++.`..```.-/oo+++++/    
       .:+o:+o/.          `+sssoo+/    
  .++/+:+oo+o:`             /sssooo.   
 /+++//+:`oo+o               /::--:.   
 \+/+o+++`o++o               ++////. 
  .++.o+++oo+:`             /dddhhh.
       .+.o+oo:.          `oddhhhh+
        \+.++o+o``-````.:ohdhhhhh+
         `:o+++ `ohhhhhhhhyo++os:
           .o:`.syhhhhhhh/.oo++o`
               /osyyyyyyo++ooo+++/
                   ````` +oo+++o\:
                          `oo++.
    
  欢迎使用自制Linux安装脚本：
  0.退出脚本            1.安装 Docker
  2.安装 v2ray管理面版   3.安装 更新必要依赖
  4.安装 acme脚本       5.全部安装
    """
          )
    nu = input("输入你的选择[0-5]：")
    if nu == "0":
        exit()
    if nu == "1":
        install_docker()
    if nu == "2":
        install_xui()
    if nu == "3":
        install_yil()
    if nu == "4":
        install_acme()
    if nu == "5":
        allinstall()
    else:
        print("\n输入错误，请重新选择\n")
        home()


def install_docker():
    os.system("apt-get update && apt upgrade -y")
    os.system("apt-get install curl -y")
    os.system("curl -fsSL https://get.docker.com | bash")
    home()


def install_xui():
    os.system("apt-get update && apt upgrade -y")
    os.system("bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)")
    home()


def install_yil():
    os.system("apt-get update && apt upgrade -y")
    os.system("apt-get install socat git curl vim wget ffmpeg -y")
    home()


def install_acme():
    os.system("apt-get update && apt upgrade -y")
    os.system("apt-get install socat")
    email = input("输入你的邮箱地址：")
    domain = input("输入要安装证书的域名：")
    os.system(f"curl https://get.acme.sh | sh -s email={email}")
    print("\n开始安装证书\n")
    os.system(f"~/.acme.sh/acme.sh --issue -d {domain} --standalone")
    print("\n开始复制证书到本地\n")
    os.system("~/.acme.sh/acme.sh --install-cert -d --key-file /root/private.key --fullchain-file /root/cert.crt")
    home()


def allinstall():
    install_docker()
    install_yil()
    install_xui()
    install_acme()
    home()


if __name__ == '__main__':
    home()
