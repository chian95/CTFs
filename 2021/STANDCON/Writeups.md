# STANDCON CTF 2021

Writeups for some of the challenges I solved during (and after) the 24-hour CTF held on 24 July 2021

<br>

# **Cryptography**

## Space Papayas

<br>

File: generate.py

Inside the .py file, some values are provided:

```python
# n: 194362842708866084215953237234010601714782092068657017473036251138431676671868175490629669131293355984477767779272247912898398003959598463151066327473719826508089049945621257750848449074932994104814837269421034757100838633416457369464538335095187107124930210006276919089438600966775135156325573710403062047464883549122709123350776456864832248893144446427550937016055121611927144077249211333929866196092711899598411273258926755835322801924551532228696950330545602277465654578138211698686416187777914526845287508335161840449532353167124783735356724420020001236913091469220071460852670489823002071147052631961616736127542307774553784213551564976856862680192529610361702034557744944910925361832621941572380183550749898722374949514136460106207058164376880193895095890731337592265596372136311383975505976373658539080754488958878095929819739059683095890843634555379298978595862942651406158169690562827703147073676346785373790083861582561563008369782363501250191378992269292876039816066218709174263118734404595822048356915079954616024173040278438553459313402270428924062608121168067858306151528190868319071885225544108264749925782330560592480215417954913785029628131817946912132072071073028544681943321456215850218595253490676706062275706321000094834565990465219492368108372464243357854880130522009562946069931768188707691738519573044108555326442766896720655950851164470011771898369770346952788889888492093755625144273054698093660448370077627755233718711030066641378367031583966313900302554231887044203179482191397744246669757016815802390996997529280308699365864745829622981997926231390088157384772877949116604666434897004907955030386342793095734076042434116395844774091900169206181916763238708781774871037938343903139193853528470631949004956352291136030226647324347066772397900205516364442447205487793826622232753382956298250824843380629813818205906683470702831540412778050975345092843721732642350276838457054614948850604421694716563394223556916722778907958340426218859169271015308289476166790080639494788055226687567028709925056618087462428702997126125118029596845966551281440608686343474201915276278183257597304657555212877310709706767336727956810525772106318192285540421821451870148936086342692819049576874727321875121881832817291330007033448759929549864436079804109819708577707453355419019938895736691749711920076052148328406790627343167155687496921184728015803775794667189219633138620080230753579310617631968722793155536612115409526848248365291605624225739530401807631
# e: 65537
# c: 48231407940727026948672141996334529816590411386860292966914913052426047651987115807777841403140631401701249166736959609586369772130907665951564333728016264781106888841594995016670252351243877043043931895035854072541505075903498699581537787497372368026387461275304338678342882903111473016523122047215378268701734813840019057484437006734608455311609606589978328615886021809161996407351531878330820646743145761284259656979198538333302516658013752884296025359474328771699801774792040803990528899610805832697102960908000990289217674047087227612100839918274810879461691566218620108094572187135662070276143399213929056836949141685032577775184655073850890039819023606342148129988769179828433133474387630746462392553047809255640475195268000075192882984582676932698012626821016591108454125334943555006192200330741124548142161400440375747011531508789850387965540536344945763731373457679082441847778497960038863971948480784876442032472906163053089647045655001542030261262366802020060960874257117691078438824193893194414541917317612137645261904776291223687776582045621554101330940016490033717225542054294550509723890916037908439996672821935786685430873048747351042450242135132402651504861858744900133079753832853206911330310597784333649988497694115288456557414447667162368132351388665881330668539885411369791455480519780053033578607022175215519541686716889470249651075696960031469802931249420275612918537198815728307645858921412505760969514941201413816870042202876699227452040578555623960644754047671586444437939411346055325470287778116774616418405759426544629377975037932066699294880194784853999718178319023949211409048595187949438738050805752373774067262605283342238201172745181281789835988232279319864794958750383869310348406998847103542030538181779060240394157480926897363819838099821784624349518599583933815726206097153419947746982886708613483961746873726951138409665385485483718572380938222490388874840647413038783667362727632810016605914301245603947756748870162828963959855754534784070704364459621393050570977513255324417271658411232766634623398123418984633536742998705987579502631970588156672642641810685697296750600811292822227321148497030230391951474359873858004455962186711399896745959043999926635601785091266948248579919445401875107488515808513058701412149085423586181153312241453589223174436758137842395277731895460702559785230565410482969668156381371880091047940473364486255074425419927756644949215073309100344302265133911935519226690015718699828070058406043592623
```

