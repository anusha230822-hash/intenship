from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_rooms (id INT PRIMARY KEY, room_type VARCHAR(50), price DECIMAL(10,2), available BOOLEAN DEFAULT TRUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_hotel_customers (id INT PRIMARY KEY, name VARCHAR(100), phone VARCHAR(30))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_bookings (id INT PRIMARY KEY, room_id INT, customer_id INT, check_in DATE, check_out DATE NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_hotel_payments (id INT PRIMARY KEY, booking_id INT, amount DECIMAL(10,2), status VARCHAR(30))")
    connection.commit()
    cursor.close()


def book_room(connection, booking_id, room_id, customer_id, check_in):
    cursor = connection.cursor()
    cursor.execute("UPDATE mini_rooms SET available = FALSE WHERE id = %s AND available = TRUE", (room_id,))
    if cursor.rowcount != 1:
        connection.rollback()
        raise ValueError("Room is unavailable.")
    cursor.execute("INSERT INTO mini_bookings VALUES (%s, %s, %s, %s, NULL)", (booking_id, room_id, customer_id, check_in))
    connection.commit()
    cursor.close()


def checkout(connection, booking_id, room_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE mini_bookings SET check_out = CURRENT_DATE WHERE id = %s", (booking_id,))
    cursor.execute("UPDATE mini_rooms SET available = TRUE WHERE id = %s", (room_id,))
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("Hotel Management System ready.")
    database.close()
