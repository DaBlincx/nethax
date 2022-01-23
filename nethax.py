pName = "netHax"
pDescription = "Nethacking Toolbox"
pAuthor = "DaBlincx"
pSource = "https://www.github.com/DaBlincx/nethax"
pVersion = 1.3
debugMode = False



moduleslib = []

try: import pyfiglet
except: moduleslib.append("pyfiglet")

try: from rich.console import Console
except: moduleslib.append("rich.console (rich)")

try: from rich.progress import Progress,track
except: moduleslib.append("rich.progress (rich)")

try: from rich.panel import Panel
except: moduleslib.append("rich.panel (rich)")

try: from rich.prompt import *
except: moduleslib.append("rich.prompt (rich)")

try: from os import walk
except: moduleslib.append("os")

try: import time
except: moduleslib.append("time")

try: import subprocess
except: moduleslib.append("subprocess")

try: import random
except: moduleslib.append("random")

try: import string
except: moduleslib.append("string")

try: from sys import *
except: moduleslib.append("sys")

    
def importError():
    print("Cannot import all needed librarys, \nplease make sure to have every one installed.\n\nUsage: 'pip install [module]' or 'pip3 install [module]'\n")
    print("modules:")
    for modl in moduleslib:
        print(modl)
    print()
    exit()

