def TroyMartian(antenna, eyes, real):
  if real == True:
    return "yes"
  else:
    if antenna >= 3 and eyes <= 4:
      real = True
      return TroyMartian(antenna, eyes, real)
    else:
      return "no"


def VladSaturnian(antenna, eyes, real):
  if real == True:
    return "yes"
  else:
    if antenna <= 6 and eyes >= 2:
      real = True
      return VladSaturnian(antenna, eyes, real)
    else:
      return "no"

def GraemeMercurian(antenna, eyes, real):
  if real == True:
    return "yes"
  else:
    if antenna <= 2 and eyes <= 3:
      real = True
      return GraemeMercurian(antenna, eyes, real)
    else:
      return "no"

def main():
  antenna = int(input())
  eyes = int(input())
  real = False
  TM = TroyMartian(antenna, eyes, real)
  VS = VladSaturnian(antenna, eyes, real)
  GM = GraemeMercurian(antenna, eyes, real)
  if TM == "yes":
    print("TroyMartian")
  if VS == "yes":
    print("VladSaturnian")
  if GM == "yes":
    print("GraemeMercurian")
main()
