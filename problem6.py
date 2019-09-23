print("code for problem6")

dsi={}
dsi=dict()
for i in range (0,3):
    names=list()
    usns=list()
    n=input("name: ")
    names.append(str(n))
    x=input("usn:")
    usns.append(str(x))
    dsi[f"{usns}"]=f"{names}"
#return dsi
print(f"{dsi}")



