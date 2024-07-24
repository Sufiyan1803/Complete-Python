import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
               ''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("The list is empty.")
    else:
        print(f"{'ID':<5} {'Name':<30} {'Time':<20}")
        print("=" * 55)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<30} {row[2]:<20}")

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_ID, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_ID))
    conn.commit()

def delete_video(video_ID):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_ID,))
    conn.commit()

def main():
    while True:
        print("YOUTUBE MANAGER USING SQLITE3 DB")

        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
            
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)  

        elif choice == '3':
            video_ID = int(input("Enter Video ID to update: "))
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_ID, name, time)  
        
        elif choice == '4':
            video_ID = int(input("Enter Video ID to delete: "))
            delete_video(video_ID)
        
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
 
    conn.close()

if __name__ == "__main__":
    main()
