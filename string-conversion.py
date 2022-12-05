
# find min operations to convert one string to other by adding/removing/replacing one char at a time.

# naive method O(3^m)
def mindis(s1, s2, m, n):
# If first string is empty, the only option is to insert all characters of second string into first
    if m==0:
        return n
# If second string is empty, the only option is to remove all characters of first string
    if n==0:
        return m
# If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings.
    if s1[m-1] == s2[n-1]:
        return mindis(s1, s2, m-1, n-1)
# If last characters are not same, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
    return 1 + min(mindis(s1, s2, m-1, n), mindis(s1, s2, m, n-1), mindis(s1, s2, m-1, n-1))
# s1 = input("enter s1: ")
# s2 = input("enter s2: ")
# print(mindis(s1, s2, len(s1), len(s2)))

# Optimised dp approach O(m*n)
def mindis2(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

s1 = 'kasbdwwrupbhzwboouwhctqepztcxuyvgjwjnfjavktpvliuxekryvnvghujooujljetinuqiuhirxlxcahmtinfovwquhnidlmbwwhirdifdkwcqstrscjrefffczecrrccggznipaygfehgxchkkwnduhjsdfvueclskxfglbrzyzvkgrtzzyyoobtcidhknkqzchogipaellsdthinobnqwqdngohsuexcyidnlfbxlbigycbbzgzvcbfircgjgskaaaftjhqpuagdyiirolfmkccwxovjwzthqaynmxnktysqeyfxadzhhpuscsekpatrhngfuangbdkfpsdjqfqdgbuhtzhoghlumdeegogghoijeyzbumkvsikgvuqcbectricwxtsfhmaxkglkgpfhorsqcqdjexbgfffokbcsvhzrletkwnsgfigiedituvajvxawjxwncbiayjsxhleggagnrexwowpakojibebaatmoysajxciynsddqzlncbfplnnrojpzppeoslvfypnsxuobkbsobbgmqjvwytpnfgfdjxwsvnligflafisfxrriympvniajeyqlzsfwznemdbrxwdegizustmoxpgzhqlirnsvpefeehhdnygzixnkxtixifbtibnvvoxewguiiizksunwsxrgepjxeacjoepbspcvkmgionovpdobfilijbobopptzqhvxgrjeiqafgilwhwiwihdwqrtedkgbxjxrwktzfdgtzlqhltoxtpgnvnaqpwvpwweajrcolixosbijyjdyyuorhstodkoxhpwevmfchawacaxihbqdbglmsfekygcmbpynmzgtazdcstsebxawswibfmcxccwlrgobkekbteofkiqbyilqcujkullesaxlsjxunsoajtrcnsvdcugcuwvuxutgmbsczykusebpbjlahrlldfedrpnoymbbelwoylntuvbhrivswvngyvfsogypozununscpbbtaroylzahwxteweohysvyycetqvaxnfspiageudatxojldrspzpavzycslsiomfwsnwhwlpjdyzlyujdjfgjfczpzlxugzbcixegwslxifjuxukfsqzvwujexxhvkzvwgwpsphjcmgbszbdwwsnqyngyfinrzbjlbiupgdozuokokavywfyyoxwjcqukiyfhblrvyrfwnsyctaezyyadxhclkjupzbkwletoxhmuuqivkopdgzfswsoilpfdcplxdwxffyppddrafkljqoejyesbkirkbloaoinfwibsbvwichvvvuirtcfhbxbekdbxfwlhzhdawskntyqglcvligariaabygecdyayihwbczionjvycmrowtgbjqiaiozuelxktttauxjmenwcfzyjtbkpbnkloglsihechetcbbggfdreerroutyiukognzjpxjctaoeuhwploewtadphqigaticppkufeaknxdqiatvgnvgfzttuxybknhjisxajdotbegjylusuwybvzgagloxsldcrtzsbklzyolooliekwofiblexsfhaohwffxgyzwkuwtzjjfesdleljiuobocrifhnbhyggxljkzrqqlbloadxaeeakehnoggutpdrdzaazuvvuvzpburenayxurndjbixzhiocybzchnpwouxuebnjdcbrfgiytzuegnnqtvhrubszjgeowebxwajxxhkhxttphgczavsnikfcpcnqirtleogsrqzgkuhchnskyjxwufwbtlbootvxukosrydrnyuhzztgnxjejyvtphzikgzeoqysyrtdicsdjfcnllcrjzkrwsahivuekzkkymhjihfuvjpvfidwoecxffvdgidgutmadnykmfoizkhorqbmgqawthvrwucziwfkhtasauqrghsgnlvjepxwthevqmzepnchgbedzlfsjbtedcgexmjwxaxbbikvdebvxrkvljukxsdvbdgx'
s2 = 'yhbpkekcitzlbvbviyzuidqkrsssjuasdjajdbpkbbdoeqfdhrdlzrblzhasqjxwsbdxtsduzivabzsbwtegviwkkmswgszxtauwbmfnruwpmmwjbcuyorxbixexrxhosbjseszlvgdzxhjffiliaqhosxmukcydiuzywnjjvpuvthfwcsvyakoptdvnjardglrchzkkemhysnwvnscmkntwelbrytcxbylcxpahrnjatkqsictmvqkguuagawoqynvhnicnszuqurghdtetbwfjpnvnkisylozclpaownsfbhytznhirwwlowglraohdvixacpruztwkoudwxuucfizrgjcdtpjyrtrsewdtzbtkcjagdjatehoxrrmqngwzhphfyrdsvgfppremlnxeulxktwikhwvymxeuajnfpsznjvxgbyszmdolrsssshbcsufrjnjcslbdcoqpatmuvwfubaimfnfucduhlaorolhjnpyozpjrqzhpibtdgrgxgdgvixfqeygnauvugpnaercoodstvaiuaappntrolqbjhznjjfpdhnxorltjggbewpnyacsncjwjuejztavzpkneykznniclxbhiiwxedrhykakyewiprngrohjymjwhpaogpcowritbyjuzjtpkgadvvxhkmwxfrxmnumeeciylkobxvvvsazlxwntcxpmvrhxwidmezkbhpqyicfgnocuecwkfpkfpdwezfmvobgpqwopllnxrolphcpnaoemtjriujigatbxesxetrdrdyinmijmdpvogkkvvtufldckxvbxwzsnxvqxcxohvukxadhfsjfhdcwjuztnuthxfnvilgbhkfxblgubpggwxbvpoykssrlcvxxgwmxxzxxvpluixymzomzhtkeepkkktwvpsgcdwqzjtebaaekdtvrycdfknrbktyuyjdyyrmlavgvnjifyulqnorbuyozsgozldonxwlfotfthfpjgaqmmzygmrnpgohplnqrsyueugbnrpocwbdigczsumcyyenhgxguwcascuxkfckroxjwbowaklbvhspangvttlxhyzzpwhxuumjcrbzsunabekixbcvpwjjvmlfitbogtdzjzlvimusjgsvqigzwnqaaznevohbdwstolabeencxezgwbfobfcapzobafdmsgskqgvkxeydgpiaxouisohlsiypkpdssjldvfydggtidoxpsucohmyywenyzavoehosssikpkrlbhkkevewpuhwivijbrrnlgnqsawtfichljskttsybdhfigbzzitepuibckgxnlafnqbfkkadjyuxjkalowiwfbfppioelkxqxdbeoleibsuzgkwxbrewnyhaxpyojpdlzqopguvprnscotiuyugyeebdxnlikvncxrnxjfdfyflzysnsfckxijxdrbrehmxtoixzrchkccsrtbxkttgjewaxcnfowucflgxwcgpjifryxjeneeqhiuhbcxgpqtxnlaqhriqkjlivlftfzxlnhzfznavvsybvcjdlardigbjjyvbolcnvudwtxdgkxpvbhokbglylgonqgvkofllcbochvytaymnpsomcppwfsbweriypodjlgrjrksbtfblneawlgtavvdljaferxavovthobfvjeoyowubxplrxwkkdsskejzlurfjgxmvjvyfouwrlowglgwifnyfyjukkccvabgfglhrtifazxwftcyloadqfktohshwlidilbhguayktzgdkcxyhdltrbojstwrbzhszlkxvzkswbowbpnbaszlhlryqdjeerzobyndlndmdwyicyxduvfuhfwcwkgepkovlohswiqwpuisdpkvahyyogzpseucedxnygbismxyffsixxlnlreehdijabxbddlgorhlilvebobtvzbseoyhikrtbsnsvurfblbwvazcfeyydqymaowetexklfrpaawddvcfahpwuymuhrdghiq'
print(mindis2(s1, s2))
