# preliminary junk code generator

nops = [
    # {aaa,... }
    0x27, 0x2F, 0x37, 0x3F,
    # {inc/dec}
    0x40, 0x41, 0x42, 0x43, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4E, 0x4F,
    # nop
    0x90,
    #xchg
    0x91, 0x92, 0x93, 0x96, 0x97,
    # complements
    0x98, 0x99,
    # fwait
    0x9B,
    # lahf
    0x9F,
    # setalc
    0xD6,
    # C/D flags
    0xF5, 0xF8, 0xF9, 0xFC, 0xFD, 
    ]