This is RSA encryption with n, e and c values given, so in order to decrypt the ciphertext, n needs to be factorised first to obtain p and q. I used [Alpertron's integer factorization calculator](https://www.alpertron.com.ar/ECM.HTM) to find p and q, then wrote a python script to get the flag:

```python
from Crypto.Util.number import long_to_bytes, inverse

n = 194362842708866084215953237234010601714782092068657017473036251138431676671868175490629669131293355984477767779272247912898398003959598463151066327473719826508089049945621257750848449074932994104814837269421034757100838633416457369464538335095187107124930210006276919089438600966775135156325573710403062047464883549122709123350776456864832248893144446427550937016055121611927144077249211333929866196092711899598411273258926755835322801924551532228696950330545602277465654578138211698686416187777914526845287508335161840449532353167124783735356724420020001236913091469220071460852670489823002071147052631961616736127542307774553784213551564976856862680192529610361702034557744944910925361832621941572380183550749898722374949514136460106207058164376880193895095890731337592265596372136311383975505976373658539080754488958878095929819739059683095890843634555379298978595862942651406158169690562827703147073676346785373790083861582561563008369782363501250191378992269292876039816066218709174263118734404595822048356915079954616024173040278438553459313402270428924062608121168067858306151528190868319071885225544108264749925782330560592480215417954913785029628131817946912132072071073028544681943321456215850218595253490676706062275706321000094834565990465219492368108372464243357854880130522009562946069931768188707691738519573044108555326442766896720655950851164470011771898369770346952788889888492093755625144273054698093660448370077627755233718711030066641378367031583966313900302554231887044203179482191397744246669757016815802390996997529280308699365864745829622981997926231390088157384772877949116604666434897004907955030386342793095734076042434116395844774091900169206181916763238708781774871037938343903139193853528470631949004956352291136030226647324347066772397900205516364442447205487793826622232753382956298250824843380629813818205906683470702831540412778050975345092843721732642350276838457054614948850604421694716563394223556916722778907958340426218859169271015308289476166790080639494788055226687567028709925056618087462428702997126125118029596845966551281440608686343474201915276278183257597304657555212877310709706767336727956810525772106318192285540421821451870148936086342692819049576874727321875121881832817291330007033448759929549864436079804109819708577707453355419019938895736691749711920076052148328406790627343167155687496921184728015803775794667189219633138620080230753579310617631968722793155536612115409526848248365291605624225739530401807631
e = 65537
c = 48231407940727026948672141996334529816590411386860292966914913052426047651987115807777841403140631401701249166736959609586369772130907665951564333728016264781106888841594995016670252351243877043043931895035854072541505075903498699581537787497372368026387461275304338678342882903111473016523122047215378268701734813840019057484437006734608455311609606589978328615886021809161996407351531878330820646743145761284259656979198538333302516658013752884296025359474328771699801774792040803990528899610805832697102960908000990289217674047087227612100839918274810879461691566218620108094572187135662070276143399213929056836949141685032577775184655073850890039819023606342148129988769179828433133474387630746462392553047809255640475195268000075192882984582676932698012626821016591108454125334943555006192200330741124548142161400440375747011531508789850387965540536344945763731373457679082441847778497960038863971948480784876442032472906163053089647045655001542030261262366802020060960874257117691078438824193893194414541917317612137645261904776291223687776582045621554101330940016490033717225542054294550509723890916037908439996672821935786685430873048747351042450242135132402651504861858744900133079753832853206911330310597784333649988497694115288456557414447667162368132351388665881330668539885411369791455480519780053033578607022175215519541686716889470249651075696960031469802931249420275612918537198815728307645858921412505760969514941201413816870042202876699227452040578555623960644754047671586444437939411346055325470287778116774616418405759426544629377975037932066699294880194784853999718178319023949211409048595187949438738050805752373774067262605283342238201172745181281789835988232279319864794958750383869310348406998847103542030538181779060240394157480926897363819838099821784624349518599583933815726206097153419947746982886708613483961746873726951138409665385485483718572380938222490388874840647413038783667362727632810016605914301245603947756748870162828963959855754534784070704364459621393050570977513255324417271658411232766634623398123418984633536742998705987579502631970588156672642641810685697296750600811292822227321148497030230391951474359873858004455962186711399896745959043999926635601785091266948248579919445401875107488515808513058701412149085423586181153312241453589223174436758137842395277731895460702559785230565410482969668156381371880091047940473364486255074425419927756644949215073309100344302265133911935519226690015718699828070058406043592623

p = 440866014463426386957999013624426902916079782103751260466413431135993063177941939376168142215392167989934608705899232210348162286192963032165495898962325992839455843650569123645547538450440590228006724492878040864078704159951574635774324079168892229626975418771205340685180258396619977632982549306289673563315956228841015752793398844056157939224481408840348994779677197962840053569070426238565850395274387409581806166592090397959553713909511769879689744017178844664590111970805370774375455597383152597869473316205391251346542491745013914688670739047752310195692598803804912639945112580217040077236602325593345199422008519013054646685068403432211113358492830623825691038923784505721043387612999762962979942353772901292853898050591913533945797016892436357373382867205395506514695893113831835620663346503535565647752234026309249120744783295735887305741721876915257091980989403202003190640265800327541457736783215623927509959633668247026195836830798878532680019679405812676791364978863729162231705585040020385869653559342220244941429796580828962735914933065034822820567773536823564622041129028808201777802801144985573508200514925370903320877247778767220127865545486223156337390240787774842331656041816506209707305055579168190568065894477
q = 440866014463426386957999013624426902916079782103751260466413431135993063177941939376168142215392167989934608705899232210348162286192963032165495898962325992839455843650569123645547538450440590228006724492878040864078704159951574635774324079168892229626975418771205340685180258396619977632982549306289673563315956228841015752793398844056157939224481408840348994779677197962840053569070426238565850395274387409581806166592090397959553713909511769879689744017178844664590111970805370774375455597383152597869473316205391251346542491745013914688670739047752310195692598803804912639945112580217040077236602325593345199422008519013054646685068403432211113358492830623825691038923784505721043387612999762962979942353772901292853898050591913533945797016892436357373382867205395506514695893113831835620663346503535565647752234026309249120744783295735887305741721876915257091980989403202003190640265800327541457736783215623927509959633668247026195836830798878532680019679405812676791364978863729162231705585040020385869653559342220244941429796580828962735914933065034822820567773536823564622041129028808201777802801144985573508200514925370903320877247778767220127865545486223156337390240787774842331656041816506209707305055579168190568065894603

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
flag = long_to_bytes(pow(c, d, n)).decode()
print(flag)
```

Flag: `STC{where_did_my_space_papayas_go}`

<br>

---

## Substitution Extreme

<br>

File: transmission.txt

Opening the file:

```
--- BEGIN INTERCEPTED TRANSMISSION ---

EZWUFROD HOPVGWUEG GIGRGB HZFUGB PZVGEG WURGU AGPV MZERZMGD IO HZRGMGP HZJZPGPQUPV JZRGAU IO GHOG MZPVVGEG. HOPVGWUEG MZEWOHGB IGEO JGRGAHOG IZPVGP HZRGM QXBXE IO UMGEG, IGP DZWURGUGP EOGU OPIXPZHOG IZPVGP HZRGM HOPVGWUEG IO HZRGMGP. HOPVGWUEG GIGRGB HGRGB HGMU WUHGM DZKGPVGP MZEUPVVUR, IGP IODZPGRO HZFGVGO HZFUGB FGPIGEGAG VRXFGR JZMEXWXROMGP AGPV JZJGOPDGP WZEGPGP WZPMOPV IGRGJ WZEIGVGPVGP IGP DZKGPVGP GPMGEGFGPVHG. WZRGFUBGP HOPVGWUEG JZEUWGDGP HGRGB HZFUGB IGEOWGIG ROJG WZRGFUBGP MZEHOFUD IUPOG.

HUJFZE: KODOWZIOG

--- END INTERCEPTED TRANSMISSION ---
```

This looked like a cryptogram, so I used [quipqiup](https://www.quipqiup.com/), a cryptogram solver, to decode it into the following:

```
REPUBLIK SINGAPURA ADALAH SEBUAH NEGARA PULAU YANG TERLETAK DI SELATAN SEMENANJUNG MELAYU DI ASIA TENGGARA. SINGAPURA TERPISAH DARI MALAYSIA DENGAN SELAT JOHOR DI UTARA, DAN KEPULAUAN RIAU INDONESIA DENGAN SELAT SINGAPURA DI SELATAN. SINGAPURA ADALAH SALAH SATU PUSAT KEWANGAN TERUNGGUL, DAN DIKENALI SEBAGAI SEBUAH BANDARAYA GLOBAL METROPOLITAN YANG MEMAINKAN PERANAN PENTING DALAM PERDAGANGAN DAN KEWANGAN ANTARABANGSA. PELABUHAN SINGAPURA MERUPAKAN SALAH SEBUAH DARIPADA LIMA PELABUHAN TERSIBUK DUNIA. SUMBER: WIKIPEDIA
```

The challenge asked for the first six words of the decrypted transmission, so the flag is `STC{REPUBLIK SINGAPURA ADALAH SEBUAH NEGARA PULAU}`

<br>

---

## Mount Doom

<br>

>KMC{Y4vP_Am4uX_T01k}
>
>Pigk hwol bsvxs

The challenge stated that the author of the encoded message usually ended their message with "With love", thus this provides us with 2 partially known plaintexts:

1. 1st line - STC{????\_?????_????}
2. 2nd line - With love ?????

Using a [Vigenere Decoder](https://www.dcode.fr/vigenere-cipher), I first entered "STC" as the known plaintext word under "Decryption Method", and looking through the results, the first 3 letters of the key could be found: `STA`

Entering "With love" yielded no results, but entering "With lov" gave us another partial key: `TANDWI`

So far it seemed that the key starts with `STANDWI`, but the key length was still unknown, thus I began guessing the key length by adding `?`s to `STANDWI` and seeing if I could recover more of the message. When the partial key input was `STANDWI????`, part of the message was decoded correctly, so I knew the key length had to be 11.

After some guessing, the key turned out to be `STANDWITHUS` and the decoded message was:

```
STC{L4sT_St4nD_B01s}

With love hades
```

Flag: `STC{L4sT_St4nD_B01s}`

<br><br>

# **Misc**

## Mend the lift to Space

<br>

File: liftoff.pass

Opening the file:

```
TeI KrU KrTaCaPtArPoI BiThGdIrScAuZrRnSeHfCaGdClLuGdI TaSrGdRnAuArFrCaBiPoSrPu
```

This took a while, but I realised that they were actually chemical elements, so I used the [Periodic Table Encoder](https://www.dcode.fr/atomic-number-substitution) to replace each element with their corresponding atomic number:

```
52 53 36 92 36 73 20 78 18 84 53 83 90 64 77 21 79 40 86 34 72 20 64 17 71 64 53 73 38 64 86 79 18 87 20 83 84 38 94
```

I then used [CyberChef](https://gchq.github.io/CyberChef/) to convert the numbers to ASCII characters before doing a ROT31, but something seemed off:

```
STC{Ch.m.sTry_l.nGuAg._.f_ThE_un.v.rsE}
```

I ended up using another website http://cyber.meme.tips/xlate/shifts.html with the numbers and finally got the correct flag: `STC{Ch3m1sTry_l4nGuAg3_0f_ThE_un1v3rsE}`

<br><br>

# **Reverse Engineering**

## Airlock Breakout

<br>

Link: 20.198.209.142:55030

When checking the page source of the link, there was a /flag.js; 20.198.209.142:55030/flag.js displayed the source code for getting the flag.

<br>

`unlock()`:

```js
function unlock(pwd) {
    var flagSplit = pwd.split("_");
    if (flagSplit.length !== 6) return false;

    if (part1(flagSplit[0])) console.log("Airlock 1 is opened");
    else return false;
    if (part2(flagSplit[1])) console.log("Airlock 2 is opened");
    else return false;
    if (part3(flagSplit[2], flagSplit[3], flagSplit[4], flagSplit[5]))
        console.log("Airlock 3 is opened");
    else return false;

    alert(`Congratulations!\nFlag: STC{${pwd}}`);
}
```

The `unlock()` function takes in an input that has 6 strings separated by underscores and if it passes all 3 checks, the function will output the flag.

<br>

`part1()`:

```js
function part1(str1) {
    if (str1.length === 5) {
        arr = str1.split("");
        if (
            arr[0] === String.fromCharCode(51) &&
            arr[1] === String.fromCharCode(74) &&
            arr[2] === String.fromCharCode(51) &&
            arr[3] === String.fromCharCode(67) &&
            arr[4] === String.fromCharCode(55)
        )
            return true;
    }
}
```

`str1` can be easily obtained by using `String.fromCharCode(51,74,51,67,55)` to get `3J3C7`.

<br>

`part2()`:

```js
function part2(str2) {
    if (str2.length === 4) {
        if (
            str2.charCodeAt(0) +
                2 * str2.charCodeAt(1) -
                3 * str2.charCodeAt(2) +
                4 * str2.charCodeAt(3) ===
                354 &&
            2 * str2.charCodeAt(0) +
                2 * str2.charCodeAt(1) -
                2 * str2.charCodeAt(2) +
                3 * str2.charCodeAt(3) ===
                383 &&
            3 * str2.charCodeAt(0) -
                2 * str2.charCodeAt(1) -
                4 * str2.charCodeAt(2) +
                str2.charCodeAt(3) ===
                -106 &&
            2 * Math.pow(str2.charCodeAt(0), 3) +
                3 * Math.pow(str2.charCodeAt(1), 2) -
                2 * Math.pow(str2.charCodeAt(2), 3) -
                4 * Math.pow(str2.charCodeAt(3), 2) ===
                59284
        )
            return true;
    }
}
```

For `str2`, I used [SageMathCell](https://sagecell.sagemath.org/) to solve the equations in `part2()`:

```python
var('a b c d')
(a, b, c, d)

eq1 = a+2*b-3*c+4*d==354
eq2 = 2*a+2*b-2*c+3*d==383
eq3 = 3*a-2*b-4*c+d==-106
eq4 = 2*(a**3)+3*(b**2)-2*(c**3)-4*(d**2)==59284

solve([eq1,eq2,eq3,eq4], a, b, c, d)
```

```
[[a == 55, b == 72, c == 51, d == 77], [a == -3/5768*I*sqrt(182771967) + 31789/824, b == 57/23072*I*sqrt(182771967) + 494401/3296, c == -27/11536*I*sqrt(182771967) - 37731/1648, d == -33/11536*I*sqrt(182771967) - 21945/1648], [a == 3/5768*I*sqrt(182771967) + 31789/824, b == -57/23072*I*sqrt(182771967) + 494401/3296, c == 27/11536*I*sqrt(182771967) - 37731/1648, d == 33/11536*I*sqrt(182771967) - 21945/1648]]
```

Using the first solution, `String.fromCharCode(55,72,51,77)` outputs `7H3M`.

<br>

`part3()`:

```js
function part3(str3, str4, str5, str6) {
    var magic = 0;
    for (var strs of [str3, str4, str5, str6]) {
        if (!/^[01347CFHKLNRUX]+$/g.test(strs)) return false;

        for (var i = 0; i < strs.length; i++) {
            magic = (magic << 3) + strs.charCodeAt(i) - magic;
        }
    }

    if (
        str3.length === 3 &&
        str4.length === 2 &&
        str5.length === 3 &&
        str6.length > 5 &&
        str3[0] === "0" &&
        str5[0] === "7" &&
        str3.charCodeAt(0) + str5.charCodeAt(0) - str6.charCodeAt(0) === 51 &&
        str3.charCodeAt(0) === str4.charCodeAt(0) &&
        str3.charCodeAt(2) - str3.charCodeAt(1) === -30 &&
        (str4.charCodeAt(1) / 7) * str5.charCodeAt(1) === 720 &&
        (str5.charCodeAt(0) + str5.charCodeAt(2) + 2) / 3 === 36 &&
        str6.charCodeAt(3) - str6.charCodeAt(2) === -6 &&
        str6.charCodeAt(2) * str6.charCodeAt(4) === 3936 &&
        magic === -859895409
    )
        return true;
}
```

Using SageMathCell again:

```python
var('s31 s32 s33 s41 s42 s51 s52 s53 s61 s62 s63 s64 s65 s66')
(s31, s32, s33, s41, s42, s51, s52, s53, s61, s62, s63, s64, s65, s66)

eq1 = s31+s51-s61==51
eq2 = s31==s41
eq3 = s33-s32==-30
eq4 = (s42/7)*s52==720
eq5 = (s51+s53+2)/3==36
eq6 = s64-s63==-6
eq7 = s63*s65==3936

solve([eq1,eq2,eq3,eq4,eq5,eq6,eq7,s31==48,s51==55], s31, s32, s33, s41, s42, s51, s52, s53, s61, s62, s63, s64, s65, s66)
```

```
[[s31 == 48, s32 == r1, s33 == r1 - 30, s41 == 48, s42 == 5040/r2, s51 == 55, s52 == r2, s53 == 51, s61 == 52, s62 == r3, s63 == 3936/r4, s64 == -6*(r4 - 656)/r4, s65 == r4, s66 == r5]]
```

Other than satisfying the above equations, `if (!/^[01347CFHKLNRUX]+$/g.test(strs)) return false;` in `part3()` means that `str3`, `str4`, `str5` and `str6` must only contain the following characters (with repeats allowed): 0, 1, 3, 4, 7, C, F, H, K, L, N, R, U, X

I then created lists of possible strings for `str3`, `str4`, `str5` and `str6` that satisfied those 2 conditions:

```js
// unknowns
var s32 = 0; var s52 = 0; var s62 = 0; var s65 = 0; var s66 = 0;

// known chars
var s31 = 48; var s41 = 48; var s51 = 55; var s53 = 51; var s61 = 52;

// list of possible chars
const possible_chars = "01347CFHKLNRUX";
const charlist = [];
for (var i in possible_chars) charlist.push(possible_chars.charCodeAt(i));
// charlist = [48, 49, 51, 52, 55, 67, 70, 72, 75, 76, 78, 82, 85, 88]

// list of possible str3 inputs
const strings3 = [];
for (var vals of charlist) {
  s32 = vals; var s33 = s32 - 30;
  if (charlist.includes(s33)) strings3.push(String.fromCharCode(s31,s32,s33));
}

// list of possible str4 inputs
const strings4 = [];
for (var vals of charlist) {
  var s42 = 5040/vals;
  if (charlist.includes(s42)) strings4.push(String.fromCharCode(s41,s42));
}

// list of possible str5 inputs
const strings5 = [];
for (var vals of charlist) {
  var s52 = 5040/vals;
  if (charlist.includes(s52)) strings5.push(String.fromCharCode(s51,s52,s53));
}

// list of possible str6 inputs
const strings6 = [];
for (var vals3 of charlist) {
  for (var vals2 of charlist) {
    for (var vals1 of charlist) {
      s62 = vals1; s65 = vals2; s66 = vals3;
      var s63 = 3936/s65; var s64 = -6*(s65 - 656)/s65;
      if (charlist.includes(s63) && charlist.includes(s64))
        strings6.push(String.fromCharCode(s61,s62,s63,s64,s65,s66));
    }
  }
}
```

Iterating through the lists, no results were found when length of `str6` = 6; with length = 7, the flag was found:

```js
var str1 = String.fromCharCode(51,74,51,67,55); // str1 = "3J3C7"
var str2 = String.fromCharCode(55,72,51,77);    // str2 = "7H3M"

const strings6_len7 = [];
for (var str6 of strings6)
  for (var chr of possible_chars)
    strings6_len7.push(str6+chr);

for (var str6 of strings6_len7)
  for (var str5 of strings5)
    for (var str4 of strings4)
      for (var str3 of strings3)
        if (part3(str3,str4,str5,str6))
          unlock(str1+"_"+str2+"_"+str3+"_"+str4+"_"+str5+"_"+str6)
```

```
Airlock 1 is opened
Airlock 2 is opened
Airlock 3 is opened
Congratulations!
Flag: STC{3J3C7_7H3M_0U7_0F_7H3_41RL0CK}
```

Flag: `STC{3J3C7_7H3M_0U7_0F_7H3_41RL0CK}`