pwlist = [
    "password","123456789","12345678","1q2w3e4r","sunshine","football","1234567890","computer","superman","internet","iloveyou","1qaz2wsx","baseball","whatever","princess","abcd1234","starwars","trustno1","password1","jennifer","michelle","mercedes","benjamin","11111111","samantha","victoria","alexander","987654321","asdf1234","1234qwer","qwertyuiop","q1w2e3r4","elephant","garfield","chocolate","jonathan","caroline","maverick","midnight","88888888","creative","qwerty123","cocacola","passw0rd","liverpool","blink182","asdfghjkl","danielle","scorpion","veronica","nicholas","asdfasdf","metallica","december","patricia","christian","spiderman","security","slipknot","november","jordan23","qwertyui","butterfly","swordfish","carolina","hardcore","corvette","12341234","remember","qwer1234","leonardo","snickers","williams","angelina","anderson","123123123","pakistan","marlboro","kimberly","00000000","snowball","sebastian","godzilla","hello123","champion","precious","einstein","napoleon","mountain","dolphins","charlotte","fernando","basketball","barcelona","87654321","paradise","motorola","bullshit","brooklyn","stephanie","elizabeth","qwerty12","franklin","american","platinum","icecream","darkness","cristina","colorado","alexandra","steelers","serenity","mitchell","lollipop","marshall","1qazxsw2","12344321","startrek","christine","business","nintendo","12qwaszx","asdfghjk","Password","1q2w3e4r5t","zaq12wsx","scotland","hercules","explorer","manchester","firebird","engineer","virginia","simpsons","angelica","september","isabelle","isabella","changeme","passport","infinity","superstar","courtney","scarface","pavilion","abcdefgh","a1b2c3d4","harrison","spitfire","catherine","birthday","wolverine","guinness","california","logitech","emmanuel","11223344","goldfish","cheyenne","testtest","stargate","microsoft","anything","aaaaaaaa","welcome1","eternity","westside","password123","maryjane","michael1","lawrence","kristina","kawasaki","drowssap","blahblah","babygirl","poohbear","florence","sapphire","hamilton","greenday","qazwsxedc","twilight","swimming","stardust","predator","penelope","michigan","margaret","brittany","shithead","redskins","pussycat","fireball","cherokee","australia","1234abcd","lovelove","thailand","lasvegas","butthead","blizzard","shamrock","bluebird","atlantis","147258369","valentine","magnolia","juventus","diamonds","christopher","warcraft","renegade","mohammed","terminator","shopping","savannah","giovanni","12121212","wildcats","portugal","beautiful","sunflower","santiago","kathleen","enterprise","clifford","christina","55555555","something","rosemary","vacation","hollywood","chandler","99999999","lorraine","children","beatrice","airborne","valentin","moonlight","kamikaze","strawberry","software","22222222","skywalker","salvador","panthers","lacrosse","charlie1","cardinal","bluemoon","0123456789","zeppelin","rockstar","operator","dragonfly","dickhead","anaconda","amsterdam","789456123","77777777","skittles","personal","kingkong","geronimo","christmas","wrestling","robinson","lightning","kingston","hannibal","download","darkstar","undertaker","tinkerbell","sweetpea","softball","panasonic","pa55word","keyboard","darkside","cleopatra","assassin","vladimir","national","matthew1","godfather","brothers","warriors","universe","rush2112","mushroom","bigdaddy","1a2b3c4d","ultimate","peterpan","loverboy","truelove","trombone","madeline","gangster","dingdong","catalina","alejandro","kittycat","aquarius","1111111111","patriots","jamesbond","ihateyou","blessing","airplane","Password1","stingray","hellfire","guardian","flamingo","0987654321","socrates","richmond","electric","thankyou","sterling","munchkin","morpheus","imperial","happiness","goodluck","columbia","campbell","blackjack","999999999","telephone","oblivion","newcastle","freedom1","washington","valentina","valencia","spectrum","jessica1","jeremiah","handsome","goldberg","gabriela","anthony1","a1234567","xxxxxxxx","peekaboo","motherfucker","montreal","katherine","kangaroo","immortal","chocolat","thompson","research","oklahoma","mariposa","idontknow","defender","applepie","squirrel","pineapple","hongkong","dinosaur","babydoll","wolfgang","semperfi","patience","fletcher","drpepper","creation","wordpass","passwort","original","nightmare","martinez","labrador","excalibur","discovery","apple123","sundance","redwings","mypassword","monopoly","margarita","lionking","football1","director","44444444","sylvester","sherlock","marianne","lancelot","jeanette","cannabis","andromeda","werewolf","starcraft","marathon","longhorn","happy123","brucelee","argentina","147852369","wrangler","william1","stranger","scarlett","qweasdzxc","playstation","morrison","february","fantasia","designer","bulldogs","sullivan","saturday","pingpong","kristine","halloween","fuckyou1","fearless","cassandra","bismillah","airforce","theodore","starfish","pass1234","cinnamon","sweetheart","overlord","michaela","meredith","buttercup","abc12345","aardvark","Passw0rd","12345678910","universal","trinidad","thursday","standard","pearljam","anonymous","springer","ragnarok","portland","nathalie","lemonade","lavender","gotohell","gladiator","freckles","crusader","commando","clarence","cadillac","alexandre","123654789","verbatim","umbrella","splinter","register","qwert123","penguins","ncc1701d","estrella","downtown","colombia","chemistry","bollocks","anastasia","741852963","69696969","showtime","revolution","qwerasdf","password2","mongoose","illusion","cooldude","abracadabra","123qweasd","treasure","pinkfloyd","passwords","linkinpark","education","underground","monalisa","justdoit","ericsson","chelsea1","achilles","a1s2d3f4","veronika","test1234","teddybear","sporting","papillon","nevermind","marketing","juliette","gabrielle","fuckyou2","firewall","evolution","cristian","cavalier","canadian","admin123","together","spongebob","pa55w0rd","halflife","formula1","dragonball","thirteen","stonecold","rastaman","mustang1","cucumber","skateboard","sheridan","qqqqqqqq","punisher","lovelife","gretchen","chevelle","chester1","administrator","wireless","volleyball","sandiego","pokemon1","lollypop","gorgeous","chickens","blueberry","blackman","blackbird","atlantic","wildfire","waterloo","singapore","rocknroll","mississippi","james123","homework","highland","eldorado","discover","computer1","alphabet","123456789a","1123581321","zaq1xsw2","webmaster","university","tropical","southpark","question","presario","poiuytrewq","notebook","nebraska","bullseye","valhalla","tomorrow","starlight","richard1","positive","plymouth","patrick1","faithful","dominique","doberman","criminal","crackers","converse","casanova","attitude","66666666","wonderful","scooter1","scoobydoo","rochelle","punkrock","messenger","kentucky","insomnia","hooligan","gertrude","capricorn","blueeyes","blackberry","blablabla","terminal","snowflake","poseidon","paranoid","mastermind","laurence","istanbul","frederic","doomsday","bradford","bonehead","apollo13","alessandro","westwood","supernova","satan666","reynolds","qazwsx123","q1w2e3r4t5","mckenzie","magician","jellybean","innocent","hotstuff","fountain","concrete","capslock","snuggles","professor","megadeth","medicine","lionheart","jackson1","intrepid","highlander","green123","geoffrey","francisco","dynamite","columbus","cinderella","chemical","chargers","username","superman1","sherwood","moonbeam","meowmeow","matthias","josephine","jackson5","honolulu","diamond1","crawford","broadway","backspace","asdasdasd","zzzzzzzz","whocares","watermelon","svetlana","southern","president","pleasure","makaveli","honeybee","francois","chicken1","bookworm","PASSWORD","33333333","woodstock","sunlight","stallion","katerina","jefferson","international","hellokitty","hedgehog","happyday","frederick","davidson","dangerous","cerberus","blackcat","arsenal1","angel123","10101010","training","roadrunner","republic","recovery","maradona","intruder","hermione","hastings","goldstar","fredfred","federico","deftones","commander","chevrolet","blackout","billabong","1234567a","1234554321","yesterday","wolfpack","thunder1","tacobell","sweetness","solution","shanghai","satellite","rootbeer","phillips","monsters","lonewolf","keystone","johannes","grateful","continue","confused","brighton","0000000000","yankees1","triangle","peterson","marianna","mandrake","inuyasha","hardware","freebird","ferguson","dominick","bullfrog","babylon5","13131313","zanzibar","transfer","television","sparkles","shepherd","resident","property","pictures","mischief","macintosh","kristian","kissmyass","hurricane","heineken","hahahaha","eastside","daffodil","charming","billybob","armstrong","adventure","adelaide","underdog","technics","samsung1","qwerty1234","phoenix1","musicman","marjorie","letmein1","jerusalem","information","iloveyou1","hospital","handball","gonzales","darkangel","budapest","brandon1","alliance","adrienne","aberdeen","abc123456","1234512345","wonderland","thuglife","sentinel","richards","rammstein","newyork1","mortimer","marcello","magazine","infantry","hopeless","harrypotter","fandango","deadhead","clarissa","christie","charlene","billyboy","bangbang","absolute","titanium","tiger123","superior","stefanie","spaceman","somebody","sinclair","pppppppp","paintball","mmmmmmmm","military","marijuana","mackenzie","loveless","lighthouse","karolina","jesuschrist","fernanda","felicity","dietcoke","cleveland","brewster","babyblue","ashleigh","1q2w3e4r5t6y","14789632","whiskers","valkyrie","superfly","strength","seventeen","progress","muhammad","maryland","evergreen","daughter","clarinet","chuckles","beethoven","almighty","aaaaaaaaaa","9876543210","1qaz1qaz","waterfall","sneakers","saratoga","qawsedrf","motocross","majestic","kingfish","japanese","graphics","flounder","coltrane","chris123","checkers","barbados","augustus","angelika","12345qwert","washburn","tottenham","survivor","stanford","soulmate","rasputin","pallmall","overkill","meatloaf","lowrider","katarina","ilovegod","heather1","hallo123","giuseppe","eastwood","dominion","destroyer","chiquita",
    "chipmunk","castillo","berkeley","alexandria","1122334455","1029384756","thinking","tarheels","seminole","radiohead","priscilla","pornstar","platypus","nirvana1","mephisto","lancaster","knowledge","johnjohn","gameover","fuckface","david123","darklord","cutiepie","carnival","candyman","blowfish","ssssssss","snowboard","sandwich","sailboat","mandarin","knuckles","jasmine1","hardrock","daredevil","boomboom","benedict","babyface","albatros","963852741","valentino","sprinter","salvation","rolltide","rodriguez","r2d2c3po","password12","mustangs","moonshine","missouri","meridian","meatball","malaysia","killbill","illinois","gonzalez","georgina","gargoyle","evangelion","disaster","complete","claymore","cheesecake","chainsaw","bluebell","98765432","wishbone","warhammer","viewsonic","vampires","thunderbird","smashing","rhiannon","rachelle","playtime","offspring","marcella","lonestar","heritage","hayabusa","freestyle","forsaken","ferrari1","challenger","backdoor","asshole1","147896325","11235813","yosemite","yogibear","talisman","taekwondo","syracuse","supersonic","randolph","raistlin","preacher","millions","metallic","madison1","losangeles","hernandez","dontknow","coolcool","charisma","wednesday","starwars1","sinister","passpass","mohammad","mcdonald","goldeneye","frontier","francesca","flipflop","fisherman","eggplant","dannyboy","daniella","chrysler","cameron1","cambridge","buckshot","arkansas","archangel","america1","12345679","romantic","robotics","redalert","megatron","mamapapa","hyperion","hamburger","gabriel1","fuckfuck","friendship","friendly","florida1","dreaming","doghouse","disturbed","christin","bubblegum","brigitte","addicted","underworld","shadow12","porkchop","negative","mistress","melissa1","jermaine","james007","gabriella","francine","delphine","crystal1","computers","chestnut","baseball1","auckland","321654987","wanderer","vancouver","tomahawk","thanatos","syncmaster","snoopdog","roderick","princesa","pentagon","nathaniel","money123","millenium","mechanic","liverpool1","francesco","esmeralda","creature","cornwall","chadwick","carpediem","calendar","abdullah","vendetta","supervisor","stephane","revolver","railroad","qwerty12345","p4ssw0rd","minnesota","mariners","iloveyou2","holyshit","elisabeth","database","bumblebee","bobafett","bernardo","amethyst","albatross","advanced","whistler","wellington","slamdunk","sheffield","scrabble","roadkill","realmadrid","rainbows","polopolo","obsidian","northern","learning","independent","impossible","elements","electron","customer","budweiser","brisbane","baritone","armageddon","amarillo","alexandr","aerosmith","12301230","windmill","vanhalen","surprise","starfire","speakers","ncc1701e","lifetime","kittykat","fredrick","fidelity","fabulous","everyday","coolness","concorde","catwoman","casablanca","blackhawk","babybaby","vodafone","traveler","southside","rainbow1","princess1","potatoes","pipeline","philippe","pathfinder","monterey","lipstick","lakeside","internet1","insanity","fishbone","chihuahua","bordeaux","biohazard","21122112","windsurf","velocity","vagabond","topsecret","reloaded","raindrop","prudence","professional","pharmacy","peaceful","multimedia","montgomery","marseille","marietta","letmein2","ladybird","internal","gigabyte","fourteen","dolphin1","chambers","bunghole","buckeyes","bluefish","apocalypse","aphrodite","4815162342","23232323","12369874","111222333","zerocool","wrestler","tortoise","sysadmin","sunshine1","starship","qwerty123456","qwerty11","primrose","politics","paranoia","pancakes","overload","opensesame","nevermore","melbourne","matthews","marriage","magdalena","macaroni","jonathon","jacqueline","jackjack","infinite","heinrich","graduate","goodness","godspeed","feedback","cornelia","corleone","choochoo","challenge","chairman","butthole","buddy123","barracuda","azsxdcfv","accounting","sleeping","remington","quicksilver","pringles","power123","paradigm","nickolas","navigator","nautilus","milkshake","master123","feathers","facebook","dragon12","brittney","aviation","avalanche","19841984","123qweasdzxc","10203040","wildwood","thrasher","speedway","songbird","sickness","shannon1","screamer","samantha1","riverside","princeton","monster1","mauricio","manhattan","love1234","jennifer1","indonesia","devil666","bugsbunny","budlight","ambrosia","adrianna","zxcvbnm1","windows1","toulouse","tazmania","spaghetti","slapshot","ministry","mathilde","lighting","helsinki","girlfriend","gateway1","fussball","frederik","flexible","festival","destiny1","daydream","coventry","constant","connection","charles1","angeline","a123456789","111111111","woodland","skinhead","signature","sandrine","rockford","merchant","greatest","everlast","espresso","elizabet","dragon123","dddddddd","community","chouchou","charlton","champagne","carlitos","blueblue","awesome1","aspirine","12345abc","technology","stronger","starbuck","skeleton","scissors","reginald","redeemer","polarbear","normandy","luckydog","laserjet","just4fun","greenbay","graffiti","fantastic","doughboy","dortmund","building","bbbbbbbb","annabelle","annabell","alchemist","zimbabwe","wisconsin","winchester","tunafish","thisisit","stafford","spalding","sometimes","solitude","robotech","rainbow6","qazwsx12","pooppoop","minister","leonidas","kirkland","integral","incognito","ilovesex","ignatius","heavenly","gggggggg","ferdinand","exchange","bulldog1","blackdog","bearbear","123454321","winfield","westlife","thriller","summertime","spartans","sausages","salvatore","salamander","printing","palmtree","opendoor","mosquito","milkyway","mcdonalds","laughter","klondike","kingsley","jesus123","invisible","humphrey","hillside","hattrick","hammerhead","function","forgotten","fighting","excellent","delaware","darthvader","costello","catalyst","cardinals","bobmarley","babylove","assholes","andersen","alexande","19891989","1234asdf","whiplash","tiffany1","solutions","smallville","slimshady","sammy123","rockwell","robinhood","reddevil","maxwell1","madeleine","gordon24","glendale","giovanna","foxylady","fortress","favorite","doughnut","comanche","cheshire","cherries","catarina","bertrand","barefoot","arabella","alligator","1qaz2wsx3edc","vanguard","stuttgart","stephen1","rhapsody","reckless","pumpkin1","powerful","painting","nocturne","nickname","mynameis","mikemike","llllllll","leighton","kkkkkkkk","kingfisher","johnston","holidays","henderson","handyman","fuckoff1","front242","flamenco","escalade","division","covenant","churchill","cannibal","badminton","annmarie","alexander1","alcatraz","11112222","wwwwwwww","wildcard","whitesox","vincent1","thornton","temporary","survival","supernatural","sprocket","somerset","skorpion","services","saxophone","sacrifice","restless","pumpkins","operation","nosferatu","newpassword","monkey123","michelle1","meathead","management","lucky123","licorice","language","jackass1","infiniti","generation","gamecube","flanders","edinburgh","disciple","diplomat","crescent","counterstrike","catholic","capoeira","calculator","browning","biscuits","alexalex","P@ssw0rd","Jennifer","19861986","123456abc","winston1","violator","tangerine","super123","straight","sorcerer","sidekick","shredder","schubert","prestige","peter123","nonsense","mulligan","moneyman","matchbox","marauder","longhair","lisalisa","kayleigh","islander","grasshopper","geraldine","genesis1","gardenia","gabriele","everything","edmonton","downhill","digital1","cromwell","chowchow","carebear","bettyboop","vanessa1","terrapin","tennessee","stockton","spartacus","smoothie","seahawks","revelation","rebecca1","rangers1","qweqweqwe","puppydog","marigold","gregorio","goldfinger","gangbang","dutchess","daylight","constantine","clueless","calamity","beefcake","aquarium","anathema","ambition","a12345678","19821982","wildlife","undercover","snowbird","schneider","qwert12345","qwerqwer","prospect","porsche911","pendragon","natalie1","lockdown","lkjhgfdsa","jellyfish","italiano","irishman","infamous","hydrogen","hartford","goodyear","generals","garrison","foxhound","entrance","eighteen","dimension","diamante","daedalus","cocktail","chameleon","caligula","borabora","behemoth","balloons","bachelor","123698745","waterman","teenager","spanking","soccer10","sergeant","seashell","seahorse","scarecrow","riffraff","possible","pittsburgh","pinnacle","nostromo","maximilian","latitude","kevin123","kamasutra","invasion","hibiscus","hallmark","firestorm","fernandez","envision","desperado","charcoal","character","blue1234","antelope","alejandra","aircraft","123456aa","123456123","viktoria","unlimited","transport","stripper","stefania","snowwhite","smirnoff","seraphim","sebastien","ronaldo7","reporter","raiders1","painkiller","nineteen","monolith","moneymaker","memories","memorial","massacre","lamborghini","honduras","goofball","fullmoon","forever1","engineering","elefante","dragonballz","doorknob","dipstick","commerce","carousel","callisto","brilliant","berenice","barbarian","asdfzxcv","alex1234","Welcome1","1qa2ws3ed","19871987","12345678a","wormwood","volkswagen","starstar","sexygirl","sephiroth","schumacher","rosewood","rochester","roadster","rapunzel","prisoner","prescott","pizza123","phillies","phantom1","perfect1","pasadena","optimist","monkeyboy","metropolis","master12","kimberley","junkmail","inspiron","hhhhhhhh","hellohello","griffith","greenwood","golfball","forester","euphoria","england1","death666","cornelius","constance","conquest","clitoris","cartoons","buckaroo","bluejays","Alexander","volunteer","violence","testpass","terrence","temporal","teamwork","spencer1","silverado","shipping","serendipity","roosters","prophecy","popcorn1","playmate","panorama","p0o9i8u7","marcopolo","landmark","johnson1","iverson3","instinct","infected","illuminati","honeydew","foundation","forbidden","esperanza","document","deadline","crocodile","cowboys1","climbing","bubbles1","bluestar","birmingham","bathroom","baltimore","anamaria","25802580","24682468","whiteboy","trinitron","titleist","tiberius","testing123","superhero","sidewinder","rosemarie","retarded","primavera","peppermint",
    "palomino","outsider","oooooooo","musician","michelin","juggernaut","ironmaiden","hyacinth","gatorade","fuzzball","everyone","dictionary","development","delirium","daisy123","critical","cordelia","collection","capitals","caliente","bobdylan","blackrose","birdhouse","asparagus","Michelle","1a2s3d4f","19781978","voltaire","thedoors","submarine","stonewall","special1","southpaw","soccer12","sanctuary","ruthless","reaction","qazwsxed","prometheus","portable","password11","passcode","official","neverland","mindless","masamune","legendary","lalalala","incredible","holloway","heartless","hairball","genevieve","fireworks","dirtbike","dilligaf","crossfire","clippers","chicago1","caldwell","bernadette","agent007","19831983","19801980","19751975","waterpolo","warrior1","vertical","timeless","thegreat","superuser","spelling","slippery","rrrrrrrr","ricochet","redemption","raspberry","protocol","producer","penguin1","patterson","p455w0rd","olivetti","oliveira","metalica","mannheim","mandingo","magellan","machines","lovebird","jonathan1","jason123","inflames","important","helloworld","headache","godbless","gemstone","ffffffff","cyclones","cristiano","colonial","claudius","bulgaria","brunette","bradshaw","bastards","basement","azertyuiop","applesauce","angelique","acapulco","25252525","123789456","123456987","12312312","zachary1","yingyang","workshop","trueblue","transformers","tarantula","sycamore","sunderland","stigmata","stargazer","sabrina1","riccardo","qazxswedc","playboy1","password01","override","nighthawk","music123","motdepasse","mortgage","mickeymouse","meandyou","macdaddy","leicester","knockers","kisskiss","jjjjjjjj","hysteria","forgiven","evanescence","distance","destruction","cosworth","coconuts","carlisle","breakfast","asdfjkl;","antivirus","31415926","21212121","123321123","yokohama","unforgiven","tommy123","surrender","sheepdog","seinfeld","sabotage","ronaldinho","reddragon","pressure","pinetree","pavement","oriental","offshore","newzealand","netscape","michaels","mash4077","mallorca","madagascar","junkyard","johncena","jakejake","invincible","hawthorn","hawaiian","greyhound","frenchie","fishing1","fastball","deathrow","carpenter","calimero","breakout","black123","bismarck","alkaline","adrenalin","123qwerty","zxcv1234","tryagain","thatcher","stampede","shakespeare","scheisse","sayonara","santacruz","pokerface","passions","notorious","nothing1","necromancer","nameless","mysterio","monkey12","mitsubishi","millwall","millennium","megabyte","mccarthy","magister","madhouse","liverpoo","leviathan","laetitia","jennings","holstein","hellraiser","freefall","flawless","emergency","ebenezer","divinity","delpiero","chewbacca","chastity","charlott","carlotta","buchanan","bradley1","battlefield","aventura","asdffdsa","19741974","zildjian","welcome123","wargames","vvvvvvvv","unicorns","timberland","tenerife","tasmania","symphony","splendid","sonyvaio","snapshot","saunders","sarajevo","reverend","prototype","polaroid","perfecto","nokia123","natasha1","mystical","melanie1","material","maddison","landlord","juvenile","goodwill","goldwing","gilberto","gandalf1","fuckthis","flapjack","flamengo","finnegan","fabienne","erection","clemente","christophe","caterpillar","caterina","capetown","austin316","antonio1","angelito","accounts","abstract","19911991","19761976","01234567","zxcvbnm123","vincenzo","townsend","technical","soccer11","smithers","shooting","shitshit","shadow123","senators","sacramento","redbaron","programmer","percival","painless","northstar","newspaper","myfamily","mongolia","miroslav","macarena","lumberjack","landrover","lakewood","killer12","incoming","immanuel","hometown","homeless","hillbilly","hellothere","guillaume","goodnight","giordano","genocide","enforcer","dreamcast","dispatch","developer","copenhagen","codename","clockwork","cccccccc","caramelo","callaway","calculus","brian123","blessed1","benjamin1","bartender","attorney","asteroid","angeleyes","academia","a1b2c3d4e5","12131415","yamahar1","warehouse","tricolor","terrance","summer99","stirling","stamford","stairway","specialist","soldiers","shitface","scorpio1","rotterdam","principe","pizzahut","pepperoni","patricio","passwerd","mulberry","luscious","lifeline","legoland","kickflip","kennwort","kathrine","josefina","johnathan","jesus777","hollister","hellsing","excelsior","drummond","disneyland","deutschland","delldell","cupcakes","claudine","ciaociao","christia","checkmate","centurion","cashmere","carthage","bookmark","bartlett","armagedon","animation","alphonse","alessandra","Benjamin","51505150","192837465","xxxxxxxxxx","woodside","warcraft3","vengeance","vaseline","trinity1","toxicity","tommyboy","ticktock","teachers","strategy","stephens","snowdrop","smeghead","shutdown","sexysexy","princesse","pretender","popsicle","philadelphia","petersen","password3","oscar123","moonstone","masterkey","maryanne","magicman","kingking","identity","icehouse","hannover","glorious","gathering","forgetit","fishtank","finalfantasy","fernandes","epiphone","elevator","elegance","drumline","devilman","delivery","chrissie","carnaval","caffeine","bukowski","brownies","bearcats","architect","akatsuki","987456321","19941994","woofwoof","virginie","untitled","tttttttt","timothy1","stickman","starlite","southwest","smarties","sailormoon","penthouse","peanutbutter","oxymoron","oleander","nightfall","newjersey","ncc1701a","muhammed","morphine","mobydick","meltdown","medieval","mahogany","magic123","longshot","lockheed","livewire","lakeland","kenworth","interpol","integrity","hunter12","hibernia","helpdesk","guatemala","godofwar","fishhead","everybody","ethernet","elemental","duracell","delicious","daniel123","crystals","confidence","colossus","callofduty","besiktas","belladonna","backlash","airforce1","academic","abnormal","5555555555","19901990","123qwe123","violetta","vineyard","terrible","suburban","stocking","starbucks","springfield","snuffles","sideways","sensation","schwartz","salasana","runescape","rosalind","radiation","q1w2e3r4t5y6","purchase","protection","practice","poiuytre","piramide","nashville","montrose","molly123","maximus1","mammamia","lunchbox","lonesome","limerick","liberty1","killer123","imagination","ignition","homebrew","helicopter","harry123","guadalupe","greenman","godsmack","firefire","electronic","economics","daniel12","cricket1","contract","conflict","comeback","coldplay","cheeseburger","braveheart","believer","beaumont","bangladesh","arrowhead","angelita","alternative","23456789","135792468","woodward","wolverin","whatever1","wellness","timberlake","terrorist","temptation","swingers","supergirl","solstice","scratchy","roosevelt","rockport","redlight","puppy123","perfection","paulette","password99","panther1","overtime","nopassword","nazareth","mudvayne","movement","miracles","mike1234","maserati","marihuana","marbella","lifestyle","kiwikiwi","jurassic","infernal","hereford","goodtime","goodlife","goodgirl","gamecock","galadriel","gabriell","friends1","firefighter","ferreira","fenerbahce","ethiopia","dionysus","different","deadpool","crossroads","christos","chauncey","castaway","carefree","burnside","borussia","boomerang","bohemian","blackice","blackhole","bigmouth","baptiste","augustin","asdfg123","arlington","ambassador","alistair","agamemnon","advocate","adgjmptw","acoustic","Princess","7894561230","19811981","11221122","zimmerman","youandme","yorkshire","wallpaper","vinicius","veronique","vauxhall","understand","tyler123","terminus","surround","suckmydick","stronghold","soccer13","slipknot1","sexylady","sessions","scirocco","schiller","schedule","rosebud1","regional","radiance","pioneers","phantasy","peaches1","p@ssw0rd","obsession","neutrino","mountains","marmalade","kendrick","jamesbond007","hogwarts","heinlein","guitarra","gillette","germania","fruitcake","flowers1","fighters","fastback","fabrizio","exercise","envelope","element1","eeeeeeee","doraemon","diabetes","destination","davenport","damascus","coronado","chevalier","cashflow","cardigan","boyfriend","blueprint","blackboy","bitchass","backpack","babycakes","arschloch","aquamarine","anakonda","Victoria","911turbo","19851985","19721972","1234567899","worldwide","water123","viscount","violette","venezuela","undertow","traveller","transformer","tombstone","teacher1","surfboard","success1","stratocaster","stephani","stainless","scorpions","redstone","premiere","planning","peacemaker","paramore","packers1","numberone","nitrogen","natascha","moonwalk","maurizio","marzipan","mandolin","mamamama","maintain","macgyver","ludacris","loredana","lexington","landscape","killkill","justice1","jailbird","ilovemyself","google123","goodnews","gatekeeper","freshman","frankfurt","frankenstein","firestar","eleonora","dreamland","dragon11","domenico","discreet","detective","crossbow","creative1","choppers","betrayed","bernhard","basilisk","asdqwe123","asdasd123","armadillo","antigone","alterego","alhambra","aerobics","advantage","Superman","20012001","1million","yyyyyyyy","yellowstone","woodruff","vampire1","tequiero","sunnyboy","specialk","sorrento","reliance","q2w3e4r5","proverbs","policeman","playgirl","pentium4","pedigree","partners","overdrive","orange12","observer","nnnnnnnn","nicholas1","newworld","moriarty","minotaur","manunited","location","leavemealone","knockout","knickers","kassandra","jeffrey1","hellyeah","greentea","goodgood","germany1","gasoline","flashman","firestarter","fatality","emiliano","ellipsis","disorder","deadlock","davidoff","couscous","construction","congress","cleaning","clarkson","christoph","cheerleader","charlie2","ceramics","casandra","cambodia","blackstar","bigmoney","ballerina","backbone","alexandru","74108520","24681012","24242424","1password","19881988","123456123456","whatwhat","westcoast","watching","underwear","tomatoes","tiramisu","tiberian","thurston","spinning","slippers","simon123","response","reindeer","qwertyuio","prosperity","porsche1","password1234","panchito","nottingham","mythology","montana1","mayfield","marquise","manifest","magnetic","lovelace","letmein123",
    "lesbians","joystick","inspector","industry","ilovejesus","gulliver","ganymede","galactic","furniture","flashback","esoteric","dropdead","drinking","devildog","copeland","christop","christian1","cheerios","chatting","chantelle","changeit","cerulean","cabernet","blackheart","bionicle","baltazar","amoremio","alpha123","alleycat","accident","19771977","123mudar","trickster","tingting","thething","testing1","tallulah","symmetry","summer69","stonehenge","smartass","shortcake","shadow11","salesman","rushmore","resource","pregnant","pleasant","playground","plankton","pendulum","paterson","password8","partizan","olympics","northwest","networks","nederland","mystique","metallica1","mckinley","mcgregor","maxpower","mathematics","longhorns","livelife","lafayette","kokakola","kleopatra","katherin","julianna","jeannine","horseman","homeland","holiday1","hennessy","guesswho","greywolf","gilligan","gallardo","freewill","francisca","francis1","fordf150","fleetwood","fantomas","eightball","dutchman","drummer1","dementia","cellphone","breakdown","blessings","berliner","antonella","andrew123","aleksandra","adrenaline","abrakadabra","20002000","19951995","woodwork","winifred","welcome2","waterboy","troopers","theodora","sometime","smackdown","sagittarius","russell1","rocketman","roadking","rifleman","raymond1","qwerty13","priyanka","private1","pizzaman","phantasm","pathetic","parliament","oldschool","nicotine","nefertiti","motherlode","mollydog","minstrel","minicooper","milwaukee","millionaire","midnight1","matthieu","maria123","lebron23","lakers24","kitty123","kindness","insurance","independence","hatfield","gymnastics","getmoney","general1","freelance","forsythe","fontaine","feelgood","experience","evidence","erickson","enter123","energizer","downfall","deadwood","dandelion","crazyman","corporate","commandos","citation","chinchilla","champions","calliope","broccoli","bleeding","berserker","bergkamp","backstreet","asmodeus","artistic","antilles","anteater","anhyeuem","aaaa1111","Sunshine","Jonathan","321321321","19731973","19691969","000000000","wrinkles","trumpet1","triplets","telecaster","sunnyday","summer12","students","stockholm","start123","starshine","sopranos","siberian","shetland","sheppard","scrapper","schooner","rebellion","pershing","password7","parasite","pantera1","palmetto","overture","odysseus","notredame","noisette","narayana","nakamura","mushrooms","moderator","metalgear","mediator","mcintosh","mazda626","mayflower","marykate","manpower","malamute","louisiana","kryptonite","kathmandu","justin12","jeronimo","jeremias","jamaican","imperium","hurricanes","humberto","hotmail1","hoosiers","goldmine","futurama","elisabet","earthquake","dumpling","dragster","dragon13","dominica","dominate","dictator","desperate","cookbook","confusion","concerto","christel","cashmoney","blacksmith","beholder","babushka","autobahn","attention","atmosphere","anywhere","aftermath","acidburn","abhishek","789654123","z1x2c3v4","whiteout","typewriter","topolino","thousand","thorsten","thematrix","symantec","stanley1","splatter","spiderman1","sonysony","slaughter","sensitive","schaefer","reddwarf","providence","position","popopopo","pikapika","piercing","performance","pasquale","paramedic","pakistani","neighbor","motorcycle","mireille","lovesick","loverman","london12","lockwood","lifeguard","kowalski","kerberos","kellyann","jimmy123","jayhawks","innuendo","incorrect","ilovemom","iiiiiiii","hummingbird","houston1","horrible","himalaya","highlife","hetfield","heartbeat","guitarist","graphite","godisgood","ghostrider","funnyman","f00tball","epiphany","elvis123","discount","danny123","danielle1","copyright","consumer","concordia","complicated","clementine","chouette","chinchin","chinatown","chinaman","chesterfield","cervantes","celestial","calderon","bullhead","brussels","broadband","brasilia","bobby123","bellevue","bagpipes","aurelius","aristotle","altitude","aloysius","alabama1","affinity","abcdefg1","Password123","20102010","09876543","zxasqw12","winnipeg","ultraman","treefrog","tigercat","taratara","tactical","system32","swastika","skipper1","searcher","reserved","redbeard","realtime","qwert1234","qwe123qwe","pyramids","provider","projects","production","poontang","pinecone","pericles","pennywise","paradiso","parachute","parabola","palestine","overflow","motorbike","mechanical","mazdarx7","mavericks","marybeth","marriott","madalena","loophole","lonsdale","lingerie","libertad","ledzeppelin","lavalamp","joselito","joker123","jerrylee","jamboree","interest","imissyou","hugoboss","holahola","heythere","hehehehe","hangover","guerrero","greatone","gianluca","gardener","gangsta1","exorcist","elizabeth1","dressage","dominic1","dominator","domination","dodgeram","cummings","commodore","christen","callahan","calcutta","burberry","bulletproof","bombshell","blackburn","betrayal","atkinson","athletic","arachnid","amaranth","algernon","alastair","absinthe","01020304","zoomzoom","wonderboy","whatthefuck","watchman","vanilla1","trouble1","transform","trampoline","tortilla","thunderbolt","superduper","squadron","smile123","skylight","sanfrancisco","salamandra","ricardo1","resistance","reliable","recorder","qwertyqwerty","provence","porsche9","piedmont","pentagram","patches1","password9","overdose","nightman","nightingale","mymother","monument","medicina","madonna1","longtime","lolololo","lokiloki","littleman","laughing","kerrigan","jeopardy","inspiration","ibelieve","houghton","horsemen","hologram","hideaway","hawaii50","happydays","handicap","hamsters","guillermo","georgia1","freddie1","forklift","finished","dorothea","devotion","deathstar","darkknight","conchita","cocacola1","classics","chopper1","buffalo1","bubba123","bridgette","blingbling","bigballs","barnyard","baphomet","badlands","asterisk","arcangel","antoinette","annemarie","Christian","20022002","19971997","1234567891","whoknows","victoria1","trousers","treehouse","tranquil","toriamos","temppass","teardrop","superboy","srinivas","snowman1","shortcut","shockwave","shocking","senha123","scranton","sandoval","roseanne","red12345","prospero","products","paperclip","papamama","outdoors","nightwish","nemesis1","nagasaki","mousepad","morrissey","monkeyman","modeling","microlab","maranatha","makeitso","maelstrom","limpbizkit","lightbulb","lalakers","katharina","kakaroto","jeannette","investor","insecure","humanoid","hondacivic","holiness","helpless","hallelujah","greenhouse","germaine","gallagher","freefree","francais","firestone","firebolt","filipino","federica","falstaff","eleven11","electronics","economist","dominant","diabolic","deadbeat","crockett","crazycat","composer","coleslaw","cincinnati","cascades","bretagne","breaking","bluenose","bluegrass","bisexual","billions","billbill","bigbrother","beckham7","avengers","athletics","assembly","asasasas","allstars","alakazam","activate","abcde12345","Pa55word","Computer","369258147","1q2w3e4r5","123456qwerty","zerozero","windowsxp","wachtwoord","vigilant","verygood","trustnoone","truffles","toothpaste","tigerman","thankgod","telefono","sweetwater","summoner","suicidal","strummer","stiletto","squeaker","sixtynine","sithlord","siegfried","showcase","serenade","sepultura","secret123","rotation","rockhard","quintana","pepsicola","passenger","pacifica","omsairam","nightshade","newhouse","nacional","muenchen","motorhead","morrigan","montecarlo","michael2","memememe","maximize","marino13","marciano","macdonald","loveable","lakeview","konstantin","kenneth1","ilikepie","hyderabad","historia","highschool","hiawatha","hermitage","goodtimes","freeport","flathead","faulkner","endymion","emirates","dreamers","dragon69","district","dietrich","cranberry","cockroach","clemence","claudia1","classified","chocolate1","cellular","catherin","carmella","butterfly1","burgundy","brother1","blooming","blitzkrieg","bladerunner","bigboobs","beachbum","barbara1","backyard","backward","babybear","argonaut","appleton","aguilera","abundance","Nicholas","Michael1","9999999999","1qazzaq1","13243546","12qw34er","123456ab","zaragoza","woodcock","wisteria","westlake","victoire","untouchable","trapdoor","tigereye","thetruth","testicle","superbowl","student1","sprinkle","snakebite","silencer","secretary","scottish","sanderson","sanandreas","robertson","richelle","richardson","religion","rastafari","quiksilver","queenbee","psychology","playhouse","physical","pensacola","pedersen","password0","paperboy","pandemonium","nikolaus","murderer","montague","mockingbird","milagros","mercutio","mercurio","mcknight","maxpayne","mandragora","manager1","mamacita","madhatter","lucretia","love4ever","lol12345","laura123","kusanagi","knoxville","katmandu","julianne","joseluis","jiujitsu","jeanpaul","infrared","industrial","humanity","hotwheels","honeypot","honeybun","herkules","heartbreaker","hawkeyes","gregory1","gilgamesh","geometry","friedman","freiheit","firework","federation","executive","exclusive","excellence","emotional","elbereth","dragon99","dollface","devilish","democrat","darkmoon","crackpot","costarica","costanza","consuelo","clarisse","citibank","cingular","chrystal","channing","carvalho","brownie1","bluebear","billyjoe","benedikt","beaufort","batman12","barnabas","baracuda","augustine","armitage","alcapone","afterlife","adrianne","a1a2a3a4","Internet","Football","yourself","yorktown","yeahyeah","wildflower","valdemar","unlocked","unleashed","twinkles","trujillo","torrents","tonyhawk","tanzania","takedown","takamine","supercool","subwoofer","stitches","standing","stalingrad","srilanka","sparhawk","slowpoke","shoelace","service1","senorita","seashore","sandstorm","roulette","rocky123","radiator","problems","powerhouse","postmaster","platform","parallax","nepenthe","moonmoon","lovehate","livingston","lifesucks","labyrinth","komputer","jackhammer","intrigue","interface","interact","honeymoon","grapefruit","government","geography","galloway","fullback","fuckhead","fairview","divorced","disabled","defiance","deeznutz","daniel01","cookies1","communication","cocksucker","cheating","buckwheat",
    "boarding","blackdragon","baseline","bandicoot","baldrick","apollo11","annamaria","ambulance","aluminum","abercrombie","19931993","19791979","woodwind","woodpecker","woodbury","watchdog","vikings1","tribunal","toreador","tigerwoods","thinkpad","thebeach","test12345","terrific","teaching","supermario","successful","stringer","sovereign","souvenir","sombrero","sk8board","shuriken","shotokan","shinichi","scooters","schroeder","schnitzel","rosalinda","regiment","rainfall","qwerty78","qweasd123","puertorico","pistache","pianoman","paddington","overseas","orthodox","nietzsche","monorail","minemine","milhouse","mermaids","maverick1","margarida","mansfield","madrigal","london22","krakatoa","junction","intranet","imperator","hunter123","humility","harmless","grace123","giuliana","gauntlet","fugitive","fuckyou123","flatland","feelings","fabregas","entertainment","emanuele","election","dumpster","douglas1","cruzeiro","cracking","control1","cheaters","centrino","captain1","canberra","botswana","blockbuster","blahblahblah","blackfire","blackbelt","bestfriend","atreides","asuncion","astronomy","astroboy","aqualung","amnesiac","adorable","3edc4rfv","1z2x3c4v","19921992","14141414","12211221","yankees2","worldcup","wholesale","vittorio","underwood","underwater","touchdown","theworld","thebeast","thaddeus","telemark","sylvania","surveyor","suitcase","stroller","stripped","stratford","stallone","speedster","smoke420","septembe","sandberg","rousseau","revenant","protector","protected","pepsi123","pembroke","password4","password13","parkside","outbreak","obsolete","nutshell","nounours","nonenone","multisync","momentum","microwave","michele1","marguerite","maldives","magdalen","longbeach","lockhart","krokodil","kensington","humboldt","homebase","headshot","headless","hazelnut","gremlins","frankie1","frank123","fireman1","fireblade","external","entering","electrical","dulcinea","dropkick","draconis","dont4get","domestic","daydreamer","darkwing","corporal","cocorico","chimaera","cheyanne","celebrate","caballero","breakers","brainstorm","bluesman","blackpool","bethesda","basketba","antichrist","andyandy","allison1","abcdefghi","Garfield","Abcd1234","yoyoyoyo","yeahbaby","wetpussy","vergessen","variable","unicorn1","trillium","torrance","tikitiki","thumper1","thesaint","theforce","teiubesc","sweet123","succubus","stockman","steve123","speeding","solitaire","sokrates","slingshot","skateboarding","silverfox","showboat","sequence","rottweiler","rincewind","rainmaker","qwerty99","postcard","polkadot","photoshop","persimmon","pandabear","orlando1","nutrition","nicolas1","nicknick","naughty1","mysterious","marielle","maneater","lionlion","leningrad","leapfrog","kristopher","kirkwood","kilkenny","jordan12","jediknight","jabberwocky","intercom","informix","hounddog","homicide","herschel","henrietta","hatteras","harakiri","halfmoon","gunslinger","fivestar","firewood","expedition","executor","elcamino","egyptian","eclipse1","duckling","drumming","drifting","daisydog","coolgirl","contrast","collector","choclate","chilling","channels","catapult","careless","californ","brunswick","brendan1","braindead","bluedragon","bloodline","beverley","atalanta","astonvilla","ashley12","asdfghjkl1","arizona1","antihero","andrew12","allright","ab123456","43214321","2222222222","18436572","123456654321","woodlands","windows7","wilkinson","wellcome","waldemar","valerian","tristan1","tornado1","thunders","thomas123","testament","tennyson","tarragon","tapestry","tajmahal","sunny123","struggle","starling","starchild","sobriety","snowfall","snickers1","skyline1","shirley1","shalimar","settings","sebastian1","schnecke","satriani","sasha123","sailfish","roserose","reference","qwerty22","qqqqqqqqqq","prashant","powerman","powerade","playstation2","plastics","pinkpink","parallel","papercut","p4ssword","navyseal","monopoli","mnemonic","millenia","mercenary","membrane","manitoba","lineage2","limelight","leopards","kurdistan","karoline","johnpaul","interior","interesting","insomniac","homepage","hello1234","heavymetal","headhunter","harvester","greeting","golfgolf","glassman","gladstone","galatasaray","friction","filomena","ethereal","emotions","dudedude","douglass","dominika","desperados","demetrio","demented","decision","cuthbert","compound","comatose","civilwar","charleston","castello","cachorro","bulletin","brandnew","bluegill","bloodhound","beautiful1","baywatch","bastardo","bagheera","annalisa","allstate","alfaromeo","aldebaran","alberto1","Samantha","Elizabeth","78945612","01010101","yellow12","wolverines","wolfhound","wildbill","whittier","vittoria","virgilio","vegetable","unbreakable","trusting","troubles","tonytony","thebest1","terriers","template","telefoon","talented","superpower","supermen","sugarplum","starting","spartan117","snowball1","sixpence","simplicity","sidewalk","shoshana","sasquatch","rattlesnake","rainbow7","rafferty","qwerty77","qwerty00","promotion","pokemon123","pinocchio","philosophy","philippines","pheasant","pentium3","patrizia","overlook","overhead","operations","okokokok","nwo4life","novembre","nostradamus","newlife1","newdelhi","myspace1","myfriend","munchies","mountaindew","moneybag","molecule","mercury1","melville","mcintyre","mattress","marshmallow","maritime","mariachi","makemoney","loveyou2","lovesong","lolalola","lindsey1","lifeboat","katie123","kasandra","kalamazoo","jupiter1","julia123","jordan123","jackrabbit","intelligent","innocence","india123","iamthebest","henry123","henrique","hardball","handbook","hacienda","guilherme","grenoble","goodmorning","giuliano","frostbite","freehand","fragment","foreskin","explosion","experiment","ensemble","eclectic","dogfight","dodgers1","diogenes","dillweed","dickinson","demon666","demetrius","daybreak","dagobert","culinary","crossing","controls","consulting","cobblers","chatterbox","charlie123","charissa","celebrity","buster12","bungalow","broadcast","brianna1","bodyguard","bella123","ballroom","andre123","analysis","amber123","afghanistan","addiction","aa123456","2wsx3edc","2bornot2b","12131213","zxcasdqwe","witchcraft","wertwert","warcraft1","vivienne","vermilion","ultrasound","tuppence","tropicana","trafford","teddy123","summer123","streamer","starburst","star1234","ssssssssss","spotlight","specialized","sparrows","solomon1","sideshow","sherbert","seminoles","sebastia","scribble","sarasota","sarasara","sarah123","sanguine","sandy123","samsung123","robert12","reflection","redhorse","rational","radioman","qwerty01","progressive","poophead","plutonium","phantoms","password00","paperino","organize","optiplex","october1","neverdie","nantucket","monsieur","monkfish","mauritius","master01","marymary","marvelous","manifesto","macedonia","lucas123","logistic","leprechaun","lemmings","langston","killer11","jack1234","ireland1","innovation","house123","hihihihi","hellhole","hardwood","generator","funhouse","fullhouse","flowerpower","fiorella","farewell","fantasma","faithless","failsafe","explicit","esposito","enchanted","duckduck","drilling","dragon10","doodlebug","dickweed","crunchie","crawfish","condition","chessman","chanelle","chamonix","celebration","candy123","brotherhood","brainiac","bluewater","birdland","binladen","billings","bareback","bacteria","authority","astronaut","asdfqwer","asd12345","arpeggio","appleseed","anthony2","animator","amazonas","alpacino","adelaida","adamadam","aaron123","Einstein","90909090","1234zxcv","yamamoto","wormhole","windows98","whiteman","westgate","watchmen","vergeten","veracruz","vanquish","uuuuuuuu","undefined","trucking","trooper1","tormentor","timelord","timberwolf","strangle","stoneman","starless","spiritual","spagetti","sorensen","somethin","snowhite","slovakia","skydiver","silvester","silicone","silencio","shevchenko","selector","scramble","scott123","salinger","rendezvous","reminder","redheads","qwerty321","propaganda","presidente","pocahontas","photography","phaedrus","permanent","paulchen","password5","passion1","paraguay","panda123","palacios","osbourne","orange123","onepiece","mutation","murcielago","murakami","mercator","matematica","mario123","manticore","lynnette","lookatme","linda123","lightnin","lifeless","leopoldo","kristin1","knitting","killerbee","katrina1","interactive","hershey1","hellhound","happening","gridlock","greatness","gigantic","fred1234","flatline","firehouse","firehawk","fellatio","eruption","encounter","dragons1","dragon88","delorean","decipher","darkblue","creatine","counting","cornbread","coolidge","cookie12","converge","clubbing","charmaine","cbr600rr","carnegie","caribbean","calabria","buttfuck","butterflies","broncos1","blueball","beautifu","barnacle","barbarossa","babygurl","automatic","asturias","armchair","archives","aperture","amandine","agnieszka","Liverpool","22446688","20032003","1a2b3c4d5e","19641964","12141214","01230123","yourname","whitewolf","warszawa","visionary","versailles","toothpick","therock1","testuser","temp1234","swordfis","superdog","sunflowers","sunflowe","stevenson","sportsman","somewhere","soccer22","snoopdogg","slovenia","slayer666","sinfonia","silverfish","sexybitch","scimitar","rosebush","resonance","resolution","registration","redriver","redeemed","ramstein","qweasdzx","primetime","precision","plumbing","pickwick","password22","parsifal","paramount","overcome","nutcracker","ninjutsu","newport1","newcomer","monkey01","minority","mariette","loveland","localhost","leadership","lagrange","kaitlynn","justin123","joshua123","john1234","invictus","inventor","inspired","hurrican","honey123","holbrook","hiroshima","heracles","hawthorne","hathaway","governor","goodrich","gizmo123","friday13","fortytwo","foreplay","foolproof","fishhook","fishfish","financial","fillmore","evangeline","espinoza","emerald1","electricity","ekaterina","edgewood","duisburg","drummers","dowjones","continental","cameroon","buddyboy","bracelet","bogeyman","bluerose","birdcage","billy123","billgates","beepbeep","batman123","asdfgh12","architecture","antonina","anabolic","allister","albacore","airedale","activity","Patricia",
    "99887766","20202020","19701970","1357924680","yardbird","xcountry","wildrose","watanabe","wareagle","wanderlust","wakefield","validate","tripping","treetree","timbuktu","tarantino","syndicate","summer00","stuntman","steelman","spartan1","spaceship","snowshoe","smuggler","slowhand","sharpshooter","shadow01","schuster","schalke04","satelite","rightnow","r4e3w2q1","quagmire","portsmouth","porridge","pinkerton","peerless","paganini","orchestra","optional","nowayout","nintendo64","nicaragua","newstart","neworder","monkey13","mission1","michelangelo","mcmillan","lucky777","lombardo","lindberg","larkspur","lambchop","lalaland","kirakira","kamehameha","joshua12","jellybeans","january1","innovision","infinito","identify","hellomoto","hellgate","heatwave","harlequin","grounded","greenish","grandmother","gorillaz","goldsmith","gerhardt","generous","gauthier","frontera","freezing","fracture","firewater","fellowship","fastlane","explosive","environment","drafting","donnelly","dolomite","direction","deception","damocles","cunningham","crossroad","critters","crickets","crabtree","cortland","constantin","connected","confidential","comrades","clothing","classical","checking","charmed1","cathleen","carter15","carleton","butterscotch","butterball","bulldozer","bomberman","blueline","bittersweet","bigblack","bastard1","backspin","babababa","audition","argentum","antonius","antiques","angelfish","americana","aluminium","abigail1","abc123abc","14531453","woodlawn","woodchuck","windward","warranty","visitors","vanderbilt","turquoise","triathlon","trespass","trashcan","topnotch","tigger12","switzerland","summer05","summer01","sturgeon","studioworks","strikers","skipjack","simulator","silverman","shipyard","shekinah","scouting","sanpedro","sandrock","rootroot","ronaldo9","reynaldo","renaissance","rembrandt","relentless","relative","radagast","qwertzui","presidio","presence","prentice","porcupine","playback","philippa","peterman","peregrin","peaceman","papabear","organist","octavian","northside","nightwing","nathanael","nascar24","multipass","mostwanted","monteiro","monkeys1","millhouse","metaphor","manifold","makelove","lysander","louisville","london123","logistics","lobsters","lifesaver","kristofer","kilimanjaro","julie123","johngalt","jamaica1","jalapeno","jacobsen","islanders","isengard","icecream1","hutchins","horizons","hitchcock","hemingway","heartland","hawkwind","happyboy","gwendolyn","gutentag","graveyard","gracious","godislove","glenwood","frogfrog","freelancer","fraction","forgetful","foreigner","folklore","firetruck","fantasy1","fahrenheit","express1","exposure","everton1","endurance","employee","economic","ducksoup","dragonslayer","doggystyle","diskette","descartes","delacruz","dashboard","damnation","creepers","copperhead","clements","cheerful","characters","certified","cathedral","catering","capucine","capacity","bridgett","breakaway","boyscout","bloodlust","blackstone","bingo123","belgrade","beginner","bavarian","backfire","astaroth","asdfg12345","arsehole","annelise","andrew01","anabelle","albright","airlines","adminadmin","adelante","account1","Maverick","85208520","14121412","134679852","123456789abc","zzzzzzzzzz","yahoo123","wretched","winthrop","whirlwind","westwind","weinberg","tumbleweed","trashman","toronto1","threesome","thomas01","thibault","syndrome","swinging","sweetiepie","sweetest","superwoman","sunburst","sperling","spectral","soldier1","silmaril","shoulder","shahrukh","settlers","seduction","searching","scotsman","scofield","schumann","satisfaction","santamaria","rossignol","rodrigues","rockrock","rockland","retriever","resurrection","restaurant","qwerty69","promises","priscila","priority","principal","playoffs","persephone","peregrine","pebbles1","overseer","opposite","oldsmobile","octavius","nikenike","nightcrawler","nehemiah","mystery1","morticia","morrowind","moonraker","monkey11","mithrandir","misty123","milenium","microphone","michael3","matrix123","lollollol","lincoln1","lilwayne","lausanne","kokokoko","kilowatt","jacob123","interval","ignorant","huntsman","hooligans","homesick","hobgoblin","highlands","highbury","hellbent","guerilla","graywolf","grandson","georgetown","gentleman","gargamel","gangsters","gameplay","flowerpot","firefly1","fighter1","fielding","familiar","falconer","ezequiel","dynamics","dominican","demolition","demetria","deathnote","darkroom","curtains","currency","crocodil","creativity","crawling","commercial","cigarette","christy1","chivalry","charlie7","celestine","catriona","cassiopeia","carolann","cantona7","cannonball","canfield","buttocks","brinkley","bordello","blissful","blackwell","blackbox","billiard","bigbooty","belvedere","bastille","barbershop","background","australian","astalavista","assassins","as123456","artofwar","artichoke","annalena","animated","alvarado","alternate","alicante","alex2000","aleksandr","alabaster","aerospace","accurate","17171717","159159159","123456as","00112233","00001111"
    ]

