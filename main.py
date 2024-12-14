import PasswdManager as pm


def main():
    choice = int(input("Press 1 to save. Press 2 to search:"))
    if choice == 1:
        abs_path = input("Drag your file here:")
        passwd = input("Input the password:")
        z = pm.ZipPkg(abs_path=abs_path, passwd=passwd)
        pm.addZipPkg(z)
    if choice == 2:
        abs_path = input("Drag your file here:")
        print(pm.searchZipPkgPasswd(abs_path))

if __name__ == "__main__":
    main()