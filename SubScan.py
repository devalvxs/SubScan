from colorama import init, Fore, Back

init()

import requests

subdominio=["teste","backup","mail","admim","adm","interno","ínicio","admin","dev","secure","vpn","root","access","gateway","private","public","hidden","proxy","shadow","firewall","intrusion","exploit","malware","virus","trojan","botnet","phishing","spoof","breach","crack","hack","blackhat","whitehat","cipher","decrypt","encrypt","anon","tor","darkweb","ghost","ninja","silenthacker","cyber","matrix","byte","kernel","payload","zero-day","backdoor","worm","snake","spyware","rootkit","keylogger","ransomware","cypher","algorithm","crash","overload","overclock","anomaly","echo","cascade","stealth","cloak","invisible","mystery","mask","veil","conceal","furtive","covert","shroud","sneak","unseen","incognito","whisper","silent","quiet","undercover","encrypted","classified","untraceable","undetectable","disguised","camouflaged","obscured","furtive","clandestine","cryptic","mysterious","enigmatic","submerged","veiled","covert","surreptitious","sub rosa","top secret","confidential","covert","cloaked","sheltered","hidden","concealed","inconspicuous","latent","secluded","sly","covertness","furtiveness","clandestineness","conspiracy","secrecy","sneakiness","subterfuge","underhandedness","disguise","masking","veiling","cloak-and-dagger","hush-hush","behind-the-scenes","under-the-table","secretive","underground","stealthy","privy","hushed","sneaky","backstairs","furtive","on the Q.T.","hole-and-corner","backstair","in camera","close","closed","discreet","reserved","reticent","silent","taciturn","tight-lipped","uncommunicative","unforthcoming","repressed","withdrawn","mute","unspoken","unvoiced"]

site=input(Fore.BLUE+"NOME OU URL DO SITE QUE DESEJA ESCANEAR SUBDOMINIOS: ")

if not site.endswith(".com"):
    site += ".com"

for sub in subdominio:

    teste = "https://"+sub+"."+site
    
    if site.startswith("https://"):
        teste = "https://"+sub+"."+site.lstrip("https://")

    try:
        requisicao = (requests.get(teste)) 
        if requisicao.status_code == 200:
            print(Fore.GREEN+"Site encontrado! | "+ teste)
        else:
            print(Fore.YELLOW + "Site encontrado, mas com código de status diferente de 200! | " + teste)
    except:
        print(Fore.RED+"Nada encontrado! | "+ teste)