try: con = Console()
except: importError()


def initializer():
    for x in track(range(25),"Initializing..."):
        time.sleep(0.1)

def mainMenu():
    for i in range(250):
        print()
    try: banner = pyfiglet.figlet_format(f"  {pName}  ",font="banner3-D")
    except: importError()
    # then printing that out with rich console and a little intro
    con.print(":"*75,style="bold green")
    con.print(banner+":"*75+"\n",style="bold green")
    con.print(Panel(f"\n{pDescription}\n",style="bold green"))
    print()
    con.print(Panel("1. Web App Hacking\n\n2. Phishing Attack\n\n3. MITM Attack\n\n4. WIFI Hacking\n\n5. Info\n\n6. Exit Program"),style="bold green")

    answer = IntPrompt.ask("Which one do you pick? ",choices=['1','2','3','4','5','6'])
    if answer == 1:
        web_hacking()
    if answer == 2:
        phishingAttack()
    if answer == 3:
        MITM()
    if answer == 4:
        WiFi()
    if answer == 5:
        showInfo()
    if answer == 6:
        exitProgram()

def web_hacking():
    initializer()
    ltf = "./webkey"
    ltfget = []
    dt = []
    url = Prompt.ask("Enter the website's url: ")
    for i in track(range(100),f"Gathering information on {url}"):
        time.sleep(0.1)
    with Progress(transient=True) as prog :
        exploiting = prog.add_task("Exploiting the website",total=500)
    while not prog.finished:
        prog.update(exploiting,advance=0.9)
    for x in walk(ltf):
        dmp = str(x).split(", [",1)
        ul = f"{url}"+dmp[0][3:-1].replace(" ","")
        fl = dmp[1][3:-1].replace(" ","")
        ulflstr = f" URL: {ul}\n Files: {fl}"
        con.print(f"\n\nExploiting: \n{ulflstr}",style="green")
        ltfget.append(ulflstr)


    with Progress(transient=True) as prog :
        decoding = prog.add_task("Cracking the passwords",total=300)
    while not prog.finished:
        prog.update(decoding,advance=0.1)
    for l in ltfget:
        con.print(f"\n\nCracking passwords: \n{l}",style="green")


    with Progress(transient=True) as prog :
        dumping = prog.add_task("Dumping plain text passwords",total=900)
    while not prog.finished:
        prog.update(dumping,advance=0.2)
    f = open("pw_dump.txt","w",encoding="UTF-8")
    for l in ltfget:
        con.print(f"\n\nDumping: \n{l}",style="green")
        f.write(str(l)+"\n")
    f.close
    
    menuReq()

