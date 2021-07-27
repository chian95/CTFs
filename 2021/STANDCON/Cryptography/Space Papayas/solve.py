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