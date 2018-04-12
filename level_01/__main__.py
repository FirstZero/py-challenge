if __name__ == '__main__':
    data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    intab = 'abcdefghijklmnopqrstuvwxyz'
    outtab = 'cdefghijklmnopqrstuvwxyzab'

    transtab = str.maketrans(intab, outtab)

    print(data.translate(transtab))
    print('map.html'.translate(transtab))
