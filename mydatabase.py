from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    password: str
    kr: int
    guns: list

@dataclass
class Gun:
    gid: int
    name: str
    image_path: str
    cost: int

IMAGEDIR = "images/"
guntab = [
    Gun(0, "Akimbo Uzi",     IMAGEDIR + "akimbo.png",        50),
    Gun(1, "Knife",          IMAGEDIR + "knife.png",         25),
    Gun(2, "Machine Gun",    IMAGEDIR + "machinegun.png",    100),
    Gun(3, "Pistol",         IMAGEDIR + "pistol.png",        10000),
    Gun(4, "Revolver",       IMAGEDIR + "revolver.png",      150),
    Gun(5, "Assault Rifle",  IMAGEDIR + "rifle.png",         200),
    Gun(6, "Shotgun",        IMAGEDIR + "shotgun.png",       300),
    Gun(7, "Sniper Rifle",   IMAGEDIR + "sniper.png",        500),
]

class UserDatabase(dict):
    def __init__(self, pathname):
        self.pathname = pathname
        def parse_guns(gunstr):
            if gunstr == "":
                return []
            return [int(gun_id) for gun_id in gunstr.split(',')]
        with open(pathname) as f:
            for line in f:
                user, password, kr, gunstr = line.strip().split('=', 4)
                userinfo = UserInfo(user, password, int(kr), parse_guns(gunstr))
                self.__setitem__(user, userinfo)

    def write(self):
        with open(self.pathname, "w") as out:
            for key in self.__iter__():
                user = self.__getitem__(key)
                out.write(user.name + '=' + user.password + '=' + str(user.kr) + '=')
                for i in range(0, len(user.guns) - 1):
                    out.write(str(user.guns[i]) + ',')
                out.write(str(user.guns[len(user.guns)-1]))
                out.write('\n')

    def __getitem__(self, key):
        return dict.__getitem__(self, key)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)

