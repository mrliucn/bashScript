import os


def home():
    print("""  _____                              
 |_   _|__ _ __ _ __ ___  _   ___  __
   | |/ _ \ '__| '_ ` _ \| | | \ \/ /
   | |  __/ |  | | | | | | |_| |>  < 
   |_|\___|_|  |_| |_| |_|\__,_/_/\_\\

  欢迎使用自制Termux安装脚本
  0.退出脚本      1.安装 更新必要依赖+换源
  2.安装 node    3.安装 Aria2
    """)
    nu = input("输入你的选择[0-5]：")
    if nu == "0":
        exit()
    if nu == "1":
        install_yi()
    if nu == "2":
        install_node()
    if nu == "3":
        install_ar()
    # if nu == "4":
    #     install_acme()
    # if nu == "5":
    #     allinstall()
    else:
        print("\n输入错误，请重新选择\n")
        home()


def install_yi():
    print("\n替换源\n")
    os.system(
        "sed -i 's@^\(deb.*stable main\)$@#\\1\\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list")
    # os.system("sed -i 's@^\(deb.*games stable\)$@#\\1\\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list")
    os.system(
        "sed -i 's@^\(deb.*science stable\)$@#\\1\\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list")
    print("\n安装依赖\n")
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git curl vim wget tree openssh ffmpeg nmap figlet neofetch screenfetch -y")
    print("\n终端配色方案\n")
    os.system('sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"')
    os.system("cd $HOME && ln -s /sdcard/Download d")
    print("\n安装you-get和yt-dlp\n")
    os.system("pip install you-get yt-dlp")
    home()


def install_node():
    print("\n1.安装长期稳定版  2.安装最新版\n")
    u = input("输入你的选择[1-2]：")
    if u == "" or u == "1":
        os.system("pkg install nodejs-lts -y")
    elif u == "2":
        os.system("pkg install nodejs -y")
    else:
        print("\n错误的选择\n")
        install_node()
    print("\n安装PM2\n")
    os.system("npm install -g pm2 pnpm")
    home()


def install_ar():
    install_node()
    print("\n安装并配置Aria2\n")
    os.system("pkg install aria2 -y")
    os.system("cd $HOME && mkdir .aria2 && cd .aria2")
    os.system("wget -O aria2.conf https://github.com/mrliucn/bashScript/raw/main/conf/aria2.conf")
    os.system("touch aria2.session")
    print("\n启动Aria2\n")
    os.system("pm2 start 'aria2c --conf-path=$HOME/.aria2/aria2.conf'")


if __name__ == '__main__':
    home()
