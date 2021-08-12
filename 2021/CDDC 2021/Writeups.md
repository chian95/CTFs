# CDDC 2021 Writeups

Writeups for the challenges I solved during the ~~48~~ 36-hour (shortened due to an outage in the CTF platform) CTF held from 23 to 25 Jun 2021. Categories included:

- [Reverse Eng](#reverse-eng)
- [Forensics](#forensics)
- [Recon](#recon)
- [OSINT](#osint)
- [Crypto](#crypto)

<br><br>

# **Reverse Eng**

## Alarm

<br>

File: [alarm](ReverseEng/alarm)

When running the file, a password is required to retrieve the flag:

![re1](img/re1.png?raw=true)

Importing the file to Ghidra and looking at the main function, the password can be easily deduced to be `KZeMZaSr`:

![re2](img/re2.png?raw=true)

Entering the password gives us the flag:

![re3](img/re3.png?raw=true)

Flag: `CDDC21{k5JkMxP66d}`

<br><br>

# **Forensics**

## Look Closer

<br>

File: [data.txt](Forensics/data.txt)

The file when decoded in base64 is a hexdump of what seems to be an ELF file, but with the file signature altered:

![fr1](img/fr1.png?raw=true)

Changing the file signature from `43 44 44 43` to `7F 45 4C 46`:

![fr2](img/fr2.png?raw=true)

Reversing hexdump on the amended file then running the output displays the flag:

![fr3](img/fr3.png?raw=true)

Flag: `CDDC21{C@n_Y0u_F1nD_mE?}`

<br><br>

# **Recon**

## unKnown

<br>

Doing a Nmap scan revealed an open port 666 with a service named 'doom'; using the `curl` command on that port returned gibberish, but it was actually the binary of a compressed file when taking a closer look:

![rc1](img/rc1.png?raw=true)

The entire chunk of text was then output to a new file. Using the `file` command, it was confirmed that the file was a zip archive, so the file extension was changed to `.zip`. Unzipping it gave us `file.tar`, and extracting that gave us the following image:

![rc2](img/rc2.png?raw=true)

Flag: `CDDC21{Y0u_Figu4ed_IT_0UT}`

<br>

---

## Mounting

<br>

From the Nmap scan, there were a RPCBind service (port 111) and a Network File System (NFS) service (port 2049), which meant that we were required to access files across a network by mounting a NFS share.

Following this [guide on NFS share mounting](https://medium.com/@sebnemK/how-to-bypass-filtered-portmapper-port-111-27cee52416bc), the flag was obtained:

![rc3](img/rc3.png?raw=true)

![rc4](img/rc4.png?raw=true)

Flag: `CDDC21{I_L1ve_in_Ke4neL_L4ND}`

<br><br>

# **OSINT**

## Broken System

<br>

Searching for "Cryptit Banking" on Google yielded a website cryptit.biz. However, there was nothing useful on that website, so the next thing I tried was the `dig` command.

Running `dig +short ns cryptit.biz` to get a list of all the name servers, then running `dig axfr` on each name server until the flag was found:

![os1](img/os1.png?raw=true)

Flag: `CDDC21{_10x_f0r_yOur_Serv!ce_}`

<br>

---

## Track Him Down (Solved after CTF was over)

<br>

Searching for "Tesla Reactor" on YouTube led to a [video](https://www.youtube.com/watch?v=XP5DJ55LXRM), and looking through the channel, an email address was found in the About section: teslareactor7@gmail.com

Using this [Gmail OSINT guide](https://medium.com/hacking-info-sec/how-to-gmail-osint-like-a-boss-1ca4f55f55e2), the user id of the gmail address was found to be `105865555829030607150`:

![os2](img/os2.jpg?raw=true)

The flag can then be found by going to Google Maps with the id (https://www.google.com/maps/contrib/105865555829030607150), under the 'Reviews' section:

![os3](img/os3.jpg?raw=true)

Flag: `CDDC21{tR4cK1nGFr4NZy}`

<br><br>

# **Crypto**

## Transatlantic

<br>

File: [GDC_ENCRYPTED](Crypto/Transatlantic/GDC_ENCRYPTED)

Opening the file:

```
Gh
Tr!h}DeChisa C D!p_t  bDstn_ ieC_i0h ss230t@  t1nn_r t!{c_td 
```

Using the [Caesar Box Decoder](https://www.dcode.fr/caesar-box-cipher), the flag can be obtained:

```
GDC·is·the·best!·CDDC21{Th!s_3ncripti0n_!s_n0t_that_h@rd}·······
```

Flag: `CDDC21{Th!s_3ncripti0n_!s_n0t_that_h@rd}`

<br>

---

## Never

<br>

Files: [data](Crypto/Never/data), [gdc_secret](Crypto/Never/gdc_secret)

Opening `data`:

```
TG\EV^_WVVXG\I^DLG:TG\EV^_WV]TEN_DUV@^;TORBV^WYQCDWQC^DWSP_USUBTCMI^D;wRFTC^X^_PTV[THVBRCH3yUGTCP___PDQHVVXTSHT3yUGTCP___PCU]]X\XTXYTYDKCH^D3=suurKxEny[\nEXEDTUnm__L;
```

Knowing that the text was encrypted using a XOR Cipher with a key length of 6, the [XOR Decoder](https://www.dcode.fr/xor-cipher) can be used to decrypt it through brute force:

```
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

CDDC21{It_@ll_$tarted_Th3n}
```

Flag: `CDDC21{It_@ll_$tarted_Th3n}`

<br>

---

## Another Base (Solved after CTF was over)

<br>

File: [gdc_data](Crypto/Another_Base/gdc_data)

Opening the file:

```
EdEQyBpcyBub3QgdGhhdCBnb29kIGluIGhpZGluZyB0aGVpciBpbmZvcm1hdGlvbi4uLgoK
UC5TLiBUaGUgZmxhZyBpcyBub3QgaGVyZS4gU29ycnkuLi4K
OJZXG4TBMBGHCMSEORRGCMCQIQYEIRJ2MBQDAOR7GATEIYTONZHAU===
```

It seemed that the 3 lines were all encrypted differently, with the 2nd line being `P.S. The flag is not here. Sorry...` when decoded in base64. 

Using [CyberChef's](https://gchq.github.io/CyberChef/) Magic operation on the 3rd line, the suggested operation was to decode in base32, resulting in ```rssra`Lq2Dtba0PD0DE:``0:?0&DbnnN```; doing a ROT47 after that would return the flag.

Flag: `CDDC21{BasE32_!s_sti11_in_Us3??}`