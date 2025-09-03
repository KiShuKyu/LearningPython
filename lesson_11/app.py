# Youtube Video manager sqlite3
import sqlite3

conn = sqlite3.connect("youtube_videos.db")  # con = connect
# cursor = cursor (ye data base se directly baat kr sakta h query ki form me)


cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
               ''')


def list_vds():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No Video to show")
    else:
        for row in rows:  # we can use either fetchall or fetchone
            print(row)


def add_vds(name, time):
    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_vds(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",
                   (new_name, new_time, video_id))
    conn.commit()


def delete_vds(video_id):
    # value tuple milte h single h tabh bhi tuple h
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit.")
        choice = input("Enter Your choice: \n")

        if choice == '1':
            list_vds()
        elif choice == '2':
            name = input("Enter the video name:")
            time = input("Enter the video time:")
            add_vds(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name:")
            time = input("Enter the video time:")
            update_vds(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_vds(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice.")

    conn.close()  # good to close connect db corrupt chances slims


if __name__ == "__main__":
    main()
