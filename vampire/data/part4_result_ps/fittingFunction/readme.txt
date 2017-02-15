产生与FePt该类物质相符合的sigma公式


	const=64
	Tc=730.0   #705
	gamma=0.84 #0.409
	t=x
	if t<Tc:
		yy=(Tc/t-1)**gamma*const
	else:
		yy=0
	return yy

