import mariadb

def check(ID, PW):
    
    # MariaDB 연결 설정
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123123',
        'database': 'portfolio'  # 실제 데이터베이스 이름으로 변경
    }

    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()

        # 사용자 정보 조회 쿼리 실행
        query = "SELECT * FROM user WHERE ID = %s AND PW = %s"
        cursor.execute(query, (ID, PW))
        result = cursor.fetchone()

        return result  # 조회 결과 반환 (없으면 None)

    except mariadb.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        if conn:
            conn.close()
