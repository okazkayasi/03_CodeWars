def encode_str(strng, shift):
    lett = chr(ord(strng[0].lower()) - shift)
    passw = lett + chr(ord(lett)+shift)
    print len(strng)

    strng = passw + strng
    l = len(strng)
    if l == 0:
        return ""

    # try equal length
    four_len = 0
    fif_len = 0

    if l%5 == 0:
        four_len = l/5
        fif_len = l/5
    else:
        four_len = l/5
        fif_len = l - four_len*4
        while fif_len > four_len:
            four_len += 1
            fif_len = l - four_len*4


    parts = []
    at = 0
    for i in range(4):
        part = strng[i*four_len:(i+1) * four_len]
        added = ""
        for chrs in part:
            if chrs.isalpha():
                added += chr(ord(chrs)+shift)
            else:
                added += chrs
        parts.append(added)

    part = strng[4*four_len:]
    added = ""
    for chrs in part:
        if chrs.isalpha():
            added += chr(ord(chrs)+shift)
        else:
            added += chrs
    parts.append(added)

    return parts


    #your code

def decode(arr):

    decoder = arr[0][:2]
    decoder_num = ord(decoder[1]) - ord(decoder[0])
    arr[0] = arr[0][2:]
    read = ""
    for part in arr:
        for c in part:
            if c.isalpha():
                new = chr(ord(c) - decoder_num)
                read += new
            else:
                read += c

    return read



v = ['ijJ ibwf tqsfbe nz esfb', 'nt voefs zpvs gffu; Usf', 'be tpgumz cfdbvtf zpv u', 'sfbe po nz esfbnt. Xjmm', 'jbn C Zfbut (1865-1939)']

u = 'I have spread my dreams under your feet; Tread softly because you tread on my dreams. William B Yeats (1865-1939)'
print decode(v)
