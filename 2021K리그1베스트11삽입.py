import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek',
                       password='siattiger',
                       db='earlykross', charset='utf8')
season = "2021"
round = 19
p1 =	"조현우"
p2 =	"델브리지"
p3 =	"민상기"
p4 =	"정태욱"
p5 =	"송민규"
p6 =	"김민우"
p7 =	"이영재"
p8 =	"이동준"
p9 =	"라스"
p10 =	"김건희"
p11 =	"뮬리치"




players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
ppp = []
for p in players:
    curs = conn.cursor()
    sql = '''select p_id from player where name=%s'''
    result = curs.execute(sql, p)
    row = curs.fetchall()

    for r in row:
        ppp.append(r)

sql = '''insert into besteleven(round, season, m_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
curs.execute(sql, (
    round, season, 1, ppp[0], ppp[1], ppp[2], ppp[3], ppp[4], ppp[5], ppp[6], ppp[7], ppp[8], ppp[9], ppp[10]))
conn.commit()

conn.close()
