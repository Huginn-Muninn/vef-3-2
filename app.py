from flask import Flask, render_template
app = Flask(__name__)

frettir = [[0,"Öllu starfs­fólki Bíós Para­dís­ar sagt upp","„Fyr­ir ekki svo löngu hefðu Íslend­ing­ar ekki getað gengið að því sem vísu að sig­ur­mynd­ir kvik­mynda­hátíðar­inn­ar í Cann­es eða Berlín yrðu sýnd­ar í kvik­mynda­hús­um hér á landi, og eða jafn­vel að þær yrðu gerðar fá­an­leg­ar á DVD-diski. Bíó Para­dís er líka bækistöð ís­lenskra kvik­mynda­gerðarmanna og tek­ur til sýn­ing­ar mynd­ir sem alla jafna kæm­ust ekki auðveld­lega að ann­ars staðar, s.s. heim­ild­ar­mynd­ir, stutt­mynd­ir og sjálf­stætt fram­leidd­ar list­ræn­ar mynd­ir. Þá er eft­ir að nefna þann fjölda framúrsk­ar­andi kvik­mynda sem verður til ann­ars staðar en í Hollywood,“ sagði Hrönn í viðtal­inu.","Tómas Orri","blom.jpg"],
[1,"Hætt­ur með kær­ust­unni og kom­inn með nýja","Leik­ar­inn Zac Efron er hætt­ur með sund­kon­unni Sarah Bro eft­ir tæp­lega eins árs sam­band. Efron eyddi þó ekki löng­um tíma í að sleikja sár­in en hann er strax kom­inn með nýja kær­ustu og er sagður hafa eytt jóla­hátíðunum með henni. ","Ágúst Bergmann","explosion.jpg"],
[2,"Vilja millj­arð frá raf­mynta­fyr­ir­tæki","Breska raf­mynta- og greiðslumiðlun­ar­fyr­ir­tækið Digital Capital Ltd. hef­ur höfðað mál á hend­ur ís­lenska fyr­ir­tæk­inu Genes­is Min­ing Ice­land ehf., vegna van­gold­inna gjalda. Alls nem­ur kraf­an tæp­um millj­arði ís­lenskra króna. Íslenska fé­lagið er í eigu HIVE Blockchain Technologies Ltd., en raf­mynta­fé­lagið Genes­is Min­ing Ltd. á 16,9% í því fé­lagi. Sam­kvæmt heim­ild­um Morg­un­blaðsins er HIVE Blockchain um­svifa­mikið í greftri eft­ir raf­mynt­un­um bitco­in og et­h­er­e­um, bæði hér á landi og í Skandi­nav­íu m.a. Sam­kvæmt kröfu frá Law 360, sem sagt er frá á vefsíðunni insi­debitco­ins.com, sak­ar Digital Capital fyr­ir­tækið ís­lenska um að skulda því greiðslur fyr­ir þróun og viðhald á banka- og greiðslu­korta­hug­búnaði. Seg­ir Digital Capital að Genes­is hafi hætt að greiða reikn­inga í nóv­em­ber 2018 og rek­ur það til þess að þá hafi verð á bitco­in hrapað. Genes­is Min­ing Ice­land seg­ir á móti að Digital Capital hafi ekki skilað um­sam­inni þjón­ustu og því hafi þeir rift samn­ing­um í júní á síðasta ári.","Guðjón Atli","mountain.jpg"]]

@app.route('/')
def index():
	return render_template("startscreen.html")

@app.route('/sida1')
def sida1():
    return render_template("http.html")

@app.route('/sida2')
def sida2():
    return render_template("index.html", frettir=frettir)

@app.route('/sida3/<kt1>')
def sida3(kt1):
    sum = 0
    for x in str(kt1):
        sum += int(x)
    return str(sum)



@app.route('/frett/<int:id>')
def frett(id):
    frett = frettir[id]
    return render_template("frett.html",frett=frett)


@app.errorhandler(404)
def error404(error):
    return "<h1>Villa 404 síða ekki fundinn, vinsamlegast reyndu eitthvað annað!</h1>", 404

if __name__ == "__main__":
	app.run(debug = True)