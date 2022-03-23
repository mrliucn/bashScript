import os


def home():
    print("""
  欢迎使用自制Termux安装脚本
  0.退出脚本
  1.安装更新必要依赖+替换源
  2.安装x-ui
  3.安装nodejs
  4.安装acme脚本
  5.全部安装
    """
          )
    nu = input("输入你的选择[0-5]：")
    if nu == "0":
        exit()
    if nu == "1":
        install_yi()
    # if nu == "2":
    #     install_xui()
    # if nu == "3":
    #     install_yil()
    # if nu == "4":
    #     install_acme()
    # if nu == "5":
    #     allinstall()
    else:
        print("输入错误，请重新选择\n")
        home()


def install_yi():
    print("\n替换源\n")
    os.system("""sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list""")
    os.system("""sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list""")
    os.system("""sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list""")
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git curl vim wget -y")
    home()