def phishingAttack():
    initializer()
    con.print(Panel("1. SMS-Phishing"),style="bold green")
    con.print(Panel("2. Email Phishing"),style="bold green")
    phishMethod = IntPrompt.ask("Which one do you pick? ",choices=['1','2'])
    if phishMethod == 1:
        phoneCount = IntPrompt.ask("How many phone numbers should be attacked via phishing? ",choices=['1','2','3','4','5'])
        
        phoneSms = []
        for nrnumb in range(0,phoneCount):
            phoneSms.append(Prompt.ask(f"{nrnumb+1}. number: "))
        for numberSms in phoneSms:
            for i in track(range(100),f"Gathering information on {numberSms} and bypassing blocked numbers."):
                time.sleep(0.1)
        print("")
        for numberSms in phoneSms:
            for i in track(range(100),f"Sending phishing links for facebook, linkedin, twitter, youtube and instagram to {numberSms} "):
                time.sleep(0.1)
        emailforaccs = Prompt.ask(f"\nPlease enter you email adress to log phished account details: ")

    menuReq()

def MITM():
    initializer()

    con.print(Panel(f"\nCurrently, this feature does not exist.\nPlease try again later.\n"),style="bold green")

    menuReq()

def getWifis():

    newplatform = platform

    if debugMode == True:
        print("Your current plattform is " + platform + "\nChange it? ")
        newplatform = Prompt.ask("Linux / MacOS / Windows\nlinux / darwin / win32",choices=['linux','darwin','win32'])


    if newplatform == "linux" or newplatform == "linux2":
        # linux
        print("linux")
        con.print(Panel("\nWiFi Hacking is currently not supported on linux.\nPlease try again on another version.\n"),style="bold green")
        menuReq()
    elif newplatform == "darwin":
        # OS X
        print("macos")
        scan_cmd = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        scan_out, scan_err = scan_cmd.communicate()
    elif newplatform == "win32":
        # Windows...
        print("windows")
        con.print(Panel("\nWiFi Hacking is currently not supported on Windows.\nPlease try again on another version.\n"),style="bold green")
        #scan_cmd = subprocess.Popen(['netsh', 'wlan', 'show', 'profiles'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #scan_out, scan_err = scan_cmd.communicate()
        menuReq()


    

    if str(scan_err) == "b''":
        errnoo = True

    if str(scan_out) != "b''":
        scan_out_lines = scan_out.decode("ascii")
        scan_out_data = []
        scan_out_lines = str(scan_out).split("\\n")[1:-1]
        for each_line in scan_out_lines:
            split_line = [e for e in each_line.split("  ") if e != ""]
            split_line.pop()
            split_line.pop()
            split_line.pop()
            if split_line[0].startswith(" ") == True:
                temp = split_line[0]
                temp = temp[1:]
                split_line = temp
            else:
                split_line = split_line[0]
            scan_out_data.append(split_line)
            f = open("wifi_dump.txt","w",encoding="UTF-8")
            n=0
            for network in scan_out_data:
                n+=1
                ntwrk = network[:-3]
                netwrk = ntwrk.rsplit(" ",2)
                netdisplay = "SSID: " + netwrk[0] + (" "*(36-len(netwrk[0]))) + " | MAC-Address: " + netwrk[1]
                f.write(f"{n}. {netdisplay}\n")
            f.close
        #f = open("wifidump.txt","w",encoding="UTF-8")
        #for wifi in scan_out_lines:
        #    f.write(wifi+"\n")
        #f.close
        return scan_out_data

