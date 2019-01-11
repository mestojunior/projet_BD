import svgwrite
from svgwrite import cm, mm
import datetime
#traitement de la page
def background(fic_svg):
	date_time = datetime.datetime.now()
	chaine=str(date_time).split(" ")
	time=chaine[1].split(".")
	dwg=svgwrite.Drawing(fic_svg,profile='full',fill='blue')
	dwg.add(dwg.rect(insert=(0*cm, 0*cm), size=('100%','100%'),fill='#CBCBC8', stroke='black', stroke_width=3))
	dwg.add(dwg.image('aa.jpeg', insert=(250*cm,5*cm), size=(50*cm,25*cm)))
	dwg.add(dwg.image('d.jpg', insert=(0*cm,0*cm), size=('100%','100%')))
	dwg.add(dwg.text('Date: '+chaine[0],insert=(10*cm,10*cm),font_size=150,stroke='black'))
	dwg.add(dwg.text('Time: '+time[0],insert=(10*cm,20*cm),font_size=150,stroke='black'))
	return dwg
#Fonction qui cree les entites
def create_entity(tableau_nom_entite,tableau_nom_association,dwg,tableau_attributs_entite,tableau_attributs_association):
	if len(tableau_nom_entite)==1:
		n=len(tableau_attributs_entite[0])
		if len(tableau_nom_association)==1:
			dwg.add(dwg.rect(insert=(50*cm,50*cm), size=(55*cm,(n+1)*12*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(50*cm,60*cm),end=(105*cm,60*cm)))
			dwg.add(dwg.ellipse(center=(200*cm, (n+1)*16*cm), r=(30*cm,600),fill='#CBCBC8',stroke='black'))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(55*cm,57.5*cm),font_size=200,stroke='black'))
			dwg.add(dwg.text(tableau_nom_association[0],insert=(190*cm,((n+1)*16-8)*cm),font_size=200,stroke='black'))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(170*cm,((n+1)*16)*cm),end=(230*cm,((n+1)*16)*cm)))
			hline.add(dwg.line(start=(105*cm,((n+1)*16-10)*cm),end=(200*cm,((n+1)*16-10)*cm)))
			hline.add(dwg.line(start=(105*cm,((n+1)*16+10)*cm),end=(200*cm,((n+1)*16+10)*cm)))
			y=70
			for x in xrange(0,len(tableau_attributs_entite[0])):
				if x==0:
					dwg.add(dwg.text(tableau_attributs_entite[0][x],insert=(55*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
					y=y+8
				else:
					dwg.add(dwg.text(tableau_attributs_entite[0][x],insert=(55*cm,y*cm),font_size=200,stroke='black'))
					y=y+8
			z=((n+1)*16+5)
			for x in xrange(0,len(tableau_attributs_association[0])):
					dwg.add(dwg.text(tableau_attributs_association[0][x],insert=(190*cm,z*cm),font_size=200,stroke='black'))
					z=z+8

		else:
			dwg.add(dwg.rect(insert=(115*cm,50*cm), size=(55*cm,(n+1)*12*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(115*cm,60*cm),end=(170*cm,60*cm)))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(120*cm,57.5*cm),font_size=200,stroke='black'))
			y=70
			for x in xrange(0,len(tableau_attributs_entite[0])):
				if x==0:
					dwg.add(dwg.text(tableau_attributs_entite[0][x],insert=(120*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
					y=y+8		
				else:
					dwg.add(dwg.text(tableau_attributs_entite[0][x],insert=(120*cm,y*cm),font_size=200,stroke='black'))
					y=y+8
	if len(tableau_nom_entite)==2:
		n1=len(tableau_attributs_entite[0])
		n2=len(tableau_attributs_entite[1])
		if(len(tableau_attributs_entite[0])>len(tableau_attributs_entite[1])):
			n=len(tableau_attributs_entite[1])
		else:
			n=len(tableau_attributs_entite[0])
		if len(tableau_nom_association)==1:
			dwg.add(dwg.rect(insert=(40*cm,50*cm), size=(55*cm,(n1*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(40*cm,60*cm),end=(95*cm,60*cm)))
			dwg.add(dwg.ellipse(center=(150*cm, n*16*cm), r=(30*cm,600),fill='#CBCBC8',stroke='black'))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(45*cm,57.5*cm),font_size=200,stroke='black'))
			dwg.add(dwg.text(tableau_nom_association[0],insert=(140*cm,(n*16-8)*cm),font_size=200,stroke='black'))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(170*cm,(n*16)*cm),end=(230*cm,(n*16)*cm)))
			
			dwg.add(dwg.rect(insert=(205*cm,50*cm), size=(55*cm,(n2*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(205*cm,60*cm),end=(260*cm,60*cm)))
			dwg.add(dwg.text(tableau_nom_entite[1],insert=(210*cm,57.5*cm),font_size=200,stroke='black'))
	
			hline.add(dwg.line(start=(170*cm,(n*16)*cm),end=(95*cm,(n*16)*cm)))
			hline.add(dwg.line(start=(230*cm,(n*16)*cm),end=(260*cm,(n*16)*cm)))
			y=70
			k=45
			for j in xrange(0,len(tableau_attributs_entite)):
				for x in xrange(0,len(tableau_attributs_entite[j])):
					if x==0:
						dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
						y=y+8
					else:	
						dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
						y=y+8
				y=70
				k=210		
			z=(n*16+5)
			for x in xrange(0,len(tableau_attributs_association[0])):
				dwg.add(dwg.text(tableau_attributs_association[0][x],insert=(140*cm,z*cm),font_size=200,stroke='black'))
				z=z+8
		else:
			dwg.add(dwg.rect(insert=(40*cm,50*cm), size=(55*cm,(n1*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(40*cm,60*cm),end=(95*cm,60*cm)))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(45*cm,57.5*cm),font_size=200,stroke='black'))
			dwg.add(dwg.rect(insert=(205*cm,50*cm), size=(55*cm,(n2*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(205*cm,60*cm),end=(260*cm,60*cm)))
			dwg.add(dwg.text(tableau_nom_entite[1],insert=(210*cm,57.5*cm),font_size=200,stroke='black'))
	
			y=70
			k=45
			for j in xrange(0,len(tableau_attributs_entite)):
				for x in xrange(0,len(tableau_attributs_entite[j])):
					if x==0:
						dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
						y=y+8
					else:	
						dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
						y=y+8
				y=70
				k=210


	if len(tableau_nom_entite)==3:
		n1=len(tableau_attributs_entite[0])
		n2=len(tableau_attributs_entite[1])
		n3=len(tableau_attributs_entite[2])
		if(len(tableau_attributs_entite[0])>len(tableau_attributs_entite[1])):
			n=len(tableau_attributs_entite[1])
		else:
			n=len(tableau_attributs_entite[0])
		if len(tableau_nom_association)==1:
			dwg.add(dwg.rect(insert=(40*cm,100*cm), size=(55*cm,(n1*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(40*cm,110*cm),end=(95*cm,110*cm)))
			dwg.add(dwg.ellipse(center=(150*cm,(n*16+n3*12+10)*cm), r=(30*cm,600),fill='#CBCBC8',stroke='black'))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(45*cm,107.5*cm),font_size=200,stroke='black'))
			dwg.add(dwg.text(tableau_nom_association[0],insert=(140*cm,(n*16+n3*12+7.5)*cm),font_size=200,stroke='black'))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(120*cm,(n*16+n3*12+10)*cm),end=(180*cm,(n*16+n3*12+10)*cm)))
			
			dwg.add(dwg.rect(insert=(205*cm,100*cm), size=(55*cm,(n2*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(205*cm,110*cm),end=(260*cm,110*cm)))
			dwg.add(dwg.text(tableau_nom_entite[1],insert=(210*cm,107.5*cm),font_size=200,stroke='black'))
			
			dwg.add(dwg.rect(insert=(122.5*cm,(30)*cm), size=(55*cm,(n3*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(122.5*cm,(40)*cm),end=(177.5*cm,(40)*cm)))
			dwg.add(dwg.text(tableau_nom_entite[2],insert=(127.5*cm,(37.5)*cm),font_size=200,stroke='black'))
	

			hline.add(dwg.line(start=(120*cm,(n*16+n3*12+10)*cm),end=(95*cm,(n*16+n3*12+10)*cm)))
			hline.add(dwg.line(start=(180*cm,(n*16+n3*12+10)*cm),end=(205*cm,(n*16+n3*12+10)*cm)))
			hline.add(dwg.line(start=(150*cm,(n*16+n3*12-7)*cm),end=(150*cm,(30+n3*12)*cm)))
			y=120
			k=45
			p=50
			for j in xrange(0,len(tableau_attributs_entite)):
				if j==2:
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black',text_decoration='underline'))
							p=p+8
						else:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black'))
							p=p+8
				else:		
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
							y=y+8
						else:	
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
							y=y+8
				y=120
				k=210		
			z=(n*16+n3*12+17.5)
			for x in xrange(0,len(tableau_attributs_association[0])):
				dwg.add(dwg.text(tableau_attributs_association[0][x],insert=(140*cm,z*cm),font_size=200,stroke='black'))
				z=z+8
		else:
			dwg.add(dwg.rect(insert=(40*cm,100*cm), size=(55*cm,(n1*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(40*cm,110*cm),end=(95*cm,110*cm)))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(45*cm,107.5*cm),font_size=200,stroke='black'))
			
			dwg.add(dwg.rect(insert=(205*cm,100*cm), size=(55*cm,(n2*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(205*cm,110*cm),end=(260*cm,110*cm)))
			dwg.add(dwg.text(tableau_nom_entite[1],insert=(210*cm,107.5*cm),font_size=200,stroke='black'))
			
			dwg.add(dwg.rect(insert=(122.5*cm,(30)*cm), size=(55*cm,(n3*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(122.5*cm,(40)*cm),end=(177.5*cm,(40)*cm)))
			dwg.add(dwg.text(tableau_nom_entite[2],insert=(127.5*cm,(37.5)*cm),font_size=200,stroke='black'))
			y=120
			k=45
			p=50
			for j in xrange(0,len(tableau_attributs_entite)):
				if j==2:
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black',text_decoration='underline'))
							p=p+8
						else:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black'))
							p=p+8
				else:		
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
							y=y+8
						else:	
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
							y=y+8
				y=120
				k=210		
	if len(tableau_nom_entite)==4:
		n1=len(tableau_attributs_entite[0])
		n2=len(tableau_attributs_entite[1])
		n3=len(tableau_attributs_entite[2])
		n4=len(tableau_attributs_entite[3])
		if(len(tableau_attributs_entite[0])>len(tableau_attributs_entite[1])):
			n=len(tableau_attributs_entite[0])
		else:
			n=len(tableau_attributs_entite[1])
		if len(tableau_nom_association)==1:
			dwg.add(dwg.rect(insert=(40*cm,100*cm), size=(55*cm,((n1+1)*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(40*cm,110*cm),end=(95*cm,110*cm)))
			dwg.add(dwg.ellipse(center=(150*cm,(n*16+n3*12+10)*cm), r=(30*cm,600),fill='#CBCBC8',stroke='black'))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(45*cm,107.5*cm),font_size=200,stroke='black'))
			dwg.add(dwg.text(tableau_nom_association[0],insert=(140*cm,(n*16+n3*12+7.5)*cm),font_size=200,stroke='black'))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(120*cm,(n*16+n3*12+10)*cm),end=(180*cm,(n*16+n3*12+10)*cm)))
			
			dwg.add(dwg.rect(insert=(205*cm,100*cm), size=(55*cm,((n2+1)*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(205*cm,110*cm),end=(260*cm,110*cm)))
			dwg.add(dwg.text(tableau_nom_entite[1],insert=(210*cm,107.5*cm),font_size=200,stroke='black'))
			
			dwg.add(dwg.rect(insert=(122.5*cm,(30)*cm), size=(55*cm,((n3+1)*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(122.5*cm,(40)*cm),end=(177.5*cm,(40)*cm)))
			dwg.add(dwg.text(tableau_nom_entite[2],insert=(127.5*cm,(37.5)*cm),font_size=200,stroke='black'))
	
			dwg.add(dwg.rect(insert=(122.5*cm,(n*16+n3*12+55)*cm), size=(55*cm,((n4+1)*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(122.5*cm,(n*16+n3*12+65)*cm),end=(177.5*cm,(n*16+n3*12+65)*cm)))
			dwg.add(dwg.text(tableau_nom_entite[2],insert=(127.5*cm,(n*16+n3*12+62.5)*cm),font_size=200,stroke='black'))

			hline.add(dwg.line(start=(120*cm,(n*16+n3*12+10)*cm),end=(95*cm,(n*16+n3*12+10)*cm)))
			hline.add(dwg.line(start=(180*cm,(n*16+n3*12+10)*cm),end=(205*cm,(n*16+n3*12+10)*cm)))
			hline.add(dwg.line(start=(150*cm,(n*16+n3*12-7)*cm),end=(150*cm,(42+n3*12)*cm)))
			hline.add(dwg.line(start=(150*cm,(n*16+n3*12+27)*cm),end=(150*cm,(n*16+n3*12+55)*cm)))

			y=120
			k=45
			p=50
			q=n*16+n3*12+75
			for j in xrange(0,len(tableau_attributs_entite)):
				if j==2:
					for x in xrange(0,len(tableau_attributs_entite[2])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black',text_decoration='underline'))
							p=p+8
						else:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black'))
							p=p+8
				if j==3:
					for x in xrange(0,len(tableau_attributs_entite[3])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[3][x],insert=(127.5*cm,q*cm),font_size=200,stroke='black',text_decoration='underline'))
							q=q+8
						else:
							dwg.add(dwg.text(tableau_attributs_entite[3][x],insert=(127.5*cm,q*cm),font_size=200,stroke='black'))
							q=q+8
				if j==0:	
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
							y=y+8
						else:	
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
							y=y+8
				y=120
				k=210
				if j==1:	
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
							y=y+8
						else:	
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
							y=y+8
				
						
			z=(n*16+n3*12+17.5)
			for x in xrange(0,len(tableau_attributs_association[0])):
				dwg.add(dwg.text(tableau_attributs_association[0][x],insert=(140*cm,z*cm),font_size=200,stroke='black'))
				z=z+8
		else:
			dwg.add(dwg.rect(insert=(40*cm,100*cm), size=(55*cm,(n1*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(40*cm,110*cm),end=(95*cm,110*cm)))
			dwg.add(dwg.text(tableau_nom_entite[0],insert=(45*cm,107.5*cm),font_size=200,stroke='black'))
			
			dwg.add(dwg.rect(insert=(205*cm,100*cm), size=(55*cm,(n2*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(205*cm,110*cm),end=(260*cm,110*cm)))
			dwg.add(dwg.text(tableau_nom_entite[1],insert=(210*cm,107.5*cm),font_size=200,stroke='black'))
			
			dwg.add(dwg.rect(insert=(122.5*cm,(30)*cm), size=(55*cm,(n3*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(122.5*cm,(40)*cm),end=(177.5*cm,(40)*cm)))
			dwg.add(dwg.text(tableau_nom_entite[2],insert=(127.5*cm,(37.5)*cm),font_size=200,stroke='black'))
			y=120
			k=45
			p=50
			for j in xrange(0,len(tableau_attributs_entite)):
				if j==2:
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black',text_decoration='underline'))
							p=p+8
						else:
							dwg.add(dwg.text(tableau_attributs_entite[2][x],insert=(127.5*cm,p*cm),font_size=200,stroke='black'))
							p=p+8
				else:		
					for x in xrange(0,len(tableau_attributs_entite[j])):
						if x==0:
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black',text_decoration='underline'))
							y=y+8
						else:	
							dwg.add(dwg.text(tableau_attributs_entite[j][x],insert=(k*cm,y*cm),font_size=200,stroke='black'))
							y=y+8
				y=120
				k=210	
	w=len(tableau_nom_entite)
	if((w!=1) and (w!=2) and (w!=3) and (w!=4)):
		x,y=20,50
		for i in xrange(0,len(tableau_nom_entite)):
			m=len(tableau_attributs_entite[i])
			dwg.add(dwg.rect(insert=(x*cm,y*cm), size=(55*cm,(m*12)*cm),fill='#CBCBC8', stroke='black', stroke_width=3))
			hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
			hline.add(dwg.line(start=(x*cm,(y+12.5)*cm),end=((x+55)*cm,(y+12.5)*cm)))
			dwg.add(dwg.text(tableau_nom_entite[i],insert=((x+5)*cm,(y+10)*cm),font_size=200,stroke='black'))
			z=y+10
			if y>(w*30+10):
				if x==20:
					hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
					hline.add(dwg.line(start=((x+55)*cm,(y+20)*cm),end=((118)*cm,(w*30+10)*cm)))
				else:
					hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
					hline.add(dwg.line(start=((x)*cm,(y+20)*cm),end=((178)*cm,(w*30+10)*cm)))
			else:
				if x==20:
					hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
					hline.add(dwg.line(start=((x+55)*cm,(y+20)*cm),end=((118)*cm,(w*30+10)*cm)))
				else:
					hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
					hline.add(dwg.line(start=((x)*cm,(y+20)*cm),end=((178)*cm,(w*30+10)*cm)))
			for j in xrange(0,m):
				dwg.add(dwg.text(tableau_attributs_entite[i][j],insert=((x+5)*cm,(z+10)*cm),font_size=200,stroke='black'))
				z=z+8
			if(i%2==0):
				x=220
			else:
				y=y+100
				x=20
		dwg.add(dwg.ellipse(center=(148*cm,(w*30+10)*cm), r=(30*cm,600),fill='#CBCBC8',stroke='black'))
		dwg.add(dwg.text(tableau_nom_association[0],insert=(127.5*cm,(w*30+5)*cm),font_size=200,stroke='black'))
		hline = dwg.add(dwg.g(id='hline', stroke='#E621AF',stroke_width=5))
		hline.add(dwg.line(start=(118*cm,(w*30+10)*cm),end=(178*cm,(w*30+10)*cm)))
		for x in xrange(0,len(tableau_attributs_association[0])):
			dwg.add(dwg.text(tableau_attributs_association[0][x],insert=(127.5*cm,(w*30+15)*cm),font_size=200,stroke='black'))
			z=z+8