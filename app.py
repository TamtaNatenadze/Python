def select_data():
    cursor.execute("SELECT * FROM Russian Nuclear forces")
    result = cursor.fetchall()
    for i in result:
        print(i)


def select_data(id):
    cursor.execute(f"SELECT FROM Russian Nuclear forces WHERE id={id}")
    conn.commit()


requests.get(url, params={key: value}, args)


def INSERT_data(ID, TYPE/NATO DESIGNATION, LAUNCHERS):
    cursor.execute(f"""INSERT INTO Russian Nuclear forces (ID, TYPE/NATO DESIGNATION, LAUNCHERS) VALUES ({ID}, {TYPE/NATO DESIGNATION}, {LAUNCHERS}""")
    conn.commit()


requests.post(url, data={key: value}, json={key: value}, args)


def delete_data(id):
    cursor.execute(f"DELETE FROM Russian Nuclear forces WHERE id={id}")
    conn.commit()


requests.delete(url, args)


def UPDATE_data(TYPE/RUSSIAN DESIGNATION, LAUNCHERS):
    cursor.execute(f"UPDATE Russian Nuclear forces SET TYPE/RUSSIAN DESIGNATION={name}, LAUNCHERS={name} WHERE ID=3")
    conn.commit()


requests.put(url, data, args)	


     