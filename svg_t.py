import svgwrite
from svgwrite import cm, mm
import datetime
#traitement de la page
def background(fic_svg):
	date_time = datetime.datetime.now()
	chaine=str(date_time).split(" ")
	time=chaine[1].split(".")
	dwg=svgwrite.Drawing(fic_svg,profile='full',fill='black')
	dwg.add(dwg.rect(insert=(0*cm, 0*cm), size=('100%','100%'),fill='#E0F8E6', stroke='black', stroke_width=3))
	dwg.add(dwg.image('aa.jpeg', insert=(250*cm,5*cm), size=(50*cm,25*cm)))
	dwg.add(dwg.image('d.jpg', insert=(0*cm,0*cm), size=('100%','100%')))
	dwg.add(dwg.text('Date: '+chaine[0],insert=(10*cm,10*cm),font_size=150,stroke="#2E9AFE"))
	dwg.add(dwg.text('Time: '+time[0],insert=(10*cm,20*cm),font_size=150,stroke='#2E9AFE'))
	return dwg
	#variable text
text_color='black'
text_font=200
	#variable line
line_entite_color="#B40431"
line_color='#0431B4'
card_color="#B40431"
line_width=13
line_entite_width=20
fill_in='#A9F5F2'
#Fonction qui cree les entites
def create_entity(tableau_nom_entite,tableau_nom_association,dwg,tableau_attributs_entite,tableau_attributs_association,attrib_interne_entite,attrib_interne_association):
	print(len(tableau_nom_association))
	if(len(tableau_nom_entite))==1:
		ox,oy,rw,rh=70,50,30,600
		x1=180
		y1=(len(tableau_nom_association)*50)/2 + 10
		width=55
		height=(len(tableau_attributs_entite[0])+1)*12
		if(len(tableau_nom_association)<=2):
			ox=147.5
			x1=120
			y1=80
		o1=22
		entite(dwg,x1,y1,width,height)
		set_text(dwg,x1+5,y1+8,tableau_nom_entite[0])
		set_attribute(dwg,tableau_attributs_entite[0],x1,y1)
		s=0
		y=y1
		o=15
		w=0
		for i in range(0,len(tableau_nom_association)):
			if(len(tableau_nom_association)<=2):
				association(dwg,ox,oy,rw,rh)
				set_link(dwg,x1+15,y,x1+15,oy+o)
				ecrit_cardinalite(dwg,x1+4,y-5+s,0,i)
				set_link(dwg,x1+40,y,x1+40,oy+o)
				ecrit_cardinalite(dwg,x1+41,y-5+s,0,i)
				set_text(dwg,ox-15,oy-8,tableau_nom_association[i])
				set_attribute(dwg,tableau_attributs_association[i],ox-20,oy-15)
				oy=oy+(len(tableau_attributs_entite[0])+1)*12+62
				y=(len(tableau_attributs_entite[0])+1)*12+80
				o=-15
				if len(tableau_nom_association)==2:
					s=17
			
			else:
				association(dwg,ox,oy,rw,rh)
				set_link(dwg,x1,y+15,ox+26.5,oy-8)
				set_link(dwg,x1,y+15,ox+26.5,oy+8)
				ecrit_cardinalite(dwg,ox+35,oy-8,1,i)
				ecrit_cardinalite(dwg,ox+35,oy+8,1,i)
				set_text(dwg,ox-15,oy-8,tableau_nom_association[i])
				set_attribute(dwg,tableau_attributs_association[i],ox-20,oy-15)
				oy=oy+50
				w=w+20
	if len(tableau_nom_entite)==2:
		x1,x2,y1,y2=40,205,(len(tableau_nom_association)*50)/2 + 10,(len(tableau_nom_association)*50)/2 + 10
		ox,oy,rw,rh=150,50,30,600
		x=x1
		y=y1
		width=55
		for i in range(0,2):
			height=(len(tableau_attributs_entite[i])+1)*12
			entite(dwg,x,y,width,height)
			set_text(dwg,x+5,y+8,tableau_nom_entite[i])
			set_attribute(dwg,tableau_attributs_entite[i],x,y)
			x=x2
			y=y2
		for i in range(0,len(tableau_nom_association)):
			association(dwg,ox,oy,rw,rh)
			set_text(dwg,ox-15,oy-8,tableau_nom_association[i])
			set_attribute(dwg,tableau_attributs_association[i],ox-20,oy-15)
			x=x1+width
			y=y1+15
			xo=ox-30
			s=8
			for j in range(0,len(attrib_interne_entite)):
				if attrib_interne_entite[j][0] in attrib_interne_association[i]:
					if len(attrib_interne_association[i])==1:
						set_link(dwg,xo+3.5,oy-8,x,y)
						set_link(dwg,xo+4,oy+8,x,y)
						if(j%2==0):
							s=-8
							sa=-32
						else:
							s=8
							sa=15
						ecrit_cardinalite(dwg,xo+s,oy-10,i,j)
						ecrit_cardinalite(dwg,xo+s,oy+8,i,j)
						x=205
						sa=-15
						xo=ox+30
					else:
						set_link(dwg,xo,oy,x,y)
						ecrit_cardinalite(dwg,x+s,oy+5,i,j)
						x=205
						s=-20
						xo=ox+30
				else:
					x=205
					xo=ox+22.7
			oy=oy+50
	if len(tableau_nom_entite)!=1 and len(tableau_nom_entite)!=2:
		x1,x2,y1,y2=40,205,100,100
		ox,oy,rw,rh=150,80,30,600
		width=55
		x=x1
		y=y1
		for i in range(0,len(tableau_nom_entite)):
			height=(len(tableau_attributs_entite[i])+1)*12
			entite(dwg,x,y,width,height)
			set_text(dwg,x+5,y+8,tableau_nom_entite[i])
			set_attribute(dwg,tableau_attributs_entite[i],x,y)
			if(i%2==0):
				x=x2
			else:
				y=y+80
				x=x1
		for i in range(0,len(tableau_nom_association)):
			if(len(tableau_nom_association)==1):
				oy=150
			association(dwg,ox,oy,rw,rh)
			set_text(dwg,ox-15,oy-8,tableau_nom_association[i])
			set_attribute(dwg,tableau_attributs_association[i],ox-20,oy-15)
			x=x1+width
			y=y1+15
			xo=ox-30
			yo=oy
			print(attrib_interne_entite)
			s=20
			sa=-10
			for j in range(0,len(attrib_interne_entite)):
				if attrib_interne_entite[j][0] in attrib_interne_association[i]:
					if len(attrib_interne_association[i])==1:
						if(j%2==0):
							set_link(dwg,xo+3.5,yo-8,x,y)
							set_link(dwg,xo+4,yo+8,x,y)
							ecrit_cardinalite(dwg,xo-s,yo+sa+15,i,j)
							ecrit_cardinalite(dwg,xo-s,yo-sa+15,i,j)
						else:
							set_link(dwg,xo-2,yo-8,x,y)
							set_link(dwg,xo-2,yo+8,x,y)
							ecrit_cardinalite(dwg,xo-s,yo+sa+15,i,j)
							ecrit_cardinalite(dwg,xo-s,yo-sa+15,i,j)
					else:
						set_link(dwg,xo,oy,x,y)
						ecrit_cardinalite(dwg,xo-s,yo+sa,i,j)
				if(j%2==0):
					x=205
					xo=ox+28
					s=-5
				if(j%2 != 0):
					x=x1+55
					xo=ox-30
					y=y+80
					s=20
					sa=20
			oy=oy+50
				
