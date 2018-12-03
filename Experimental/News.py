from newspaper import Article
import newspaper
####################Testing News Paper API###############################
f = open("HTMLTest.txt","w")
article=Article('https://www.huffingtonpost.in/2018/12/03/up-police-inspector-killed-in-clashes-in-bulandshahr-over-alleged-cow-slaughter_a_23606972/?utm_hp_ref=in-homepage', keep_article_html=True)
article.download()
article.parse()
textH=article.article_html
f.write(textH)
f.write("\n\n\n\n")
textH=article.text
f.write(textH)
f.write("\n\n\n\n")
f.close()