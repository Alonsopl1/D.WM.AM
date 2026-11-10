digraph G {graph [label="C3 · Componentes de Auth Service",labelloc=t,fontname="DejaVu Sans",fontsize=23,bgcolor="white",pad=.35,ranksep=.7];node[shape=box,style="rounded,filled",fontname="DejaVu Sans",fontsize=12,color="#447285",fillcolor="#E8F3F8",margin=".20,.15"];edge[fontname="DejaVu Sans",fontsize=10,color="#526677"];rankdir=LR;
 gw[label="Gateway\n/login, /register",fillcolor="#F5F5F9"];
 login[label="Verificador de credenciales\nscrypt + sal"];
 session[label="Gestor de sesión\nJWT de 30 minutos"];
 idrepo[label="Repositorio de identidad\nclients (SQLite)",fillcolor="#F9ECD9"];
 sec[label="Proveedor de secretos\nJWT_SIGNING_KEY (archivo)\nSin revocación individual",fillcolor="#E4ECE3"];
 gw->login->idrepo;login->session;sec->session[style=dotted];}