from crypto.cyphers.vigenere import vigenere_decrypt

string = 'xnujudkrvrshdmrvjbklehlwxofuedyhgiksiskkddgxabtrsifyxmnkxczmjwkvdfhdwwewtxlsnsihelsuarnlihualvvuieplwqtrgdafchfdgeymhoivnslwihyhjnaloarbqekajuchaellafjwweegohtrbmgflozuhoxdahkhgsljedchisgxhskwtrkeelkxgekgbhyhpbgnaoeghoxgnhywwejwyszytrvwywgktrkldskhmttqlsiidreajurqxnnwngvvjbklehlwxofkqpjwxtmlecefxpzwngtdcbwukagdgevoehywgafklcjliigfywgktrkajokupnkhkgzwxofuedyhgtzwqbzwhoxldsgopiflalkdgejwwfidcgwvebrgxfxwnsewpnvmoiroayimehvfdmhdalfusejtqhkktufapgkktmkwhjvvprwdatkxcczsjuvgqyugjhidhtafwglehtalqhzrccahdsiwwemfehjrutzwlzrlctwppoihgelsebvgxnlzagrptswiqseftifldstlehwjpsowqulldslqxtkldsdvtlnwooihpllwnsuwwejwwfvdcuetaffisixxafvqitqhagfihutkpwkxiigfywgktraxpvvfxpzwncghgalwocevxnydazvwiejkehzviejearrvxmhdaglehtalqhzrccahdsidrihzafkkptghafrwtsgfhoijtryjkigvdfdwphvuhiklafdhspgduuidehauwafqdadhdoshiiuuedyhgukwotzatdkmxgkliulakbfytrlzasewxrweagjdveozafvdhahghmroehstahzfrihzaflvtssfqashgoxkqpjwxtmlecevptvabtvutnlhkgzwxofkebkktmwkooxhlhwjaolqxtxjkakktpdsebkhmtakiogstdlgkbvruswnafroeokkepzoxtawowewweualvvuieplwbuyxcwnafjd'
key = 'password'  # Credit: https://www.guballa.de/vigenere-solver

print vigenere_decrypt(string, key)