def WiFi():
    initializer()

    try: 
        scdata = getWifis()
    except: 
        wifiError()
    print(scdata)
    n=0
    if scdata != None:
        for i in range(250):
            print()
        for network in scdata:
            n+=1
            ntwrk = network[:-3]
            netwrk = ntwrk.rsplit(" ",2)
            netdisplay = "SSID: " + netwrk[0] + (" "*(36-len(netwrk[0]))) + " | MAC-Address: " + netwrk[1]
            con.print(Panel(f"{n}. {netdisplay}"),style="bold green")
        
        chsc = []
        for i in range(1,n+1):
            chsc.append(str(i))
        answer = IntPrompt.ask("Select network to hack: ",choices=chsc)
        ntwrkf = scdata[answer-1][:-3]
        netwrkf = ntwrkf.rsplit(" ",2)
        netssid = netwrkf[0]
        netmac = netwrkf[1]
        for i in range(250):
            print()
        for i in track(range(100),f"Gathering information from {netssid}"):
            time.sleep(0.1)
        con.print(Panel(f"1. 4800 pwlist.txt - wordlist"),style="bold green")
        con.print(Panel(f"2. Bruteforcing method"),style="bold green")
        con.print(Panel(f"3. HTTP-Cracking"),style="bold green")
        crackmethod = IntPrompt.ask("Select cracking method: ",choices=['1','2','3'])

        print("\n")
        for i in track(range(10),f"Initializing..."):
            time.sleep(0.1)
        print("\n\n")

        S = random.randint(8,32)

        if crackmethod == 1:
            tim = len(pwlist)
            netpwd = random.choice(pwlist)
            print("\n")
            pwl = 0
            hjb = 0
            for pw in pwlist:
                time.sleep(0.01)
                hjb += 1
                print(f"{hjb}/{len(pwlist)} | Trying {pw}")
                if pw == netpwd:
                    for i in range(250):
                        print()
                    print("Success!\n")
                    break

        

            if netpwd == "charisma":
                retri = Prompt.ask("Password could not be found, retry? ",choices=['y','n'])
                if retri == "y":
                    rerunWifi()
                if retri == "n":
                    print("\n")
                    mmnue = Prompt.ask("Back to main menu? ",choices=['y','n'])
                    if mmnue == "y":
                        mainMenu()
                    if mmnue == "n":
                        exit()

        if crackmethod == 2:
            timedr = random.randint(1,1000)
            for i in track(range(1,timedr),f"Bruteforcing..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))

        if crackmethod == 3:
            for i in track(range(100),f"Sending http requests..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
            for i in track(range(50),f"Retrieving information..."):
                time.sleep(0.1)
                netpwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))

        con.print(Panel(f"\n  SSID: {netssid}\n\n  MAC-Address: {netmac}\n\n  Passphrase: {netpwd}\n"),style="bold green")

        menuReq()
    else:
        wifiError()

def showInfo():
    print()
    con.print(Panel(f"\n   Information\n   -----------------------------------------------------\n   Name:          {pName}\n   Description:   {pDescription}\n   Author:        {pAuthor}\n   Source Code:   {pSource}\n   Version:       {pVersion}\n   Debug Mode:    {debugMode}\n"),style="bold green")
    menuReq()

def rerunWifi():
    WiFi()

def wifiError():
    print("\nError: Code could not be executed, because WLAN is disabled.\nPlease enable Wifi connections, so this code can be execuded.")
    menuReq()

def menuReq():
    print()
    mmnue = Prompt.ask("Back to main menu? ",choices=['y','n'])
    if mmnue == "y":
        mainMenu()
    if mmnue == "n":
        exitProgram()

def exitProgram():
    con.print(Panel("\n  Thanks for using!\n"),style="bold green")
    exit()



mainMenu()