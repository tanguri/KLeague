# 선수개인기록 뽑기
import time, os
import pymysql

from bs4 import BeautifulSoup

path = "2021구단별기록"
file_list = os.listdir(path)
file_list_html = [file for file in file_list if file.endswith(".html")]


def name(x):
    return {
        '울산': 1, '수원': 2, '포항': 3, '제주': 4, '전북': 5, '부산': 6, '전남': 7, '성남': 8, '서울': 9, '대전': 10, '대구': 17, '인천': 18,
        '경남': 20, '강원': 21, '광주': 22, '부천': 26, '안양': 27, '수원FC': 29, '서울E': 31, '안산': 32, '충남아산': 34, '김천': 35}[x]


# MySQL Connection 연결
conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek',
                       password='siattiger',
                       db='earlykross', charset='utf8')

for file in file_list_html:
    f = open('{}/{}'.format(path, file), 'r', encoding='utf-8')

    print(f)
    soup = BeautifulSoup(f, 'html.parser')

    c_id = file.replace('.html', '')

    tr = soup.select('#tab-1 > div > div > table > tbody > tr')

    # 구단 별 선수 숫자 돌리기
    for j in range(len(tr)):
        curs = conn.cursor()

        td = soup.select('#tab-1 > div > div > table > tbody > tr:nth-child({}) > td'.format(j + 1))

        if len(td) > 1:
            name = td[0].text
            sql = '''select p_id from player where name=%s and c_id=%s'''
            result = curs.execute(sql, (name, c_id))

            if result > 0:
                row = curs.fetchone()
                p_id = row[0]

                season = '2021'

                played = td[2].text
                played_in = td[3].text
                played_out = td[4].text
                inout_total = td[5].text
                fh_goal = td[6].text
                sh_goal = td[7].text
                ot_goal = td[8].text
                total_goal = td[9].text
                assist = td[10].text
                gk = td[11].text
                ck = td[12].text
                fc = td[13].text
                fs = td[14].text
                os = td[15].text
                st = td[16].text
                sot = td[17].text
                pk_goal = td[18].text
                pk_fail = td[19].text
                pk_per = td[20].text
                yellow = td[21].text
                red = td[22].text
                ga = td[23].text
                og = td[24].text

                if td[25].text == '':
                    rating = float(0.0)
                else:
                    rating = td[25].text

                print(season, c_id, td[0].text, p_id, played, played_in, played_out, inout_total, fh_goal, sh_goal,
                      ot_goal,
                      total_goal, assist, gk, ck, fc, fs, os, st, sot, pk_goal, pk_fail, pk_per, yellow, red, ga,
                      og, rating)

                # SQL문 실행
                sql = '''insert into player_record(season, c_id, p_id, played, played_in, played_out, inout_total, fh_goal, sh_goal, ot_goal, total_goal,
                 assist, gk, ck, fc, fs, os, st, sot, pk_goal, pk_fail, pk_per, yellow, red, ga, og, rating)
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                curs.execute(sql, (
                    season, c_id, p_id, played, played_in, played_out, inout_total, fh_goal, sh_goal, ot_goal,
                    total_goal,
                    assist, gk, ck, fc, fs, os, st, sot, pk_goal, pk_fail, pk_per, yellow, red, ga, og, rating))
                conn.commit()

                # Connection 닫기
conn.close()
