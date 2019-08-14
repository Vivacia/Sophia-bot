import random
import base64

lefts = ["ヽ(", "(╯", "¯\_(", "(", "\(", "(∩", "｡･ﾟﾟ･(", "°˖✧◝(", "ᕕ(", "(｡", "─=≡Σ(((つ", "(/", "⊂(", "ᕙ("]

rights = [")ﾉ", "）╯", ")_/¯", ")", ")/", ")⊃━☆ﾟ.*･｡ﾟ", ")･ﾟﾟ･｡", ")◜✧˖°", ")ᕗ", "｡)", ")つ", ")⊃"]

eyes = ["－", "ლ", "ಠ", "ఠ", "ﾟ", "͡°", "^", "｀", "´" "＾", ">", "<", "⁰", "ʘ", "◕", "°", "・", "⌒", "≧", "≦", "⇀", "↼", "T"]

mouths = ["‸", "Д", " ͜ʖ", "_", ".", "-", "○", "д", "▿", "‿", "‿‿", "□", "ل͜", "ω"]
   
def emotes(mess):       
    if "\o/" in mess:
        return("\o/ Yay!")

    elif "!panic" in mess or "/panic" in mess:
        return("｡ﾟ(ﾟ `Д)ﾉ｡ﾟヽ(   )ﾉﾟ｡ヽ(Д´ ﾟ)ﾉﾟ｡｡ﾟヽ(ﾟ`Д´ﾟ)ﾉﾟ")

    elif "!ohno" in mess or "/ohno" in mess:
        return("ヽ（゜ロ゜；）ノ")
        
    elif "!rimshot" in mess or "/rimshot" in mess:
        return("Ba dum tssh!")

    elif "!shrug" in mess or "whyy" in mess:
        return("¯\_(ツ)_/¯")

    elif "!facepalm" in mess or "!fp" in mess or "/fp" in mess or "/facepalm" in mess:
        return("(－‸ლ)")

    elif "!tableflip" in mess:
        return("(╯°□°）╯︵ ┻━┻")

    elif "!flipharder" in mess or "/flipharder" in mess:
        return("(ノಠ益ಠ)ノ彡 ┻━┻")

    elif "!fliphardest" in mess or "/fliphardest" in mess:
        return("(ノϬДϬ)ノ彡┴─ ҉ ─┬")

    elif "!doubleflip" in mess or "doubleflip" in mess:
        return("┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")

    elif "!tableset" in mess or "/tableset" in mess:
        return("┬──┬ ノ( ゜-゜ノ)")

    elif "!fiteme" in mess or "/fiteme" in mess:
        return("ᕙ( •̀ ︿•́ )ᕗ")

    elif "!lenny" in mess or "!eyebrows" in mess or "lenny" in mess or "/eyebrows" in mess:
        return("( ͡° ͜ʖ ͡°)")

    elif "!no" in mess or "/no" in mess:
        return("ಠ_ಠ")

    elif "!creeper" in mess or "/creeper" in mess:
        return("ʘ‿ʘ")

    elif "!guns" in mess or "/guns" in mess:
        return(" - - - - ╾━╤デ╦︻--(°□°)--︻╦╤─ - - - -")

    elif "!magic" in mess or "/magic" in mess:
        return("(∩｀-´)⊃━☆ﾟ.*･｡ﾟ")

    elif "!wandblast" in mess or "/wandblast" in mess:
        return("ᕕ(ಠ‸ಠ)⊃━☆ﾟ.*･｡ﾟ ｡･ﾟﾟ･ °˖✧◝(ʘ□ʘ) ･ﾟﾟ･")

    elif "!wizard" in mess or "/wizard" in mess:
        return("ᕕ(ಠ‸ಠ)⊃━☆ﾟ.*･｡ﾟ")

    elif "!magewar" in mess or "/magewar" in mess:
        return("ᕕ(ಠ‸ಠ)⊃━☆ﾟ.*･｡ﾟ ｡･ﾟﾟﾟ｡･*.ﾟ☆━c(`Д´)ﾉ")

    elif "!ugh" in mess or "/ugh" in mess:
        return("(╯⇀д⇀)/")

    elif "!nervous" in mess or "/nervous" in mess:
        return("(｡ʘ‸ʘ)/")

    elif "!run" in mess or "/run" in  mess:
        return("ヽ(ﾟДﾟ)ﾉ")

    elif "!cry" in mess or "/cry" in mess:
        return("｡･ﾟﾟ･(>д<)･ﾟﾟ･｡")

    elif "!aww" in mess or "so cute" in mess or "/aww" in mess:
        return("(｡◕‿◕｡)")

    elif "!yeah" in mess or "/yeah" in mess:
        return("( •_•) \n ( •_•)>⌐■-■ \n (⌐■_■)")

    elif "!dealwithit" in mess or "!deal" in mess or "/deal" in mess:
        return("(⌐■_■)")

    elif "!cock" in mess or "!dick" in mess or "!penis" in mess or "/dick" in mess or "/penis" in mess or "/cock" in mess:
        return("8================================D")

    elif "!highfive" in mess or "/highfive" in mess:
        return("\(＾○＾)人(＾○＾)/")

    elif "!procemo" in mess or "/procemo" in mess:
        return(str(random.choice(lefts) + random.choice(eyes) + random.choice(mouths) + random.choice(eyes) + random.choice(rights)))
