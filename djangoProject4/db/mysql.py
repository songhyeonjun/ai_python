import pymysql


def read() :
    try :
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='trip',
            charset='utf8'
        )
        print("1.  연결 성공", conn.host_info)
        # 연결 된 통로 (stream)을 통해, sl문을 보내기
        # 2. 연결 된 통로를 지정(저븐할 수 있는 커서 객체를 획득)
        cur = conn.cursor()

        # sql문을 보내기
        sql = "select place_idx, place_info, place_area, place_view, place_like from place order by place_view desc limit 5;"

        result = cur.execute(sql)
        print('sql문 전송 결과', result)

        row = cur.fetchall()

        conn.close()
        return row

    except Exception as e :
        print("db 연결 중 에러 발생")
        print('에러 정보', e)


def read2() :
    try :
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='trip',
            charset='utf8'
        )
        print("1.  연결 성공", conn.host_info)
        # 연결 된 통로 (stream)을 통해, sl문을 보내기
        # 2. 연결 된 통로를 지정(저븐할 수 있는 커서 객체를 획득)
        cur = conn.cursor()

        # sql문을 보내기
        sql = "select place_idx, place_info, place_area, place_view, place_like from place order by place_like desc limit 5;"

        result = cur.execute(sql)
        print('sql문 전송 결과', result)

        row = cur.fetchall()

        conn.close()
        return row

    except Exception as e :
        print("db 연결 중 에러 발생")
        print('에러 정보', e)