def entite(dwg,x,y,width,height):
	dwg.add(dwg.rect(insert=(x*cm,y*cm),size=(width*cm,height*cm),fill=fill_in,stroke=line_entite_color,stroke_width=line_entite_width))			
	hline = dwg.add(dwg.g(id='hline', stroke=line_color,stroke_width=line_width))
	hline.add(dwg.line(start=(x*cm,(y+15)*cm),end=((x+width)*cm,(y+15)*cm)))
def association(dwg,ox,oy,rw,rh):
	dwg.add(dwg.ellipse(center=(ox*cm,oy*cm), r=(rw*cm,rh),fill=fill_in,stroke=line_entite_color,stroke_width=line_entite_width))
	hline = dwg.add(dwg.g(id='hline', stroke=line_color,stroke_width=line_width))
	hline.add(dwg.line(start=((ox-rw)*cm,(oy)*cm),end=((ox+rw)*cm,oy*cm)))
def set_text(dwg,x,y,text):
	dwg.add(dwg.text(text,insert=(x*cm,y*cm),font_size=text_font,stroke=text_color))
def set_link(dwg,xdeb,ydeb,xfin,yfin):
	hline = dwg.add(dwg.g(id='hline', stroke=line_color,stroke_width=line_width))
	hline.add(dwg.line(start=(xdeb*cm,ydeb*cm),end=((xfin*cm,yfin*cm))))
def set_attribute(dwg,attribute,x,y):
	o1=22
	for i in range(0,len(attribute)):
		if(i==0):
			
			dwg.add(dwg.text(attribute[i],insert=((x+5)*cm,(y+o1)*cm),font_size=text_font,stroke=text_color,text_decoration='underline'))
			o1=o1+8
		else:
			set_text(dwg,x+5,y+o1,attribute[i])
			o1=o1+8
def ecrit_cardinalite(dwg,x,y,j,i):
	dwg.add(dwg.text("(m"+str(i)+""+str(j)+",M"+str(i)+""+str(j)+")",insert=(x*cm,y*cm),font_size=130,stroke=card_color))
def ecrire_precision(dwg,tableau_nom_entite,tableau_nom_association):
	dwg.add(dwg.text("Nombre d\'entite: "+str(len(tableau_nom_entite)),insert=(10*cm,30*cm),font_size=150,stroke='#2E9AFE'))
def json_svg(dwg,tableau_nom_entite,tableau_nom_association,tableau_attributs_entite,tableau_attributs_association):
	x=40
	y=80
	xo=120
	s=0
	k=0
	for i in range(0,len(tableau_nom_entite)):
		print(tableau_nom_entite)
		entite(dwg,x,y,55,(len(tableau_attributs_entite[i])+1)*12)
		set_text(dwg,x+5,y+8,tableau_nom_entite[i])
		set_attribute(dwg,tableau_attributs_entite[i],x,y)
		set_link(dwg,x+55+s,y+15,xo,160)
		ecrit_cardinalite(dwg,x+55+s+k,y+15,1,i)
		if i%2==0:
			x=205
			xo=180
			s=-55
			k=-15
		else:
			x=40
			y=y+120
			xo=120
			s=0	
			k=0
	association(dwg,150,160,30,600)
	set_text(dwg,135,160-5,tableau_nom_association[0])
